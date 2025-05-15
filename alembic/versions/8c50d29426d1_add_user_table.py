"""add user table

Revision ID: 8c50d29426d1
Revises: 2315eedbd3c8
Create Date: 2025-05-14 21:54:35.059711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c50d29426d1'
down_revision = '2315eedbd3c8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass




def downgrade():
    op.drop_table('users')
    pass
