"""empty message

Revision ID: 981e52e5bc61
Revises: 804dea8eccd6
Create Date: 2023-07-30 00:40:04.187598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '981e52e5bc61'
down_revision = '804dea8eccd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entry', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('telefone', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('endereco', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('cpf', sa.String(length=120), nullable=False))
        batch_op.drop_index('ix_entry_description')
        batch_op.drop_index('ix_entry_title')
        batch_op.create_index(batch_op.f('ix_entry_cpf'), ['cpf'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_endereco'), ['endereco'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_nome'), ['nome'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_telefone'), ['telefone'], unique=False)
        batch_op.drop_column('description')
        batch_op.drop_column('title')
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entry', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('title', sa.VARCHAR(length=64), nullable=False))
        batch_op.add_column(sa.Column('description', sa.VARCHAR(length=120), nullable=False))
        batch_op.drop_index(batch_op.f('ix_entry_telefone'))
        batch_op.drop_index(batch_op.f('ix_entry_nome'))
        batch_op.drop_index(batch_op.f('ix_entry_endereco'))
        batch_op.drop_index(batch_op.f('ix_entry_cpf'))
        batch_op.create_index('ix_entry_title', ['title'], unique=False)
        batch_op.create_index('ix_entry_description', ['description'], unique=False)
        batch_op.drop_column('cpf')
        batch_op.drop_column('endereco')
        batch_op.drop_column('telefone')
        batch_op.drop_column('nome')

    # ### end Alembic commands ###