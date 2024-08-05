from typing import Union, List, Optional
import os
import sys
sys.path.append("pyScripts")
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel

from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pyScripts.main import main

import subprocess

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

templates = Jinja2Templates(directory="templates")

@app.get("/crafting/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="crafting.html", context={"id": id}
    )

@app.get("/")
def read_root():
 with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/styles.css", include_in_schema=False)
async def favicon():
    return FileResponse("static/styles.css")

@app.get("/templates/styles.css", include_in_schema=False)
async def favicon():
    return FileResponse("templates/styles.css")

@app.get("/templates/scripts.js", include_in_schema=False)
async def favicon():
    return FileResponse("templates/scripts.js")



@app.get("/dropdown.js", include_in_schema=False)
async def favicon():
    return FileResponse("static/dropdown.js")


@app.get("/drawing.svg", include_in_schema=False)
async def favicon():
    return FileResponse("static/drawing.svg")

@app.post("/submit")
def submit_form(topic: List[str] = Form(...), words: Optional[List[str]] = Form(None)):
    words = ['도시', '이름', '저', '나', '남자', '여자', '이', '그', '저', '것', '이것', '그것', '저것', '의자', '탁자', '선생님', '침대', '집', '차', '사람', '책', '컴퓨터', '나무', '소파', '중국', '일본', '문', '의사', '학생', '이다', '네', '아니', '나라', '가방', '창문', '잡지', '방', '냉장고', '개', '강아지', '고양이', '쥐', '펜', '전화기', '커피', '식당', '건물', '텔레비전', '미국', '캐나다', '호텔', '학교', '은행', '안', '위', '밑', '옆', '뒤', '앞', '여기', '있다', '있다', '음식', '케이크', '공항', '병원', '공원', '한국어', '머리', '귀', '팔', '눈', '입', '배', '버스', '배', '우리', '먹다', '가다','만나다', '닫다', '열다', '원하다', '만들다', '하다', '말하다', '이해하다', '좋아하다', '크다','작다', '새롭다', '낡다', '비싸다', '싸다', '아름답다', '뚱뚱하다', '길다', '좋다']
    print(topic)
    os.chdir("pyScripts")
    main(topic, words)
    os.chdir("..")
    #subprocess.run(["python", "main.py"], cwd="pyScripts")
    return FileResponse("pyScripts/output.pdf", media_type="application/pdf")
