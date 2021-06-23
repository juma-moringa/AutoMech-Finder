"""Initial Migration

Revision ID: 085b391596cd
Revises: bee31410d3a4
Create Date: 2021-06-23 12:26:31.171186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '085b391596cd'
down_revision = 'bee31410d3a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mechanics', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    op.drop_column('mechanics', 'pass_secure')
    # ### end Alembic commands ###
