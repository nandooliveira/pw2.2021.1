"""empty message

Revision ID: bfaeadaa3445
Revises: f18a1acf1c2c
Create Date: 2021-10-25 21:05:11.739519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfaeadaa3445'
down_revision = 'f18a1acf1c2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('turmas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matriculas',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('turma_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['turma_id'], ['turmas.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('usuario_id', 'turma_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matriculas')
    op.drop_table('turmas')
    # ### end Alembic commands ###