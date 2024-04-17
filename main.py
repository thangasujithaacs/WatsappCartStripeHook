from email.message import EmailMessage
import smtplib
from fastapi import FastAPI, Request, Response,status
import os
import json
import warnings
warnings.filterwarnings('ignore')
import configparser
from fastapi.responses import JSONResponse
from requests import request
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


# Allow all origins, methods, and headers for testing purposes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/create-event")
async def create_event(request: Request,response: Response):
    request_body = await request.json()
    if os.path.exists("requests.json"):
        os.remove("requests.json")
    with open("requests.json", "w") as file:
        json.dump(request_body, file, indent=4)

    return {"message": "Request stored successfully."}

@app.get("/get_requests")
async def get_requests():
    try:
        # Read the stored requests from the file
        with open("requests.json", "r") as file:
            requests_data = json.load(file)
    except FileNotFoundError:
        return JSONResponse(content={"message": "No requests found."}, status_code=404)
    return requests_data