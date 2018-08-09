"""followers

Revision ID: 98b0a53bc22c
Revises: 938a0c16a3b3
Create Date: 2018-08-09 10:01:49.773659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98b0a53bc22c'
down_revision = '938a0c16a3b3'
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