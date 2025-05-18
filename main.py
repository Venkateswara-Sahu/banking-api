# main.py
from fastapi import FastAPI
from app.routes import banking

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(banking.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
