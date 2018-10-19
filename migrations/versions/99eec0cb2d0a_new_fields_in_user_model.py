"""new fields in user model

Revision ID: 99eec0cb2d0a
Revises: d204c767d870
Create Date: 2018-10-17 17:55:51.343915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99eec0cb2d0a'
down_revision = 'd204c767d870'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
