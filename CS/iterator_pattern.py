from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncio
import os
from collections.abc import Iterator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JSONIterator(Iterator):
    def __init__(self, file_name: str):
        script_dir = os.path.dirname(os.path.abspath(__file__))  
        self.file_path = os.path.join(script_dir, file_name)  
        self.data = self.load_json()
        self.index = 0

    def load_json(self):
        if not os.path.exists(self.file_path):  
            raise FileNotFoundError(f"파일을 찾을 수 없습니다: {self.file_path}")
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def __iter__(self) -> "JSONIterator":
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item

@app.get("/stream-json")
async def stream_json():
    iterator = JSONIterator("data.json")

    async def event_generator():
        for item in iterator:
            json_item = json.dumps(item)
            yield f"data: {json_item}\n\n"
            await asyncio.sleep(0.5)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

import uvicorn

if __name__ == "__main__":
    uvicorn.run("a:app", host="127.0.0.1", port=8000, reload=True)