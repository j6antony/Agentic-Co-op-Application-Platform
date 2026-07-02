from fastapi import FastAPI

app = FastAPI(title="Co-op Agent Platform API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
