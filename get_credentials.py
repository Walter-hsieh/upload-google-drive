from google_auth_oauthlib.flow import InstalledAppFlow

def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',
        scopes=['https://www.googleapis.com/auth/drive.file']
    )
    creds = flow.run_local_server(port=5000) #8080
    print('Refresh Token:', creds.refresh_token)

if __name__ == '__main__':
    get_credentials()
