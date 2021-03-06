"""followers

Revision ID: 168296fc78e4
Revises: 7732d5d6c422
Create Date: 2019-01-27 00:17:51.208172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '168296fc78e4'
down_revision = '7732d5d6c422'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
