from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.analyze import router as analyze_router
from api.auth import router as auth_router  #  New router
from api.history import router as history_router

app = FastAPI()

# Allow Nuxt (localhost:3000 or Cloudflare domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with exact origin in production
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(analyze_router, prefix="/api") 
app.include_router(auth_router, prefix="/auth")    #  New
#history router to get the history of the user 
app.include_router(history_router, prefix="/history")
