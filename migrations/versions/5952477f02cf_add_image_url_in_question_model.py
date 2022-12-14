"""add image_url in question model

Revision ID: 5952477f02cf
Revises: 7caa725c88db
Create Date: 2022-11-14 14:05:47.313170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5952477f02cf'
down_revision = '7caa725c88db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('image_url', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'image_url')
    # ### end Alembic commands ###
