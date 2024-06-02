import socket
import os
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Awesome API",
    description="Basic API used by example in Vault learning course. Project for University of Picardie (Amiens, France) - Master's Degree."
)

@app.get("/livez")
def alive():
    return("I'm alive!")

@app.get("/wellcome/{name}", response_class=HTMLResponse)
def wellcome(name: str):
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%H:%M:%S")
    image_url = os.environ.get('IMAGE_URL', "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXBzZGthY2VyeHdjZGFrdTVoeXN1bzMzczllb2hubHRqZGw4ZnhicCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OYg6ybQlRp6Pwm4tzP/giphy.webp")
    html_content = f"""
    <html>
        <head>
            <title>👋 Bienvenue {name}</title>
        </head>
        <body>
            <h1>Bienvenue {name}!</h1>
            <p>💻 Tu es connecté depuis <strong>{hostname}</strong>.</p>
            <p>⏳ L'heure actuelle est : <strong>{current_time}</strong>.</p>
            <img src="{image_url}" alt="image">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

