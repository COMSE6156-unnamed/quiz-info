"""empty message

Revision ID: b83e013c5ec6
Revises: 9176ddc36af9
Create Date: 2022-11-02 18:43:30.462532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b83e013c5ec6'
down_revision = '9176ddc36af9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('img_url', sa.String(length=256), nullable=True),
    sa.Column('right_answer_id', sa.Integer(), nullable=True),
    sa.Column('other_choice_id1', sa.Integer(), nullable=True),
    sa.Column('other_choice_id2', sa.Integer(), nullable=True),
    sa.Column('other_choice_id3', sa.Integer(), nullable=True),
    sa.Column('difficulty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('question_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###
