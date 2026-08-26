from datetime import datetime, UTC
from fastapi import FastAPI, HTTPException
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from prometheus_fastapi_instrumentator import Instrumentator
from app.costs import get_monthly_summary, get_cost_breakdown, get_cost_history

#OpenTelemetry Config
resource = Resource.create({SERVICE_NAME: "aws-cost-tracker"})
provider = TracerProvider(resource=resource)
otlp_exporter = OTLPSpanExporter(endpoint= "http://jaeger:4317", insecure=True)
provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
trace.set_tracer_provider(provider)

app = FastAPI(
    title="AWS Cost Tracker",
    description="Real-Time AWS Infrastructure cost monitoring dashboard",
    version="0.0.1"
)

Instrumentator().instrument(app).expose(app)
FastAPIInstrumentor.instrument_app(app)

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
