"""Create table Todos

Revision ID: 9a472ea8b31c
Revises: 557dbac98f55
Create Date: 2024-01-06 15:11:23.636337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a472ea8b31c'
down_revision = '557dbac98f55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('todo', sa.String(length=140), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_todos_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_todos_updated_at'), ['updated_at'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_todos_updated_at'))
        batch_op.drop_index(batch_op.f('ix_todos_created_at'))

    op.drop_table('todos')
    # ### end Alembic commands ###
