# Model Analyzer App

A full-stack application for analyzing model performance with:
- **Frontend**: Nuxt.js for the user interface
- **Backend**: FastAPI for serving the model analysis
- **Database**: Supabase for authentication and storage

## Project Structure

```
/model-analyzer-app/
├── frontend/               # Nuxt app (input form, result display)
├── backend/                # FastAPI backend
│   ├── main.py             # FastAPI app entry
│   ├── api/                # Routes (e.g., analyze.py)
│   ├── db/                 # Supabase client logic
│   ├── models/             # Model execution logic
│   ├── model_checkpoints/  # Contains model files (.pt/.pkl)
│   ├── config.py
│   ├── .env
│   ├── requirements.txt
│   └── venv/               # Python virtual environment
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v18+)
- Python 3.10+
- A Supabase project

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at http://localhost:3000

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

The backend will be available at http://localhost:8000

### Environment Variables

Make sure to set up your `.env` files in both the frontend and backend directories with your Supabase credentials. 