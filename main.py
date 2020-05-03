from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import aiosqlite

app = FastAPI()

@app.on_event("startup")
async def startup():
	app.db_connection = await aiosqlite.connect('chinook.db')

@app.on_event("shutdown")
async def shutdown():
	await app.db_connection.close()

@app.get("/tracks")
async def tracks(page: int = 0, per_page: int = 10):
	app.db_connection.row_factory = aiosqlite.Row
	cursor = await app.db_connection.execute("SELECT * FROM tracks ORDER BY TrackId LIMIT :per_page OFFSET :per_page*:page",
		{'page': page, 'per_page': per_page})
	tracks = await cursor.fetchall()
	return tracks

@app.get("/tracks/composers")
async def tracks_composers(response: Response, composer_name: str):
	app.db_connection.row_factory = lambda cursor, x: x[0]
	cursor = await app.db_connection.execute("SELECT Name FROM tracks WHERE Composer = ? ORDER BY Name", (composer_name, ))
	tracks = await cursor.fetchall()
	if len(tracks) == 0:
		response.status_code = status.HTTP_404_NOT_FOUND
		return {"detail":{"error":"Jakis error"}}
	return tracks


class New_album(BaseModel):
    title: str
    artist_id: int


@app.post("/albums")
async def artists_add(new_album: New_album):
    app.db_connection.row_factory = None
    cursor = await app.db_connection.execute("SELECT ArtistId FROM artists WHERE ArtistId = ?", (new_album.artist_id, ))
    result = await cursor.fetchall()
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": {"error": "Jakis error"}}
    cursor = app.db_connection.execute(
        f"INSERT INTO tracks (name) VALUES {new_album.title}",
    )
    app.db_connection.commit()
    return {
        "artist_id": new_album.artist_id,
        "artist_name": new_album.titile
    }
