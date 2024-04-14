from geoalchemy2.functions import ST_MakePoint, ST_Intersects, ST_SetSRID
from sqlalchemy.orm import sessionmaker

from database import engine
from models import PA_Boundary

Session = sessionmaker(bind=engine)


def point_intersects_pennsylvania(latitude: float, longitude: float):
    session = Session()
    valid_point = session.query(PA_Boundary.gid).filter(
        ST_Intersects(
            ST_SetSRID(ST_MakePoint(longitude, latitude), 4326),
            PA_Boundary.geom
        )
    ).all()
    return valid_point
