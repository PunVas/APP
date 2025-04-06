from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

TARGET_URL = "https://www.youtube.com/shorts/FwoIK3Qm6CA"

@app.get("/")
def redirect_to_github():
    return RedirectResponse(url=TARGET_URL, status_code=302)
