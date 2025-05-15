"""add content column to posts table

Revision ID: 2315eedbd3c8
Revises: d5d4440e4fb6
Create Date: 2025-05-14 21:49:41.006546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2315eedbd3c8'
down_revision = 'd5d4440e4fb6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
