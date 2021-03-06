"""added a subscriptions model

Revision ID: 61dd1efb28df
Revises: cc62faf7a680
Create Date: 2021-05-02 15:35:10.887453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61dd1efb28df'
down_revision = 'cc62faf7a680'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscriptions_email'), 'subscriptions', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscriptions_email'), table_name='subscriptions')
    op.drop_table('subscriptions')
    # ### end Alembic commands ###
