import sqlite3
from datetime import datetime, timedelta

# Database name in URI form, so we can open it in read only mode.
dbFile = 'file:db/speedtest.db?mode=ro'

# Function to get the data from the database
#     Arguments:
#         db    := name of the database that we are connecting to in URI form
#         sDate := start date for our search
#         eDate := end date for our search
def getData(db, sDate='', eDate=''):
    # Array that stores the data from the search in JSON format
    d = []

    # If an end date (eDate) is not given then assign current date and time to it
    # and then assign current date - 5 days to the end date (eDate). I do this to
    # make sure that sDate is smaller than eDate otherwise the select statement
    # will not work as expected.
    if not (eDate):
        now = datetime.now()
        eDate = now.strftime('%Y-%m-%d %H:%M:%S')
        sDate = (now - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')

    # Well a start date (sDate) was not entered, so I will just assign 5 days
    # prior to whatever was provided as an end date (eDate)
    if not (sDate):
        sDate = (datetime.strptime(eDate, '%Y-%m-%d %H:%M:%S') - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')

    sqlCmd = "SELECT * FROM stdata WHERE (datetime(date) >= datetime('" + sDate + "')) AND (datetime(date) <= datetime('" + eDate + "'))"

    # Connect to the database
    conn = sqlite3.connect(db, uri=True)
    curs = conn.cursor()

    # Process all of the rows returned and store the data in JSON format then
    # append the data to the array
    for row in curs.execute(sqlCmd):
        rec = {
            'date': row[0],
            'dlBytes': row[1],
            'ulBytes': row[2]
        }

        d.append(rec)

    # Close the DB and return the array
    conn.close()
    return d