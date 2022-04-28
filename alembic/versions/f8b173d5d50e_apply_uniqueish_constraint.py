"""Apply uniqueish constraint

Revision ID: f8b173d5d50e
Revises: bba1676d2e24
Create Date: 2022-04-28 11:00:34.558618

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f8b173d5d50e'
down_revision = 'bba1676d2e24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_appeal_name_deleted', 'appeal', ['name'], unique=True,
                    postgresql_where='deleted_at IS NOT NULL')
    op.create_index('idx_appeal_name_notdeleted', 'appeal', ['name', 'deleted_at'],
                    unique=True, postgresql_where='deleted_at IS NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_appeal_name_notdeleted', table_name='appeal',
                  postgresql_where='deleted_at IS NULL')
    op.drop_index('idx_appeal_name_deleted', table_name='appeal',
                  postgresql_where='deleted_at IS NOT NULL')
    # ### end Alembic commands ###
