from typing import Annotated

from fastapi import FastAPI, Body, Depends, HTTPException
from pydantic import BaseModel, Field

from data_access_layer import point_intersects_pennsylvania
from schemas import LocationIntersectionRequest, LatLongRequest

app = FastAPI()


@app.post(
    "/intersection_schema/",
    tags=["Pydantic based validation"]

)
def intersection(
        point: LocationIntersectionRequest = Body(...)
):
    return point

# https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
def point_intersects_pa(
        point: Annotated[LatLongRequest, Body(...)]
):
    if not point_intersects_pennsylvania(point.latitude, point.longitude):
        raise HTTPException(status_code=422,
                            detail='Lat/Long must be located within Pennsylvania')


@app.post(
    "/intersection_dependency/",
    tags=["Dependency based validation"],
    dependencies=[Depends(point_intersects_pa)]
)
def intersection(
        point: LatLongRequest = Body(...)
):
    return point
