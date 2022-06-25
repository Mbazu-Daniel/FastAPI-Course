"""add user table

Revision ID: 92e6d431d64a
Revises: 3fdeb7deb08c
Create Date: 2022-06-25 00:22:12.018839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "92e6d431d64a"
down_revision = "3fdeb7deb08c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(),  nullable=False),
        sa.Column("email",sa.String(), nullable=False),
        sa.Column("password",sa.String(), nullable=False),
        sa.Column("created_at",
            sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
