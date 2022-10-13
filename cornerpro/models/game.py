import uuid
from typing import Optional, Any
from pydantic import BaseModel, Field


class Game(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    bot: str = Field(description="Nome do Bot")
    name: str = Field(description="Nome do jogo")
    date: str = Field(description='Data do jogo')
    league: str = Field(description="Campeonato da partida")
    result: str = Field(description="Resultado da aposta")
    code: str = Field(description="Código do jogo no CornerPro")
    link: str = Field(description="Link do jogo")
    events: list[dict] = Field(description="Eventos do jogo")

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "bot": "FTEvo - DD",
                "name": "Cruzeiro x Ituano",
                "date": "2022-10-05 20:30",
                "league": "Brazil Serie B",
                "result": "2",
                "code": "q4823",
                "link": "https://cornerprobet.com/pt/analysis/q4823",
                "events": [
                    {
                        'time': '4',
                        'event': 'Golo Edu'
                    },
                    {
                        'time': '10',
                        'event': 'Canto'
                    }
                ]
            }
        }


class GameUpdate(BaseModel):
    name: Optional[str]
    bot: Optional[str]
    date: Optional[str]
    code: Optional[str]
    league: Optional[str]
    result: Optional[str]
    link: Optional[str]
    events: Optional[list[dict]]

    class Config:
        schema_extra = {
            "example": {
                "name": "Cruzeiro x Ituano",
                "bot": "FTEvo - DD",
                "date": "2022-10-05 20:30",
                "league": "Brazil Serie B",
                "code": "q4823",
                "result": "2",
                "link": "https://cornerprobet.com/pt/analysis/q4823",
                "events": [
                    {
                        'time': '4',
                        'event': 'Golo Edu'
                    },
                    {
                        'time': '10',
                        'event': 'Canto'
                    }
                ]
            }
        }
