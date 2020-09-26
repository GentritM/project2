"""empty message

Revision ID: 92f25a9e3b07
Revises: 330d36d62186
Create Date: 2020-09-24 11:34:51.305579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92f25a9e3b07'
down_revision = '330d36d62186'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('join_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'join_date')
    # ### end Alembic commands ###
