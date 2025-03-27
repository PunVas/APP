from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

TARGET_URL = "https://github.com/Akshit2807/e_waste_app/releases/latest"

@app.get("/")
def redirect_to_github():
    return RedirectResponse(url=TARGET_URL, status_code=302)

# Required for Vercel
from mangum import Mangum
handler = Mangum(app)
