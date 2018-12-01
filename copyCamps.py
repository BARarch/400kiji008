import subprocess
import pullSheetData as psd
import psycopg2
import config as config
from googleapiclient.errors import HttpError

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
    camps = psd.get_camps()

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
    print("Pushed" + str(pushedElms) + " kiji-camps")

    cursor.close()
    conn.close()