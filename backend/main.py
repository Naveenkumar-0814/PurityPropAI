from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.routes import router
# from app.auth_routes import router as auth_router
from app.config import settings

app = FastAPI(
    title="Tamil Nadu Real Estate AI Assistant",
    version="1.0.0",
)

# ✅ CORS CONFIG (HARDCODED FOR STABILITY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://puritypropai.onrender.com",
        "https://purityprop.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ❌ Explicit OPTIONS handler removed to let CORSMiddleware handle preflights

# ✅ Routers
# auth_routes.py already defines /auth/*
# app.include_router(auth_router, prefix="/api")

# other routes
# app.include_router(router, prefix="/api")

# TEMPORARY: Minimal Login Endpoint to TEST CORS
@app.post("/api/auth/login")
async def dummy_login():
    return {"access_token": "fake_token", "token_type": "bearer", "user": {"email": "test@example.com", "name": "Test User"}}

@app.options("/api/auth/login")
async def dummy_options():
    return {} # Force return for testing if middleware fails

# ✅ Health check
@app.get("/")
def root():
    return {
        "message": "Tamil Nadu Real Estate AI Assistant API (Safe Mode)",
        "status": "active",
        "docs": "/docs",
    }
