#!/usr/bin/python3
""" City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """class city.
    args:
        state_id : The state id.
        name : The name of the city.
    """

    state_id = ""
    name = ""

