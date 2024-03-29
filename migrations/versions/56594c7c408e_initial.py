"""initial

Revision ID: 56594c7c408e
Revises: 
Create Date: 2024-02-29 23:06:40.397577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56594c7c408e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
