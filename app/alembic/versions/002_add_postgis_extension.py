"""Add PostGIS Extension

Revision ID: 3f8a294dc35e
Revises: '9fa7befa0394'

"""

from alembic import op

revision: str = '3f8a294dc35e'
down_revision = '9fa7befa0394'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS postgis;')


def downgrade() -> None:
    op.execute('DROP EXTENSION IF EXISTS postgis;')
