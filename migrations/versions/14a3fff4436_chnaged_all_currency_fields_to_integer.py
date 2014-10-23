"""Chnaged all currency fields to integer

Revision ID: 14a3fff4436
Revises: 2084f746818
Create Date: 2014-10-23 13:02:02.680288

"""

# revision identifiers, used by Alembic.
revision = '14a3fff4436'
down_revision = '2084f746818'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('skus', 'crrnt_gm_forecast',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('skus', 'current_price',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('skus', 'opt_price',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('skus', 'optml_gm_forecast',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('skus', 'org_price',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('skus', 'unit_cost',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('stores', 'lat',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=6),
               existing_nullable=True)
    op.alter_column('stores', 'lng',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=6),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stores', 'lng',
               existing_type=sa.Float(precision=6),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('stores', 'lat',
               existing_type=sa.Float(precision=6),
               type_=sa.REAL(),
               existing_nullable=True)
    op.alter_column('skus', 'unit_cost',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('skus', 'org_price',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    op.alter_column('skus', 'optml_gm_forecast',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('skus', 'opt_price',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('skus', 'current_price',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    op.alter_column('skus', 'crrnt_gm_forecast',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    ### end Alembic commands ###
