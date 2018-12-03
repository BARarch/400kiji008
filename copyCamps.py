import subprocess
import clear as cl
import psycopg2
import config as config
from googleapiclient.errors import HttpError

import sys
import argparse

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

if __name__ == '__main__':
    # Step 0 Initialize Models
    conn = config.connect()
    cursor = conn.cursor()
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--sheet", help="the sheet id to pull data")
    args = parser.parse_args()
    
    # Step 1 Get Camp Data
    if args.sheet:
        print ("[copyCamps] Pulling Camps from sheetID {}".format(args.sheet))
        sys.argv = sys.argv[:1]  ## Clear Command Line Args befor import google API code
        import pullSheetData as psd
        defalted = False
        camps = psd.get_programs(sheetId=args.sheet)
    else:
        sys.argv = sys.argv[:1]
        import pullSheetData as psd
        defalted = True
        camps = psd.get_programs()

    # Step 2 Clear Current Camps
    cl.clearCamps(conn)

    # Step 3 Push New Camps
    pushedElms = 0
    for elm in camps:
        if len(elm) == 18:
            cursor.execute(
                "INSERT INTO kijisearch_camps (id, {}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);".format(', '.join(campFields)),
                (pushedElms,) + tuple(elm))
        else:
            print('did not add row {}'.format(pushedElms + 2))
            print(str(elm))
    
        pushedElms += 1
    conn.commit()
    print()
    print("DONE")
    print("Pushed " + str(pushedElms) + " kiji-camps")

    if defalted:
        print("[copyCamps] Camp data was pulled from the default sheet since no link was specified")

    cursor.close()
    conn.close()