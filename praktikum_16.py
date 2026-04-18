import requests
import json

# Ganti sesuai data kamu
server = "https://thingsboard.cloud"
access_token = "6N0WgQ9ucJYH9WtxM3la"

url = f"{server}/api/v1/{access_token}/telemetry"

data = {
    "temperature": 29
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Status:", response.status_code)
print("Response:", response.text)
