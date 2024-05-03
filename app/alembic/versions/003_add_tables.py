"""Add tables

Revision ID: 406968e80ebb
Revises: 3f8a294dc35e
Create Date: 2024-04-13 23:58:07.090317

"""

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '406968e80ebb'
down_revision = '3f8a294dc35e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(open('alembic/pa_boundary.sql').read())
    op.execute(open('alembic/pit_neighborhoods.sql').read())


def downgrade() -> None:
    op.drop_index('pa_boundary_geom_idx')
    op.drop_table('pa_boundary')
    op.drop_index('pit_neighborhoods_geom_idx')
    op.drop_table('pit_neighborhoods')
