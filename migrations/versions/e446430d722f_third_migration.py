"""Third Migration

Revision ID: e446430d722f
Revises: 7e39effd372d
Create Date: 2021-06-23 20:29:56.489665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e446430d722f'
down_revision = '7e39effd372d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mechanics', sa.Column('location', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mechanics', 'location')
    # ### end Alembic commands ###