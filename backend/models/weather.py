from db import Base

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from sqlalchemy import Column, String, DateTime, JSON

class TodayWeather(Base):
  __tablename__ = 'today_weather'
  ##################
  id = Column(String(50), primary_key=True)
  ##################
  region = Column(String(500))
  precip = Column(String(5))
  humidity = Column(String(5))
  wind = Column(JSON)
  dayhour = Column(String(50))
  created_at = Column(DateTime(timezone=False))
  @property
  def label(self):
    return self.id
  
class NextDaysWeather(Base):
  __tablename__ = 'next_days_weather'
  ##################
  id = Column(String(50), primary_key=True)
  ##################
  day = Column(String(50))
  comment = Column(String(50))
  min_temp = Column(JSON)
  max_temp = Column(JSON)
  created_at = Column(DateTime(timezone=False))
  @property
  def label(self):
    return self.id

class WeatherScheme(BaseModel):
  id: Optional[str]
  count: Optional[int]
  user_id: Optional[str]
  service_type: Optional[str]
  created_at: Optional[datetime]
  class Config: orm_mode = True