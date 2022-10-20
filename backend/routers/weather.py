from app import app
from typing import List
from pydantic import BaseModel
import requests as http

class TodayWeatherModel(BaseModel):
  temp: dict
  wind: dict
  precip: str
  dayhour: str
  comment: str
  humidity: str

class NextDaysWeatherModel(BaseModel):
  day: str
  min_temp: dict
  max_temp: dict

class ResponseModel(BaseModel):
  region: str
  currentConditions: TodayWeatherModel
  next_days: List[NextDaysWeatherModel]

@app.get('/api/weather', response_model=ResponseModel)
def get_weather():
  response = http.get('https://weatherdbi.herokuapp.com/data/weather/moscow')
  if response.ok:
    data = response.json()
    schema = ResponseModel(**data)
    return schema