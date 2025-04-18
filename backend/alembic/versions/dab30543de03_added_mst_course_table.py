"""added mst_course table

Revision ID: dab30543de03
Revises: 
Create Date: 2025-04-16 11:08:26.349887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dab30543de03'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mst_courses',
    sa.Column('course_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_code', sa.String(length=15), nullable=False),
    sa.Column('course_name', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_index(op.f('ix_mst_courses_course_code'), 'mst_courses', ['course_code'], unique=False)
    op.create_index(op.f('ix_mst_courses_course_name'), 'mst_courses', ['course_name'], unique=False)
    op.create_table('mst_students',
    sa.Column('stud_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stud_name', sa.String(length=15), nullable=False),
    sa.Column('stud_dob', sa.Date(), nullable=True),
    sa.Column('stud_doj', sa.Date(), nullable=True),
    sa.Column('stud_gender_id', sa.Integer(), nullable=False),
    sa.Column('stud_email', sa.String(length=50), nullable=True),
    sa.Column('stud_phone_no', sa.String(length=15), nullable=True),
    sa.Column('stud_address', sa.String(length=100), nullable=True),
    sa.Column('stud_course_id', sa.BigInteger(), nullable=False),
    sa.Column('isactive', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['stud_course_id'], ['mst_courses.course_id'], ),
    sa.PrimaryKeyConstraint('stud_id')
    )
    op.create_index(op.f('ix_mst_students_stud_name'), 'mst_students', ['stud_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mst_students_stud_name'), table_name='mst_students')
    op.drop_table('mst_students')
    op.drop_index(op.f('ix_mst_courses_course_name'), table_name='mst_courses')
    op.drop_index(op.f('ix_mst_courses_course_code'), table_name='mst_courses')
    op.drop_table('mst_courses')
    # ### end Alembic commands ###
