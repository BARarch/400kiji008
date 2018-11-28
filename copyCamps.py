import subprocess
import modelGS as mgs
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
                'register',
                'camp_image_link',
                'camp_video_link'
]

if __name__ == '__main__':
    # Step 0 Initialize Models
    get_credentials = mgs.modelInit()
    conn = config.connect()
    cursor = conn.cursor()
    camps = psd.get_camps()

    pushedElms = 0
    for elm in camps:
        cursor.execute(
            "INSERT INTO kijisearch_camps %s VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
            (str(tuple(campFields)),) + (pushedElms,) + tuple(elm))
    
        pushedElms += 1
    conn.commit()
    print(str(pushedElms) + " kiji-camps")