from pydantic import BaseModel, model_validator, Field

from data_access_layer import point_intersects_pennsylvania


class LocationIntersectionRequest(BaseModel):
    latitude: float = Field(default=10)
    longitude: float = Field(default=10)

    @model_validator(mode='after')
    def lat_long_in_pennsylvania(self):
        if not point_intersects_pennsylvania(self.latitude, self.longitude):
            raise ValueError('Lat/Long must be located within Pennsylvania')
        return self


class LatLongRequest(BaseModel):
    latitude: float = Field(default=10)
    longitude: float = Field(default=10)
