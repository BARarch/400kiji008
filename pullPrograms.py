import subprocess
import modelGS as mgs
import psycopg2
import config as config
from googleapiclient.errors import HttpError

def get_programs():
    """Google Sheets API Code.
    Pulls data from the kiji programs sheet on the google drives
    https://docs.google.com/spreadsheets/d/1Szsa0yzQJBoeOhi-L0xKqEZ1AqKw8aFygO6MJFuUo1g/
    """
    credentials = get_credentials()
    http = credentials.authorize(mgs.httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = mgs.discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    #specify tabName sheetID and range
    tabName = 'Programs'
    lastColumn = 'R'
    spreadsheetId = '1Szsa0yzQJBoeOhi-L0xKqEZ1AqKw8aFygO6MJFuUo1g'
    rangeName = tabName + '!A2:' + lastColumn
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Done')

    return values

if __name__ == '__main__':
    # Step 0 Initialize Models
    get_credentials = mgs.modelInit()
    conn = config.connect()
    cursor = conn.cursor()


    # Step 1 Load Program Information
    programs = get_programs()

    for program in programs:
        print(program)
        print(len(program))
    
