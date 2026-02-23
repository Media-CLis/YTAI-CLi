from fastapi import FastAPI
import sqlite3
import json

app = FastAPI()
DB_PATH = "../data/ytai.db"

def query_db(sql):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

@app.get("/videos")
def get_videos():
    rows = query_db("SELECT * FROM videos")
    return {"videos":rows}

@app.get("/clips")
def get_clips():
    rows = query_db("SELECT * FROM clips")
    return {"clips":rows}
