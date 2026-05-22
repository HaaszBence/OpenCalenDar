from fastapi import FastAPI

app = FastAPI()

# This is the frontend URL, adjust it as needed
origin = ["http://localhost:8080"]

@app.get("/")
async def root():
    return {"message": "Hello World"}



