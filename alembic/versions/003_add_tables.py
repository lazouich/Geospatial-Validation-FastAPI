"""Add tables

Revision ID: 406968e80ebb
Revises: 3f8a294dc35e
Create Date: 2024-04-13 23:58:07.090317

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision: str = '406968e80ebb'
down_revision: Union[str, None] = '3f8a294dc35e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'places',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('geom', Geometry('POLYGON', srid=4326))
    )
    op.execute(open('alembic/pa_boundary.sql').read())


def downgrade() -> None:
    op.drop_table('places')
    op.drop_index('pa_boundary_geom_idx')
    op.drop_table('pa_boundary')

