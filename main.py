from fastapi import FastAPI

app = FastAPI(title="API contacts", 
              description="This is the API contacts",
              version="1.0")

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
