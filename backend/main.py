from fastapi import FastAPI

from backend.services.database_service import DatabaseService

app = FastAPI(
    title="EcoPulse AI",
    description="AI-Powered Industrial Energy Optimization Platform",
    version="1.0.0"
)

database = DatabaseService()


@app.get("/")
def home():

    return {
        "project": "EcoPulse AI",
        "status": "Backend Running"
    }


@app.get("/health")
def health():

    return {
        "server": "Healthy"
    }


@app.get("/logs")
def logs():

    return database.get_all_logs()


@app.get("/machines")
def machines():

    return database.get_latest_logs()