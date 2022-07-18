import uvicorn
from fastapi import FastAPI, Request, Form, UploadFile,File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import models
from databases import Database
from database import SessionLocal

database = Database("sqlite:///whatsapp.db")
db = SessionLocal()


# Start fastapi application
app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

# Render Home page
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post("/sendmsg", response_class=HTMLResponse)
async def submit(request: Request,csv: UploadFile=File(...),message:str=Form(...)):
    csv=pd.read_csv(csv.file, sep=',')
       
    msg = models.Message(
        message=message,
        status=1
    )

    db.add(msg)
    db.commit()
    db.flush()
    id=msg.id
    numbers=csv.Number

    print(numbers)
    for i in numbers:
        number = models.Numbers(
            message_id=id,
            number=i,
            status=1
        )
        db.add(number)
        db.commit()
        db.flush()
    
    
    return templates.TemplateResponse('thanks.html', {'request': request})





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)