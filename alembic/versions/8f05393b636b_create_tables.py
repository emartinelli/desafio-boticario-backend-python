"""Create tables

Revision ID: 8f05393b636b
Revises: 
Create Date: 2022-08-11 22:27:30.560514

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "8f05393b636b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "revendedores",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("cpf", sa.String(length=11), nullable=False),
        sa.Column("email", sa.String(length=254), nullable=False),
        sa.Column("nome_completo", sa.String(length=255), nullable=False),
        sa.Column("senha_com_hash", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_revendedores_cpf"), "revendedores", ["cpf"], unique=True)
    op.create_index(
        op.f("ix_revendedores_email"), "revendedores", ["email"], unique=True
    )
    op.create_index(op.f("ix_revendedores_id"), "revendedores", ["id"], unique=False)
    op.create_table(
        "compras",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("codigo", sa.String(length=50), nullable=False),
        sa.Column("valor", sa.Numeric(), nullable=False),
        sa.Column("data", sa.DateTime(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("em_validacao", "aprovado", name="statusenum"),
            nullable=False,
        ),
        sa.Column("porcentagem_de_cashback", sa.Numeric(), nullable=False),
        sa.Column("revendedor_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["revendedor_id"],
            ["revendedores.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_compras_codigo"), "compras", ["codigo"], unique=True)
    op.create_index(op.f("ix_compras_id"), "compras", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_compras_id"), table_name="compras")
    op.drop_index(op.f("ix_compras_codigo"), table_name="compras")
    op.drop_table("compras")
    op.drop_index(op.f("ix_revendedores_id"), table_name="revendedores")
    op.drop_index(op.f("ix_revendedores_email"), table_name="revendedores")
    op.drop_index(op.f("ix_revendedores_cpf"), table_name="revendedores")
    op.drop_table("revendedores")
    # ### end Alembic commands ###
