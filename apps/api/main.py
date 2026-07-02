from fastapi import FastAPI
# this is a check to prove that the back end is working
# in terminal run: uvicorn main:app --reload --port 8000
# then look up http://localhost:8000/health in browser
# if you see {"status":"ok"} then it is working
"""
app = FastAPI(title="Co-op Agent Platform API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
"""
