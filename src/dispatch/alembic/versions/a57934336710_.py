"""Adds task ticket association table

Revision ID: a57934336710
Revises: cfd62f719c84
Create Date: 2020-05-27 14:30:41.249023

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "a57934336710"
down_revision = "cfd62f719c84"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "task_tickets",
        sa.Column("ticket_id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["task_id"], ["task.id"],),
        sa.ForeignKeyConstraint(["ticket_id"], ["ticket.id"],),
        sa.PrimaryKeyConstraint("ticket_id", "task_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task_tickets")
    # ### end Alembic commands ###
