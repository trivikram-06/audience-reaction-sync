from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------------------------
# FastAPI App
# -------------------------------------------------

app = FastAPI(
    title="Audience Reaction API",
    version="1.0"
)

# -------------------------------------------------
# Enable CORS
# -------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Paths
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "outputs" / "logs"

# -------------------------------------------------
# Load Latest CSV
# -------------------------------------------------

def load_latest():

    files = sorted(
        LOG_DIR.glob("*.csv"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    if len(files) == 0:
        return None

    return pd.read_csv(files[0])

# -------------------------------------------------
# Home
# -------------------------------------------------

@app.get("/")
def home():

    return {
        "project": "Audience Reaction Sync",
        "status": "Running"
    }

# -------------------------------------------------
# Health Check
# -------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

# -------------------------------------------------
# Latest Audience Data
# -------------------------------------------------

@app.get("/latest")
def latest():

    df = load_latest()

    if df is None:
        return {"error": "No data"}

    latest = df.groupby("person_id").tail(1)

    return latest.to_dict(orient="records")

# -------------------------------------------------
# Analytics
# -------------------------------------------------

@app.get("/analytics")
def analytics():

    df = load_latest()

    if df is None:
        return {"error": "No data"}

    return {
        "people": int(df["person_id"].nunique()),
        "avg_attention": round(df["attention"].mean(), 2),
        "avg_engagement": round(df["engagement"].mean(), 2),
        "max_engagement": round(df["engagement"].max(), 2),
        "min_engagement": round(df["engagement"].min(), 2)
    }

# -------------------------------------------------
# Full History
# -------------------------------------------------

@app.get("/history")
def history():

    df = load_latest()

    if df is None:
        return {"error": "No data"}

    return df.to_dict(orient="records")