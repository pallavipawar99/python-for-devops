from fastapi import FastAPI # Importing FastAPI Class
from routers import system_check,log_check

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utitlities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version="1.1.0",
    doc_url="/docs",
    redoc_url="/redoc"
)

app.include_router(system_check.router, prefix="/health")
app.include_router(log_check.router, prefix="/logs")