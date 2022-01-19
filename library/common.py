from library.debug import debug
import os
import requests
import shutil
import datetime
import pytz

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def filedownload(link, name):
    try:
        file = open(DIR + "/feed/management/files/" + name, "wb")
        file.write(requests.get(link).content)
        file.close()
        debug("Download", 0, "Successfully Download. {}".format(link))
        return True
    except Exception as e:
        print(e)
        debug("Download", 2, "File Download Failed. {}".format(link))
        return False


def backup():
    try:
        shutil.copyfile(DIR + '/db.sqlite3', DIR + '/backup/db-' + datetime.datetime.now(
            pytz.timezone('US/Eastern')).strftime("%Y-%m-%d") + '.sqlite3')
        debug("Admin", 0, "Database Backup Completed.")
    except Exception as e:
        print(e)
        debug("Admin", 2, "Database Backup Failed. {}".format(e))
