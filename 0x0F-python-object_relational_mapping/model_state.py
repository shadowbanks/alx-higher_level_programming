#!/usr/bin/python3
"""
State Schema
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence


Base = declarative_base()


class State(Base):
    """
    Create State Schema
    """

    __tablename__ = "states"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
