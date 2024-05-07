from flask import request
import json

response = request.get_json("elprisenligenu.dk/api/v1/prices/2024/04-19_DK1.json")
print(response.status_code)
print(response)