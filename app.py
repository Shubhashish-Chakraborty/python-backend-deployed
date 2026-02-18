from fastapi import FastAPI
app = FastAPI()
 
@app.get("/")
def root():
  return {"message": "This python backend Up & Running!!"}