from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 요청을 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용 (GET, POST 등)
    allow_headers=["*"],  # 모든 헤더 허용
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/spacex/launches")
async def get_launches():
    url = "https://api.spacexdata.com/v4/launches"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    launches = response.json()  # 여러 발사 데이터

    # 각 발사 데이터에 이미지 링크 추가
    for launch in launches:
        if 'links' in launch and 'patch' in launch['links']:
            launch['image_small'] = launch['links']['patch'].get('small', None)
            launch['image_large'] = launch['links']['patch'].get('large', None)
        else:
            launch['image_small'] = None
            launch['image_large'] = None

    return launches  # 이미지가 포함된 발사 데이터 반환

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)