from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.books_router import router

app = FastAPI(
    title='Scrape to API',
    description='API para consultar livros coletados no site books-to-scrape',
    version='1.0.0',
)

origins = [
    "http://localhost:5173",   # Vite 
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],      # Quais métodos HTTP: GET, POST, PUT, DELETE...
    allow_headers=["*"],      # Quais cabeçalhos são permitidos
)


app.include_router(router, prefix='/api')
