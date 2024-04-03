TOKEN = "7081234426:AAGiRfRCt2rVzfUmndn9C2gtZZ4OpHrdVF0"

# Webserver settings
WEB_SERVER_HOST = "localhost" # bind localhost only to prevent any external access
WEB_SERVER_PORT = 8080 # Port for incoming request from reverse proxy. Should be any available port
WEBHOOK_PATH = "/webhook" # Path to webhook route, on which Telegram will send requests
WEBHOOK_SECRET = '' # Secret key to validate requests from Telegram (optional)
BASE_WEBHOOK_URL = "https://81f8-223-204-123-131.ngrok-free.app"