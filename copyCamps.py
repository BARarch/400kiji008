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
    
    campsHash =  [{ 'pubDate':record[0], 
                    'team':feedRow[1], 
                    'title':record[1], 
                    'type':feedRow[2], 
                    'link':record[2], 
                    'discription':record[3], 
                    'creator':record[4]
                    } for record in camps]



    pushedElms = 0
    for elm in reversed(camps):
        cursor.execute(
            "INSERT INTO nfl_team_articles (Date, Team, Title, Type, Link, Discription, Creator, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
            (elm['pubDate'], elm['team'], elm['title'], elm['type'], elm['link'], elm['discription'], elm['creator'], lastId))
    
        pushedElms += 1
    conn.commit()
    print(str(pushedElms) + " kiji-camps")