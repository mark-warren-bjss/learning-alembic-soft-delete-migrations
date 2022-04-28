"""replace deleted with deleted_at

Revision ID: bba1676d2e24
Revises: 2d4d48e39196
Create Date: 2022-04-28 10:37:27.183383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bba1676d2e24'
down_revision = '2d4d48e39196'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appeal', sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True))
    op.drop_column('appeal', 'deleted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appeal', sa.Column('deleted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('appeal', 'deleted_at')
    # ### end Alembic commands ###
