from sqlalchemy.orm import Session

from app.models.game import Game
from app.schemas.game import GameCreate


def create_game(db: Session, game_data: GameCreate):
    game = Game(
        name=game_data.name,
        platform=game_data.platform,
        purchase_price=game_data.purchase_price,
        sale_price=game_data.sale_price,
        status="available"
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    return game


def get_games(db: Session):
    return db.query(Game).all()


def get_game(db: Session, game_id: int):
    return db.query(Game).filter(Game.id == game_id).first()


def delete_game(db: Session, game_id: int):
    game = get_game(db, game_id)

    if not game:
        return False

    db.delete(game)
    db.commit()

    return True


def get_dashboard(db: Session):
    games = get_games(db)

    total_items = len(games)

    inventory_cost = sum(
        game.purchase_price
        for game in games
        if game.status == "available"
    )

    potential_revenue = sum(
        game.sale_price
        for game in games
        if game.status == "available"
    )

    potential_profit = potential_revenue - inventory_cost

    sold_items = sum(
        1
        for game in games
        if game.status == "sold"
    )

    return {
        "total_items": total_items,
        "inventory_cost": inventory_cost,
        "potential_revenue": potential_revenue,
        "potential_profit": potential_profit,
        "sold_items": sold_items
    }