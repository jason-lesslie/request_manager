"""empty message

Revision ID: 74fe213b3008
Revises: 
Create Date: 2018-04-02 18:16:16.396876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74fe213b3008'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('request_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('target_date', sa.Date(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('client_request_priority', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request_model')
    op.drop_table('product')
    op.drop_table('client')
    # ### end Alembic commands ###
