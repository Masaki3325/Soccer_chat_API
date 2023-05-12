from fastapi import FastAPI
from http.client import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings
from .models import User

engine = create_engine(settings.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI(title="FastAPI, Docker, and Traefik")

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    # データベースから該当するユーザーを取得する
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()

    # 該当するユーザーが存在しない場合は404エラーを返す
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # ユーザーの情報を返す
    return user