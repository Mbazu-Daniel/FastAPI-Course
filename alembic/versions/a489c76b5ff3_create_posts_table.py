"""create posts table

Revision ID: a489c76b5ff3
Revises: 
Create Date: 2022-06-24 18:35:00.207080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a489c76b5ff3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
