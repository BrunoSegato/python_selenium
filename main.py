import uvicorn
from fastapi import FastAPI, Request
from dotenv import dotenv_values
from pymongo import MongoClient
from cornerpro.routers.games import router as game_router

config = dotenv_values(".env")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Automação Corner Pro"}


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["NOSQL_DB_NAME"]]
    print("Connected to the MongoDB database!!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Disconnected to the MongoDB database!!")


app.include_router(game_router, tags=["games"], prefix="/game")


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
