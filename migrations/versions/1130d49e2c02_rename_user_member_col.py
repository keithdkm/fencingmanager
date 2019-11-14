"""rename user.member col

Revision ID: 1130d49e2c02
Revises: ec2a189f0744
Create Date: 2019-10-04 00:09:23.042299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1130d49e2c02'
down_revision = 'ec2a189f0744'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    table_name = 'users'
    with op.batch_alter_table(table_name) as batch:
    
        batch.add_column(sa.Column('member_id', sa.Integer(), nullable=True))
        batch.drop_constraint('users', type_='foreignkey')
        batch.create_foreign_key('users', 'members', ['member_id'], ['id_'])
        batch.drop_column('member')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('member', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users', 'users', 'members', ['member'], ['id_'])
    op.drop_column('users', 'member_id')
    # ### end Alembic commands ###