"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
import google_apis

read_scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'

if __name__ == '__main__':

    # Read a sheet created by google
    spreadsheet_id = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    range_name = 'Class Data!A2:E'

    client_secret_path = '../'
    credentials_path = '../'
    read_sheets_service = google_apis.get_sheets_service(
        credentials_path=credentials_path,
        client_secret_path=client_secret_path,
        scopes=read_scope)
    # Call the Sheets API
    values = google_apis.read_sheets_values(
        read_sheets_service, spreadsheet_id, range_name)
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
