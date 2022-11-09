"""empty message

Revision ID: 7ab2f5757a64
Revises: b83e013c5ec6
Create Date: 2022-11-08 15:17:42.745975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab2f5757a64'
down_revision = 'b83e013c5ec6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('img_url', sa.String(length=256), nullable=True),
    sa.Column('content', sa.String(length=1024), nullable=True),
    sa.Column('answer', sa.String(length=256), nullable=True),
    sa.Column('difficulty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('question_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###