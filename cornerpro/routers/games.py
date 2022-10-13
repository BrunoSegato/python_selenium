from fastapi import APIRouter, status, Request, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from cornerpro.models.game import Game

router = APIRouter()


@router.get("/", response_description="List all games", response_model=list[Game])
def list_games(request: Request):
    games = list(request.app.database["games"].find(limit=100))
    return games


@router.get("/{identifier}", response_description="Get a single game by id", response_model=Game)
def find_game(identifier: str, request: Request):
    if (game := request.app.database["games"].find_one({"_id": identifier})) is not None:
        return game
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Game with ID {identifier} not found")


@router.get("/code/{code}", response_description="Get a single game by code", response_model=Game)
def find_game_by_code(code: str, request: Request):
    if (game := request.app.database["games"].find_one({"code": code})) is not None:
        return game
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Game with Code {code} not found")


@router.post("/", response_description="Create a new game", response_model=Game, status_code=status.HTTP_201_CREATED)
def create_game(request: Request, game: Game = Body(...)):
    game = jsonable_encoder(game)
    new_game = request.app.database["games"].insert_one(game)
    created_game = request.app.database["games"].find_one(
        {"_id": new_game.inserted_id}
    )
    return created_game
