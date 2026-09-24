from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.game import GameCreate, GameResponse
from app.services.game_service import (
    create_game,
    get_games,
    get_game,
    delete_game,
    get_dashboard
)

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


@router.post("/", response_model=GameResponse, status_code=201)
def create(game: GameCreate, db: Session = Depends(get_db)):
    return create_game(db, game)


@router.get("/", response_model=list[GameResponse])
def list_games(db: Session = Depends(get_db)):
    return get_games(db)


@router.get("/dashboard/summary")
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard(db)


@router.get("/{game_id}", response_model=GameResponse)
def find_game(game_id: int, db: Session = Depends(get_db)):
    game = get_game(db, game_id)

    if not game:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    return game


@router.delete("/{game_id}")
def remove_game(game_id: int, db: Session = Depends(get_db)):
    deleted = delete_game(db, game_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    return {
        "message": "Game deleted successfully"
    }