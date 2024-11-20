from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os, uvicorn

app = FastAPI()

IMG_DIRECTORY = "./storage"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods = ["GET","POST"],
    allow_headers = ["*"]
)

@app.get("/{img_name}")
def get_img(img_name:str):
    img_path = os.path.join(IMG_DIRECTORY, img_name)
    if os.path.exists(img_path):
        return FileResponse(img_path)  # 이미지 파일을 응답으로 반환
    else:
        return {"error": "Image not found"}  # 이미지가 없으면 에러 메시지 반환
    
@app.post("/upload")
async def upload_img(file: UploadFile = File(...)):
    img_path = os.path.join(IMG_DIRECTORY, file.filename)
    
    # 파일을 저장
    with open(img_path, "wb") as buffer:
        buffer.write(await file.read())
    
    return {"filename": file.filename, "message": "Image uploaded successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)