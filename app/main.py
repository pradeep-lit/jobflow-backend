from fastapi import FastAPI

app = FastAPI(title='Jobflow Backend', description='Backend service for aggregating and tracking job opportunities.', version='0.1.0')

@app.get('/health')
def health_check() -> dict[str,str]:
    """Return the current health of the API Service"""
    return {'status':'ok'}

