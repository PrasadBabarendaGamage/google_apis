"""
Shows basic usage of the Sheets API. Reads values from a Google Spreadsheet and
writes them to another sheet
"""
import google_apis

scope = 'https://www.googleapis.com/auth/spreadsheets'

if __name__ == '__main__':

    # Read a sheet created by google
    read_spreadsheet_id = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    read_range_name = 'Class Data!A2:E'

    client_secret_path = '../'
    credentials_path = '../'
    read_sheets_service = google_apis.get_sheets_service(
        credentials_path=credentials_path,
        client_secret_path=client_secret_path,
        scopes=scope)
    values = google_apis.read_sheets_values(
        read_sheets_service, read_spreadsheet_id, read_range_name)
    rows = []
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
            rows.append([row[0],row[4]])

    # Create a sheet under your google account and paste the spreadsheet_id and
    # sheet range below
    write_spreadsheet_id = '1l1oamBWIh9MpwCt7ZiPlZ2XckgJP6TyrCoB5U4WWV3Y'
    write_sheet_name = 'Sheet1'
    write_range_name = 'A2:B'
    write_sheets_service = google_apis.get_sheets_service(
        credentials_path=credentials_path,
        client_secret_path=client_secret_path,
        scopes=scope)

    google_apis.clear_sheet(write_sheets_service, write_spreadsheet_id, write_sheet_name)

    # Select range of cells to write to
    num_rows = len(rows)
    num_cols = len(rows[0])
    start_row = 1
    start_col = 1
    write_range_name = '{0}!{1}{2}:{3}{4}'.format(
        write_sheet_name,
        google_apis.num2ascii(start_col-1), start_row,
        google_apis.num2ascii(num_cols-1), '')
    google_apis.write_rows(write_sheets_service, write_spreadsheet_id,
                           write_range_name, rows)