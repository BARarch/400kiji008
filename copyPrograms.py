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



    programsHash =  [{ 'pubDate':record[0], 
                    'team':feedRow[1], 
                    'title':record[1], 
                    'type':feedRow[2], 
                    'link':record[2], 
                    'discription':record[3], 
                    'creator':record[4]
                    } for record in programs]

    pushedElms = 0
    for elm in reversed(programs):
        cursor.execute(
            "INSERT INTO nfl_team_articles (Date, Team, Title, Type, Link, Discription, Creator, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
            (elm['pubDate'], elm['team'], elm['title'], elm['type'], elm['link'], elm['discription'], elm['creator'], lastId))
    
        pushedElms += 1
    conn.commit()
    print(str(pushedElms) + " kiji-programs")