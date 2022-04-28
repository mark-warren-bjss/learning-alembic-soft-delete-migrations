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

TABLES_AFFECTED = ('appeal',)

def upgrade():
    for table_name in TABLES_AFFECTED:
        op.add_column(table_name, sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True))
        op.execute(f"update {table_name} SET deleted_at=updated_at WHERE deleted = TRUE")
        op.drop_column(table_name, 'deleted')


def downgrade():
    for table_name in reversed(TABLES_AFFECTED):
        op.add_column(table_name, sa.Column('deleted', sa.BOOLEAN(), autoincrement=False, nullable=True))
        op.execute(f"update {table_name} SET deleted=TRUE WHERE deleted_at IS NOT NULL")
        op.drop_column(table_name, 'deleted_at')
