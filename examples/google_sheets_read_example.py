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
    :param client_secret_path: 
    :param client_secret_fname: 
    :param credentials_path: 
    :param credentials_fname: 
    :return: 
    :rtype: Sheets API service object
    """
    store = file.Storage(os.path.join(credentials_path, credentials_fname))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(
            os.path.join(client_secret_path, client_secret_fname), SCOPES)
        creds = tools.run_flow(flow, store)
    return build('sheets', 'v4', http=creds.authorize(Http()))


def read_sheets_values(spreadsheet_id, range_name):
    """

    :param SPREADSHEET_ID: 
    :param RANGE_NAME: 
    :return: 
    """
    result = read_sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name).execute()
    return result.get('values', [])


# Read a sheet created by google
spreadsheet_id = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
range_name = 'Class Data!A2:E'

client_secret_path = '../'
credentials_path = '../'
read_sheets_service = get_sheets_service(
    credentials_path=credentials_path, client_secret_path=client_secret_path)
# Call the Sheets API
values = read_sheets_values(spreadsheet_id, range_name)
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
