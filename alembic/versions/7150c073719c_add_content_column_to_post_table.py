"""add content column to post table

Revision ID: 7150c073719c
Revises: ef47912cca91
Create Date: 2023-09-14 09:11:38.807394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7150c073719c'
down_revision: Union[str, None] = 'ef47912cca91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
