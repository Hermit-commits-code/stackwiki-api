from fastapi import FastAPI

app = FastAPI(
    title="StackWiki API",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "StackWiki API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
