# main.py
from fastapi import FastAPI
from app.routes import banking

app = FastAPI(
    title="Banking API",
    description="A FastAPI application for banking operations",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Banking API is running"}

@app.get("/")
def root():
    return {"message": "Welcome to Banking API", "health_endpoint": "/health"}

app.include_router(banking.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_level="info"
    )