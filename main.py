from typing import Annotated

from fastapi import FastAPI, Body, Depends, HTTPException

import data_access_layer as dal
from schemas import PointWithValidation, PointNoValidation, Geom

app = FastAPI()


@app.post(
    "/intersection-with-schema/",
    tags=["Pydantic based validation"],
    response_model=PointWithValidation,
)
def intersection(point: PointWithValidation = Body(...)):
    # --------------------------------------------------------------------------------------------------------------
    # Show the PointWIthValidation validation happens also on the return because of the response_model
    # --------------------------------------------------------------------------------------------------------------
    """Check if point intersects Pennsylvania"""
    return {
        "latitude": point.latitude,
        "longitude": point.longitude,
    }
    # return {"latitude":0, "longitude":0}


# --------------------------------------------------------------------------------------------------------------
# Dependency based validation
# SEE - https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
# --------------------------------------------------------------------------------------------------------------


def point_intersects_pa(point: Annotated[PointNoValidation, Body(...)]):
    """Check point is within Pennsylvania"""
    if not dal.point_intersection_pennsylvania_sql(point.latitude, point.longitude):
        raise HTTPException(
            status_code=422, detail="Lat/Long must be located within Pennsylvania"
        )


@app.post(
    "/intersection_dependency/",
    tags=["Dependency based validation"],
    dependencies=[Depends(point_intersects_pa)],
)
def pit_neighborhood(point: PointNoValidation = Body(...)):
    return dal.point_in_neighborhood_sql(point.latitude, point.longitude)


# --------------------------------------------------------------------------------------------------------------
# Bonus - Not in presentation
# --------------------------------------------------------------------------------------------------------------
@app.post("/distance/", response_model=None)
def distance(
    point: PointNoValidation = Body(description="Point to calculate distance from"),
    geom: Geom = Body(...),
):
    """Calculate distance from point to provided geometry"""
    return dal.point_distance_from_geom(point.latitude, point.longitude, geom.geom)
