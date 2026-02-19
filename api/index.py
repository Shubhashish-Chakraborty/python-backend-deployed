from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
  return {"message": "This python backend is Up & Running!!"}
