# src/firstapp/router.py

from fastapi import APIRouter
import src.firstapp.crud as crud
from fastapi.responses import HTMLResponse
from src.firstapp.dependencies import Session_dep

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def get_main_page():
    return """
    <html>
        <head>
            <title>Main</title>
        </head>
        <body>
            <h1> Hello World!! </h1>
            <p> For create a note create a url address with query params: value(int) and description(string). Path: /add. Example: http://host/add?value=1&description="Nice work"</p>
            <p> For see all notes with the same value go to http://host/get&value=your value </p>
        </body>
    </html>
    """

@router.get("/get", response_class=HTMLResponse)
async def get_notes(value: int, db: Session_dep):
    notes = await crud.get_note(value=value, db=db)
    if type(notes) == list:
        all_notes_str = ''.join(notes)
        return f"""
        <html>
            <head>
                <title>SHOW!!!</title>
            </head>
            <body>
                <h1> Hello World!! </h1>
                <p> Thats all: {all_notes_str} </p>
            </body>
        </html>
        """
    else:
        return """
        <html>
            <head>
                <title>ERROR</title>
            </head>
        <body>
            <h1> NOT FOUND </h1>
        </body>
        </html>
        """

@router.post("/add")
async def add_note(description: str,value: int, db: Session_dep):
    is_allow = await crud.add_note(db=db, value=value, des=description)
    return {"added" : is_allow}