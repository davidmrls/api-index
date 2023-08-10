from oauth2client.service_account import ServiceAccountCredentials
import httplib2

SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

#Clave privada JSON - ruta
JSON_KEY_FILE = "#ruta-clave-privada"

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())


content = """{
  "url": "#url-indexar",
  "type": "URL_UPDATED"
}"""

response, content = http.request(ENDPOINT, method="POST", body=content)
print(response)
print(content)