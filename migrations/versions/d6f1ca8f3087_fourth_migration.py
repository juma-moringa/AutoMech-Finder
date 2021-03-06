"""fourth Migration

Revision ID: d6f1ca8f3087
Revises: e446430d722f
Create Date: 2021-06-23 20:54:00.970827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6f1ca8f3087'
down_revision = 'e446430d722f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mechanics', 'specialization',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mechanics', 'specialization',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
