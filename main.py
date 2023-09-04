from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return "Hello Fast API!"

if __name__ == "__main__":
    uvicorn.run(app)
    # uvicorn.run("main:app", reload=True)