import subprocess
import pullSheetData as psd
import clear as cl
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
    conn = config.connect()
    cursor = conn.cursor()
    programs = psd.get_programs()

    # Step 1 Clear current Programs
    cl.clearPrograms(conn)

    # Step 2 Push New Programs
    pushedElms = 0
    for elm in programs:
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

    cursor.close()
    conn.close()