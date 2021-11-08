"""empty message

Revision ID: 27483a7261f3
Revises: 536abfc00f50
Create Date: 2021-10-25 19:48:33.260296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27483a7261f3'
down_revision = '536abfc00f50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('usuarios', 'nome',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('usuarios', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('usuarios', 'senha',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'usuarios', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usuarios', type_='unique')
    op.alter_column('usuarios', 'senha',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('usuarios', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('usuarios', 'nome',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
