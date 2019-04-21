from datetime import date
import datetime
import sqlite3
import subprocess
import sys

args = sys.argv
num = (len(args))
comm = (args[1:num])


def action():
  file = open('log/roman_holiday.log', 'a')
  now = datetime.datetime.now()
  now_ymd = "{0:%Y%m%d}".format(now)
  conn = sqlite3.connect("holidaylist.db")
  c = conn.cursor()
  row = c.execute("SELECT * FROM dl WHERE day = ?", [(now_ymd)])
  if len(row.fetchall()) == 0:
     res = subprocess.call(comm)
     if res == 0:
       file.write(str(now) + "\t" + str(comm) + "\t" + "Execute command." + "\n")
     else:
       file.write(str(now) + "\t" + str(comm) + "\t" + "Command Error." + "\n")
  else:
    desc = c.execute("SELECT desc FROM dl WHERE day = ?", [(now_ymd)])
    for mes in desc:
      file.write(str(now) + "\t" + str(comm) + "\t" + "Exist holiday date. Not execute command." +
                            "\t" + "Description: " + mes[0] + "\n")
  file.close()
  conn.close()

action()
