# src/firstapp/dependencies.py

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from collections.abc import AsyncGenerator
from fastapi import Depends
from src.database import AsyncSessionLocal

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

Session_dep = Annotated[AsyncSession, Depends(get_session)]