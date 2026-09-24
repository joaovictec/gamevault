from sqlalchemy import Column, Integer, String, Float

from app.database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    platform = Column(String, nullable=True)
    purchase_price = Column(Float,nullable=False)
    sale_price= Column(Float,nullable = False)
    status = Column(String, default = "available",
                    nullable=False)