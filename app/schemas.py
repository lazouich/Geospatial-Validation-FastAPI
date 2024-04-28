from typing import Annotated

from geoalchemy2 import Geometry
from pydantic import BaseModel, model_validator, Field, field_validator

import data_access_layer as dal


class PointWithValidation(BaseModel):
    """Latitude and Longitude - must be within Pennsylvania"""

    latitude: float = Field(default=40.252)
    longitude: float = Field(default=-80.054)

    @model_validator(mode='after')
    def lat_long_in_pennsylvania(self):
        """Check point is within Pennsylvania"""
        if not dal.point_intersects_pennsylvania(self.latitude, self.longitude):
            raise ValueError('Lat/Long must be located within Pennsylvania')
        return self


class PointNoValidation(BaseModel):
    """Latitude and Longitude - no validation"""

    latitude: float = Field(default=40.444975822624855)
    longitude: float = Field(default=-79.99701625706184)


class Geom(BaseModel):
    """Geometry - must be a valid geometry"""

    geom: Annotated[str, Geometry] = Field(
        description='WKT string representing geometry',
        default='POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))',
    )

    @field_validator('geom', mode='before')
    @classmethod
    def geom_is_valid(cls, geom):
        if not dal.geom_is_valid(geom):
            raise ValueError('Provided geometry is not valid')
        return geom
