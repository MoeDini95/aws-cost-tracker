from fastapi import FastAPI
from datetime import datetime, UTC

app = FastAPI(
    title="AWS Cost Tracker",
    description="Real-Time AWS Infrastructure cost monitoring dashboard",
    version="0.0.1"
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "version": "0.0.1",
        "timestamp": datetime.now(UTC).isoformat()
    }

@app.get("/version")
def get_version():
    return {
        "version": "0.0.1"
    }