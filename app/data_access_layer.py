from typing import Annotated

import sqlalchemy.exc
from geoalchemy2 import Geometry, Geography
from geoalchemy2.functions import (
    ST_MakePoint,
    ST_Intersects,
    ST_SetSRID,
    ST_Distance,
    ST_GeomFromText,
    ST_IsValid,
)
from sqlalchemy import text, cast
from sqlalchemy.orm import sessionmaker

from database import engine
from models import PABoundary

Session = sessionmaker(bind=engine)


# --------------------------------------------------------------------------------------------------------------
def point_intersects_pennsylvania_sql(latitude: float, longitude: float):
    """Check if point intersects Pennsylvania using raw SQL"""
    session = Session()
    sql_text = text(
        f"""
        SELECT gid
        FROM pa_boundary
        WHERE ST_Intersects(
            ST_SetSRID(ST_MakePoint({longitude}, {latitude}), 4326),
            geom
        );
        """
    )
    valid_point = session.execute(sql_text).all()
    return valid_point


def point_intersects_pennsylvania(latitude: float, longitude: float):
    """Check if point intersects Pennsylvania using SQLAlchemy/GeoAlchemy2"""
    session = Session()
    valid_point = (
        session.query(PABoundary.gid)
        .filter(
            ST_Intersects(
                ST_SetSRID(ST_MakePoint(longitude, latitude), 4326), PABoundary.geom
            )
        )
        .all()
    )
    return valid_point


# --------------------------------------------------------------------------------------------------------------
def point_in_pittsburgh_neighborhood_sql(latitude: float, longitude: float):
    """Get the Pittsburgh neighborhood the point is in"""
    session = Session()
    neighborhood = text(
        f"""
        SELECT hood as "neighborhood_name"
        FROM pit_neighborhoods
        WHERE 
            ST_Intersects(
                ST_SetSRID(ST_MakePoint({longitude}, {latitude}), 4326),
                geom
            );
        """
    )
    neighborhood = session.execute(neighborhood).one_or_none()
    if neighborhood:
        neighborhood = neighborhood[0]
    return neighborhood


# --------------------------------------------------------------------------------------------------------------
# Bonus - Not in presentation
# --------------------------------------------------------------------------------------------------------------
def point_distance_from_geom_sql(latitude: float, longitude: float, geom: Geometry):
    """Calculate distance from point to provided geometry using raw SQL"""
    session = Session()
    sql_text = text(
        f"""
        SELECT ST_Distance(
            ST_SetSRID(ST_MakePoint({longitude}, {latitude}), 4326),
            ST_GeomFromText('{geom}')
        );
        """
    )
    distance = session.execute(sql_text).one()[0]
    return distance


def point_distance_from_geom(
    latitude: float, longitude: float, geom: Annotated[str, Geometry]
):
    """Calculate distance from point to provided geometry using SQLAlchemy/GeoAlchemy2"""
    session = Session()
    distance = session.query(
        ST_Distance(
            ST_SetSRID(ST_MakePoint(longitude, latitude), 4326),
            cast(ST_GeomFromText(geom), Geography(srid=4326)),
        )
    ).one()[0]
    return distance


# --------------------------------------------------------------------------------------------------------------
def geom_is_valid(geom: str):
    """Check if provided geometry is valid"""
    session = Session()
    try:
        valid_geom = session.query(ST_IsValid(ST_GeomFromText(geom))).one()
    except sqlalchemy.exc.InternalError:
        valid_geom = False
    return valid_geom
