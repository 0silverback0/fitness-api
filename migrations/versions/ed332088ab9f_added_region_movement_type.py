"""added region, movement_type

Revision ID: ed332088ab9f
Revises: 07a65dc7b38b
Create Date: 2023-02-25 14:13:29.544710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed332088ab9f'
down_revision = '07a65dc7b38b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercises', schema=None) as batch_op:
        batch_op.add_column(sa.Column('region', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('movement_type', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercises', schema=None) as batch_op:
        batch_op.drop_column('movement_type')
        batch_op.drop_column('region')

    # ### end Alembic commands ###
