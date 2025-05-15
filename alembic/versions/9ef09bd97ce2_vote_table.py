"""vote-table

Revision ID: 9ef09bd97ce2
Revises: 166a248032a3
Create Date: 2025-05-15 10:49:23.602307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ef09bd97ce2'
down_revision = '166a248032a3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    pass


def downgrade():
    op.drop_table('votes')
    pass
