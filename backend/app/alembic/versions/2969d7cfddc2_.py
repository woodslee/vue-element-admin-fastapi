"""

Revision ID: 2969d7cfddc2
Revises: 6d2f0aac7bb2
Create Date: 2020-06-28 16:44:07.582027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2969d7cfddc2'
down_revision = '6d2f0aac7bb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_group_menu_id'), table_name='group_menu')
    op.drop_table('group_menu')
    # ### end Alembic commands ###
