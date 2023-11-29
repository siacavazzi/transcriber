"""init

Revision ID: f5f23ee08e3c
Revises: 
Create Date: 2023-11-29 15:26:30.581939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5f23ee08e3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('fname', sa.String(), nullable=True),
    sa.Column('lname', sa.String(), nullable=True),
    sa.Column('pass_hash', sa.String(), nullable=True),
    sa.Column('creation_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('configs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prompt', sa.String(), nullable=True),
    sa.Column('generate_img', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_configs_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transcripts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_started', sa.Date(), nullable=True),
    sa.Column('time_ended', sa.Date(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_transcripts_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_ms', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('transcript_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transcript_id'], ['transcripts.id'], name=op.f('fk_lines_transcript_id_transcripts')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lines')
    op.drop_table('transcripts')
    op.drop_table('configs')
    op.drop_table('users')
    # ### end Alembic commands ###
