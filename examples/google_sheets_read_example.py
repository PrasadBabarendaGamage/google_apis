"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'


def get_sheets_service(client_secret_path='./',
                       client_secret_fname='client_secret.json',
                       credentials_path='./',
                       credentials_fname='credentials.json'):
    """
    Setup the Sheets API
    :rtype: Sheets API service object
    """
    store = file.Storage(os.path.join(credentials_path, credentials_fname))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(
            os.path.join(client_secret_path,client_secret_fname), SCOPES)
        creds = tools.run_flow(flow, store)
    return build('sheets', 'v4', http=creds.authorize(Http()))

client_secret_path = '../'
credentials_path = '../'
sheets_service = get_sheets_service(
    credentials_path=credentials_path, client_secret_path=client_secret_path)
# Call the Sheets API
SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
RANGE_NAME = 'Class Data!A2:E'
result = sheets_service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
