"""empty message

Revision ID: a708d2f44545
Revises: 
Create Date: 2022-02-14 20:21:11.637464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a708d2f44545'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('character_homeworld', sa.String(length=250), nullable=False),
    sa.Column('character_name', sa.String(length=250), nullable=True),
    sa.Column('character_skill', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('character_id')
    )
    op.create_table('planet',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('planet_population', sa.Integer(), nullable=False),
    sa.Column('planet_diameter', sa.Integer(), nullable=False),
    sa.Column('planet_climate', sa.String(length=250), nullable=False),
    sa.Column('planet_name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('planet_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=12), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favorite_character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.character_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.planet_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_planet')
    op.drop_table('favorite_character')
    op.drop_table('user')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
