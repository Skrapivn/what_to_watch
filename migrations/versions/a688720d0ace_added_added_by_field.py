"""added added_by field

Revision ID: a688720d0ace
Revises: 
Create Date: 2022-08-24 10:46:34.671444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a688720d0ace'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('opinion', sa.Column('added_by', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('opinion', 'added_by')
    # ### end Alembic commands ###
