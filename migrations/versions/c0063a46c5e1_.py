"""empty message

Revision ID: c0063a46c5e1
Revises: 2d08aaa51db5
Create Date: 2022-10-22 16:58:00.391549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0063a46c5e1'
down_revision = '2d08aaa51db5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_answer', sa.Column('quiz_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_answer', 'quiz_id')
    # ### end Alembic commands ###
