"""empty message

Revision ID: 202b7b3cc9ee
Revises: 3048d6512e92
Create Date: 2022-04-01 17:58:24.438251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202b7b3cc9ee'
down_revision = '3048d6512e92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar_image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar_image')
    # ### end Alembic commands ###