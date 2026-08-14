import itertools
from typing import TypedDict

from fastapi import FastAPI, status
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(
    title="Jobflow Backend",
    description="Backend service for aggregating and tracking job opportunities.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the current health of the API Service"""
    return {"status": "ok"}


class JobModel(BaseModel):
    title: str = Field(min_length=2, max_length=120)
    company: str = Field(min_length=2, max_length=120)
    url: HttpUrl
    location: str | None = None
    source: str = Field(min_length=2, max_length=50)


class JobReturnModel(TypedDict):
    id: int
    title: str
    company: str
    url: HttpUrl
    location: str | None
    source: str


# id = 0
@app.post("/job", status_code=status.HTTP_201_CREATED)
def create_job(job: JobModel) -> JobReturnModel:
    
    return {
        "id": 1,
        "title": job.title,
        "company": job.company,
        "url": job.url,
        "location": job.location,
        "source": job.source,
    }
