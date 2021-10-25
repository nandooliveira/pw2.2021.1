"""empty message

Revision ID: 536abfc00f50
Revises: 
Create Date: 2021-10-18 21:24:37.575241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536abfc00f50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###