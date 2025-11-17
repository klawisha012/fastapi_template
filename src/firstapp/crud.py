# src/firstapp/crud.py

from src.firstapp.dependencies import Session_dep
import src.firstapp.models as models
from sqlalchemy.future import select

async def get_note(db: Session_dep, value: int) -> list | bool:
    try:
        result = await db.execute(select(models.MyTestTable).filter(models.MyTestTable.value == value))
        notes = result.scalars().all()
        if not notes:
            return False
        notes_description = [i.description for i in notes]
        return notes_description
    except Exception:
        return False

async def add_note(db: Session_dep, value: int, des: str) -> bool:
    new_note = models.MyTestTable(value=value, description=des)
    db.add(new_note)
    await db.commit()
    return True
