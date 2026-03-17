from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/otp/{phone}")
def send_otp(phone: str):
    return {"phone": phone, "otp": "123456"}
