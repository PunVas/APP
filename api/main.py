from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

TARGET_URL = "https://github.com/Akshit2807/e_waste_app/releases/latest"

@app.get("/")
def redirect_to_github():
    return RedirectResponse(url=TARGET_URL, status_code=302)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
