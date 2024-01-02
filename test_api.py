import requests

# Request Api
#url_endpoint = "http://localhost:7071/api/http_trigger"
url_endpoint = "https://functionhugo.azurewebsites.net/api/http_trigger"
params = {
    "name": "John",
    "surname": "Doe",
    "id_number": "123456789"
}

response = requests.request('POST', url_endpoint, params = params)
print(response.status_code)
print(response.text)