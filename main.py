from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, books, checkouts, reservations
import uvicorn

app = FastAPI(title="Library Management API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(books.router, prefix="/api/books", tags=["Books"])
app.include_router(checkouts.router, prefix="/api/checkouts", tags=["Checkouts"])
app.include_router(reservations.router, prefix="/api/reservations", tags=["Reservations"])

@app.get("/")
def root():
    return {"message": "Library Management API", "docs": "/docs"}

@app.get("/api/test")
def test():
    return {"test": "working", "routes_loaded": True}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)