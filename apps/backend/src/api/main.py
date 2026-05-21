from fastapi import FastAPI

app = FastAPI()

# This is 
origin = ["http://localhost:8080"]

@app.get("/")
async def root():
    return {"message": "Hello World"}

