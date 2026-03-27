from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from interviewcoach.api import router as interviewcoach_router

app = FastAPI(title="InterviewCoach API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interviewcoach_router, prefix="/api/interviewcoach")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
