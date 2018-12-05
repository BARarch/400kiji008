import subprocess
import modelGS as mgs
import psycopg2
import config as config
from googleapiclient.errors import HttpError

import pandas as pd
import numpy as np

def get_camps():
    """Google Sheets API Code.
    Pulls data from the kiji camps sheet on the google drives
    https://docs.google.com/spreadsheets/d/1Szsa0yzQJBoeOhi-L0xKqEZ1AqKw8aFygO6MJFuUo1g/
    """
    credentials = get_credentials()
    http = credentials.authorize(mgs.httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = mgs.discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    #specify tabName sheetID and range
    tabName = 'Camps'
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


    # Step 1 Load Camp Information
    camps = get_camps()

    campFields = [ 	'name',
                'course',
                'address',
                'city',
                'state',
                'zip_code',
                'phone',
                'website',
                'email',
                'grades',
                'ages',
                'overview',
                'time_of_year',
                'schedule',
                'daily_model',
                'focus_areas',
                'cost',
                'camp_image_link'
    ]

    # Step 2 Clean data with DataFrame
    df = pd.DataFrame.from_records(camps, columns=campFields).replace(np.nan, '', regex=True)
    print(df)

    cursor.close()
    conn.close()
