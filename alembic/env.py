# alembic/env.py

from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from src.database import Base
from src.config import database_settings
from src.firstapp.models import *

# Alembic Config объект
config = context.config

# Подставляем параметры из settings в alembic.ini
section = config.config_ini_section
config.set_section_option(section, "ALEMBIC_DATABASE_URL", str(database_settings.ALEMBIC_DATABASE_URL))
# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata для автогенерации миграций
target_metadata = Base.metadata

# ---------------------------
# Offline режим
# ---------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# ---------------------------
# Online режим (синхронный)
# ---------------------------
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Создаем синхронный движок
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # include_schemas=True,  # если используешь схемы
        )

        with context.begin_transaction():
            context.run_migrations()


# ---------------------------
# Выбор режима
# ---------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
