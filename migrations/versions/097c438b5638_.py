"""empty message

Revision ID: 097c438b5638
Revises: 8b2331ffa3b0
Create Date: 2023-05-15 14:51:06.253500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '097c438b5638'
down_revision = '8b2331ffa3b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('people_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'people', ['people_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('people_id')

    # ### end Alembic commands ###
