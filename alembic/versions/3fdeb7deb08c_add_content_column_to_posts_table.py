"""add content column to posts table

Revision ID: 3fdeb7deb08c
Revises: a489c76b5ff3
Create Date: 2022-06-25 00:16:13.379917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3fdeb7deb08c"
down_revision = "a489c76b5ff3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
