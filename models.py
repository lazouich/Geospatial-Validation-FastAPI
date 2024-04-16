from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String

from database import Base


class PABoundary(Base):
    __tablename__ = "pa_boundary"

    gid = Column(Integer, primary_key=True)
    statefp = Column(String)
    statens = Column(String)
    affgeoid = Column(String)
    geoid = Column(String)
    stusps = Column(String)
    name = Column(String)
    lsad = Column(String)
    aland = Column(Integer)
    awater = Column(Integer)
    geom = Column(Geometry("MULTIPOLYGON"))
