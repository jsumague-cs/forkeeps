"""initial schema

Revision ID: 98e1d5b5f238
Revises: 
Create Date: 2026-08-21 15:56:22.229211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98e1d5b5f238'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
    )
    op.create_table(
        'couples',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('user1_id', sa.Integer(), nullable=False),
        sa.Column('user2_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user1_id'], ['users.id']),
        sa.ForeignKeyConstraint(['user2_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'date_ideas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('couple_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=150), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('category', sa.String(length=50), nullable=True),
        sa.Column('estimated_budget', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('status', sa.String(length=50), nullable=True),
        sa.Column('scheduled_date', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['couple_id'], ['couples.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'dates',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('couple_id', sa.Integer(), nullable=False),
        sa.Column('dateidea_id', sa.Integer(), nullable=True),
        sa.Column('title', sa.String(length=150), nullable=False),
        sa.Column('scheduled_at', sa.DateTime(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('category', sa.String(length=50), nullable=True),
        sa.Column('status', sa.String(length=50), nullable=True),
        sa.Column('budget', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('location', sa.String(length=150), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['couple_id'], ['couples.id']),
        sa.ForeignKeyConstraint(['dateidea_id'], ['date_ideas.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'memories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=150), nullable=False),
        sa.Column('journal_entry', sa.Text(), nullable=True),
        sa.Column('actual_expense', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column('location', sa.String(length=150), nullable=True),
        sa.Column('rating', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['date_id'], ['dates.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'photos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('memory_id', sa.Integer(), nullable=False),
        sa.Column('photo_url', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['memory_id'], ['memories.id']),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('photos')
    op.drop_table('memories')
    op.drop_table('dates')
    op.drop_table('date_ideas')
    op.drop_table('couples')
    op.drop_table('users')
