import socket
import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Awesome API",
    description="Basic API used by example in Vault learning course. Project for University of Picardie (Amiens, France) - Master's Degree."
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/livez")
def alive():
    return("I'm alive!")

@app.get("/wellcome/{name}", response_class=HTMLResponse)
def wellcome(request: Request, name: str):
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%H:%M:%S")
    image_url = os.environ.get('IMAGE_URL', "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXBzZGthY2VyeHdjZGFrdTVoeXN1bzMzczllb2hubHRqZGw4ZnhicCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OYg6ybQlRp6Pwm4tzP/giphy.webp")
    secret_value = os.environ.get('SECRET_VALUE', "")

    return templates.TemplateResponse(
        request=request, name="index.html", context={
                                                "hostname": hostname,
                                                "current_time": current_time,
                                                "image_url": image_url,
                                                "secret_value": secret_value,
                                            }
    )

