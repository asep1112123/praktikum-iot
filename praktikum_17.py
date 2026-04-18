import requests
import json

server = "https://thingsboard.cloud"
device_id = "81f1d3d0-3b14-11f1-95af-8d736c9fe8db"
api_key = "tb_YXmF6wl5Gi6XD8R9q9UHlbFEADDaka9Lvpn5wXZ291T9fwzURCL4wZGAfAUoOy0MCmm0XUh7eiuADIBKGg3gnQ"

url = f"{server}/api/plugins/telemetry/DEVICE/{device_id}/attributes/SHARED_SCOPE"

data = {
    "led_state": True
}

headers = {
    "X-Authorization": f"ApiKey {api_key}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code, response.text)