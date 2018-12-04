import subprocess
import clear as cl
import psycopg2
import config as config
from googleapiclient.errors import HttpError

import pandas as pd
import numpy as np

import sys
import argparse

programFields = [ 	'name',
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
                    'daily_model',
                    'time_of_year',
                    'focus_areas',
                    'cost',
                    'eligibility',
                    'other_locations_of_operation',
                    'profile_pic_link'
]

if __name__ == '__main__':
    # Step 0 Initialize Models
    conn = config.connect()
    cursor = conn.cursor()
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--sheet", help="the sheet id to pull data")
    args = parser.parse_args()
    
    # Step 1 Get Program Data
    if args.sheet:
        print ("[copyPrograms] Pulling Programs from sheetID {}".format(args.sheet))
        sys.argv = sys.argv[:1]  ## Clear Command Line Args befor import google API code
        import pullSheetData as psd
        defalted = False
        programs = psd.get_programs(sheetId=args.sheet)
    else:
        sys.argv = sys.argv[:1]
        import pullSheetData as psd
        defalted = True
        programs = psd.get_programs()
        
    # Step 2 Clear current Programs
    cl.clearPrograms(conn)

    # Step 3 Clean data with DataFrame
    df = pd.DataFrame.from_records(programs, columns=programFields).replace(np.nan, '', regex=True)
    print(df)
    
    # Step 4 Push New Programs
    pushedElms = 0
    for elm in df.values.tolist():
        if len(elm) == 18:
            cursor.execute(
                "INSERT INTO kijisearch_programs (id, {}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);".format(', '.join(programFields)),
                (pushedElms,) + tuple(elm))
        else:
            print('did not add row {}'.format(pushedElms + 2))
            print(str(elm))
    
        pushedElms += 1
    conn.commit()
    print()
    print("DONE")
    print("Pushed " + str(pushedElms) + " kiji-programs")
    if defalted:
        print("[copyPrograms] Program data was pulled from the default sheet since no link was specified")

    cursor.close()
    conn.close()