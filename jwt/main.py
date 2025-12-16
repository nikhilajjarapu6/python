import controller
from database import Base, engine
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from exceptions import AppException


app=FastAPI()
# Create DB tables
Base.metadata.create_all(bind=engine)

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.__class__.__name__,
            "message": exc.message
        }
    )

# Include routes
app.include_router(controller.router)
