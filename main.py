from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

TARGET_URL = "https://youtu.be/asOpxvkrx1g"

@app.get("/")
def redirect_to_github():
    return RedirectResponse(url=TARGET_URL, status_code=302)
