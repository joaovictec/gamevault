from pydantic import BaseModel, Field


class GameCreate(BaseModel):
    name: str = Field(min_length=1)
    platform: str = Field(min_length=1)
    purchase_price: float = Field(ge=0)
    sale_price: float = Field(ge=0)


class GameUpdate(BaseModel):
    name: str | None = None
    platform: str | None = None
    purchase_price: float | None = Field(default=None, ge=0)
    sale_price: float | None = Field(default=None, ge=0)
    status: str | None = None


class GameResponse(GameCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
