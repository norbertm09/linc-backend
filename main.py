from fastapi import FastAPI
from routers import auth
from routers import wallet
from routers import transfer
from routers import crypto
from routers import savings
from routers import insurance
from routers import scoring
from routers import admin
from routers import compliance

app = FastAPI(title="Linc Full API", version="1.7+")

app.include_router(auth.router)
app.include_router(wallet.router)
app.include_router(transfer.router)
app.include_router(crypto.router)
app.include_router(savings.router)
app.include_router(insurance.router)
app.include_router(scoring.router)
app.include_router(admin.router)
app.include_router(compliance.router)

@app.get("/")
def root():
    return {"message": "Linc Full Backend API v1.7+"}