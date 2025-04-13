import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_CHECKPOINTS_DIR = BASE_DIR / "model_checkpoints"

# Default model path
DEFAULT_MODEL_PATH = os.getenv(
    "MODEL_PATH", 
    str(MODEL_CHECKPOINTS_DIR / "amortized_model.pt")
)

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# API configuration
API_PREFIX = "/api"
MODEL_TIMEOUT = 30  # seconds 