from datetime import datetime, UTC
from fastapi import FastAPI, HTTPException
from app.costs import get_monthly_summary, get_cost_breakdown, get_cost_history

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

@app.get("/costs/summary")
def cost_summary():
    try:
        return get_monthly_summary()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@app.get("/costs/breakdown")
def cost_breakdown():
    try:
        return get_cost_breakdown()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


@app.get("/costs/history")
def cost_history():
    try:
        return get_cost_history()
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
