"""Add field dectivate 

Revision ID: 75db16a7f420
Revises: 99c93bba3d35
Create Date: 2024-06-01 23:49:34.303060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75db16a7f420'
down_revision: Union[str, None] = '99c93bba3d35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dectivate', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'dectivate')
    # ### end Alembic commands ###
