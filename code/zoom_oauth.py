# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from getpass import getpass
import webbrowser
import base64
from http.server import BaseHTTPRequestHandler,HTTPServer
from pathlib import Path

import requests
import pandas

class GlobalHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write((
            '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>title</title></script></head><body>'
            '<h1>OK</h1></body></html>'
        ).encode())
        global request_path
        request_path = self.path

    def log_message(self, format, *args):
        return


# +
port = 8878
redirect_url = f"http://lvh.me:{port}/redirect"

client_id = getpass("client id: ")
client_secret = getpass("client secret: ")

# +
webbrowser.open(
    f"https://zoom.us/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_url}"
)
server = HTTPServer(('', port), GlobalHandler)
server.handle_request()
server.socket.close()
auth_code = request_path[len('/redirect?code='):]

response = requests.post(
    f"https://zoom.us/oauth/token?grant_type=authorization_code&code={auth_code}&redirect_uri={redirect_url}",
    headers={
        "Authorization": f"Basic {base64.b64encode(':'.join([client_id, client_secret]).encode()).decode()}"
    },
)

oauth_token = response.json()['access_token']
headers = {"Authorization": f"Bearer {oauth_token}"}

# +
meetings = requests.get("https://api.zoom.us/v2/users/me/meetings", headers=headers).json()

meeting_id = meetings['meetings'][0]['id']

meeting_details = requests.get(f"https://api.zoom.us/v2/meetings/{meeting_id}", headers=headers).json()

registrants = requests.get(f"https://api.zoom.us/v2/meetings/{meeting_id}/registrants?page_size=500", headers=headers).json()

registrants2 = [{**i, **{q["title"]: q["value"] for q in i.pop("custom_questions")}} for i in registrants['registrants']]

data = pandas.DataFrame(registrants2)

# Drop empty columns
data = data.loc[:, data.any(axis=0)]
# -

len(data), len(data[data['Do you wish to register for a discussion with the speaker after the colloquium?'] == "Yes"])

data[data['Do you wish to register for a discussion with the speaker after the colloquium?'] == "Yes"]
