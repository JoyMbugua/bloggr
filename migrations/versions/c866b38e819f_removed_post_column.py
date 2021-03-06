"""removed post column

Revision ID: c866b38e819f
Revises: f24dc5028e4f
Create Date: 2021-05-01 12:13:32.276434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c866b38e819f'
down_revision = 'f24dc5028e4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('post', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
