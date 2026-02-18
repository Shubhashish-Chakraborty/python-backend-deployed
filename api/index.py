from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
  return {
    "message": "This python Backend is up & Running!"
  }

handler = app