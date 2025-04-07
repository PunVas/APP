from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from collections import defaultdict
import html

app = FastAPI()

TARGET_URL = "https://youtu.be/asOpxvkrx1g"
ip_clicks = defaultdict(int)

@app.get("/")
async def redirect_to_github(request: Request):
    client_ip = request.client.host
    ip_clicks[client_ip] += 1
    return RedirectResponse(url=TARGET_URL, status_code=302)

@app.get("/clicks", response_class=HTMLResponse)
def show_clicks():
    table_rows = "".join(
        f"<tr><td>{html.escape(ip)}</td><td>{count}</td></tr>"
        for ip, count in ip_clicks.items()
    )
    html_content = f"""
    <html>
        <head><title>Click Tracker</title></head>
        <body>
            <table border="1">
                <tr><th>IP </th><th>Clk Cnt</th></tr>
                {table_rows}
            </table>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
