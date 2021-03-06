import json
import urllib.request
import requests
from constants import API_URL
from os import path


# Log in to new admin session
def login_admin(email, pw):
    url = API_URL + '/admin/session'
    body = {"email": email, "pw": pw}

    try:
        response = requests.post(url, data=body)
        print('Logged in as admin: ', response.status_code)

        return response.text
    except Exception as err:
        print('Admin Login Error: ', err)


# Upload image files
def upload_files_admin(files, session_token):
    url = API_URL + '/admin/images'
    headers = {'api-token': session_token}
    files_body = []

    # Initialize body of request
    for file in files:
        file_ext = path.splitext(file)[1][1:]
        files_body.append(('files', (file, open(
            file, 'rb'), 'image/' + file_ext)))

    try:
        print('\nStarted Admin Image Upload. Check js console for details\n')
        response = requests.post(url, files=files_body, headers=headers)
        if response.status_code == 201:
            print('Admin Image Upload: 201')
            print('Uploaded',
                  len(response.json()), 'out of', len(files), 'files\n')
        else:
            print('Admin Image Upload: ', response.status_code)
            print(response.json())

    except Exception as err:
        print('Admin Image Upload Error: ', err)
