import subprocess
import modelGS as mgs
import pullSheetData as psd
import psycopg2
import config as config
from googleapiclient.errors import HttpError

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
    get_credentials = mgs.modelInit()
    conn = config.connect()
    cursor = conn.cursor()
    programs = psd.get_programs()

    pushedElms = 0
    for elm in programs:
        cursor.execute(
            "INSERT INTO kijisearch_programs %s VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
            (str(tuple(programFields)),) + (pushedElms,) + tuple(elm))
    
        pushedElms += 1
    conn.commit()
    print(str(pushedElms) + " kiji-programs")