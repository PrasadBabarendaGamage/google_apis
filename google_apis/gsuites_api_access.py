"""
Methods for accessing google API's
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import string


def get_sheets_service(client_secret_path='./',
                       client_secret_fname='client_secret.json',
                       credentials_path='./',
                       credentials_fname='credentials.json',
                       scopes='https://www.googleapis.com/auth/spreadsheets.readonly'):
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
            os.path.join(client_secret_path, client_secret_fname), scopes)
        creds = tools.run_flow(flow, store)
    return build('sheets', 'v4', http=creds.authorize(Http()))


def read_sheets_values(service, spreadsheet_id, range_name):
    """

    :param SPREADSHEET_ID: 
    :param RANGE_NAME: 
    :return: 
    """
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name).execute()
    return result.get('values', [])

def write_rows(sheets_service, spreadsheet_id, write_range_name, rows):
    # Write values to target sheet
    body = {
        "majorDimension": "ROWS",
        'values': rows
    }
    result = sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=write_range_name,
        valueInputOption='USER_ENTERED', body=body).execute()

def num2ascii(n,b=string.ascii_uppercase):
   d, m = divmod(n,len(b))
   return num2ascii(d-1,b)+b[m] if d else b[m]

def clear_sheet(service, spreadsheet_id, sheet_name):
    rangeAll = '{0}!A1:Z'.format(sheet_name)
    body = {}
    resultClear = service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id, range=rangeAll, body=body).execute()