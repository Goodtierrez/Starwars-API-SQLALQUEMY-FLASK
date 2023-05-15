"""empty message

Revision ID: bcf9ad8f881b
Revises: a466c694cbad
Create Date: 2023-05-15 09:49:00.838993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcf9ad8f881b'
down_revision = 'a466c694cbad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=240), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###