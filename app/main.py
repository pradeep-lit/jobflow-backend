import itertools
from multiprocessing import JoinableQueue

from fastapi import FastAPI, status
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(
    title="Jobflow Backend",
    description="Backend service for aggregating and tracking job opportunities.",
    version="0.1.0",
)
id_counter = itertools.count(1)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the current health of the API Service"""
    return {"status": "ok"}


class JobCreate(BaseModel):
    title: str = Field(min_length=2, max_length=120)
    company: str = Field(min_length=2, max_length=120)
    url: HttpUrl
    location: str | None = None
    source: str = Field(min_length=2, max_length=50)


class JobResponse(BaseModel):
    id: int
    title: str = Field(min_length=2, max_length=120)
    company: str = Field(min_length=2, max_length=120)
    url: HttpUrl
    location: str | None = None
    source: str = Field(min_length=2, max_length=50)

jobs: list[JobResponse] = []
@app.post("/jobs", status_code=status.HTTP_201_CREATED, response_model=JobResponse)
def create_job(job: JobCreate) -> JobResponse:
    job_id = next(id_counter)
    created_job = JobResponse(id=job_id, **job.model_dump(),)
    jobs.append(created_job)
    return created_job
