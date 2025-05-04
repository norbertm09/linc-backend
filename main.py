from fastapi import FastAPI
from routers import auth  # suppose que /routers/auth.py existe
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS settings (important for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict this in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include auth routes
app.include_router(auth.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"status": "Linc backend is running"}