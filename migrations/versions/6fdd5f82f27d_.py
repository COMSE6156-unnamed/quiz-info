"""empty message

Revision ID: 6fdd5f82f27d
Revises: f5bab83836a6
Create Date: 2022-11-09 12:07:03.422729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fdd5f82f27d'
down_revision = 'f5bab83836a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('q_type', sa.Integer(), nullable=True),
    sa.Column('c_type', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
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
