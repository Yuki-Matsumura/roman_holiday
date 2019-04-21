from datetime import date
import datetime
import os
import sqlite3



##### Input number #####
def cnsl():
  global now
  now = datetime.datetime.now()
  os.system('clear')
  now_dow = "{0:%a}".format(now)
  now_ymd = "{0:%Y/%m/%d}".format(now)
  print("+==============================================================+" + '\n' +
        "|                                 | Today" + " | " + now_ymd + " (" + now_dow + ")   |" + "\n" +
        "+==============================================================+" + "\n" + "\n")
  global result
  result = os.path.exists('holidaylist.db')
  if result == False:
    dbnotexists()
  print("+=====================+===============+===============+========+" + '\n' +
        "| 1)show holiday list | 2)add holiday | " + color.RED + "3)del holiday" + color.END +
                                                             " | 4)Exit |" + '\n' +
        "+=====================+===============+===============+========+" + '\n' +
        "|  " + color.RED + "8)remove old date" + color.END + "  | " + color.RED + "9)remove all date" + color.END +
        "                      |" + '\n' +
        "+==============================================================+")
  global num
  try:
    num = input(" Please select Number: ")
    action()
  except:
    print("+==============================================================+" + '\n' +
          "|                        Please Number.                        |" + '\n' +
          "+==============================================================+")
    raw_input()
    cnsl()
##### Input number #####


##### Chose case #####
def action():
  if num == 1:
    show()
  elif num == 2:
    add()
  elif num == 3:
    delete()
  elif num == 4:
    os.system('clear')
    print("+==============================================================+" + '\n' +
          "|                          See you.                            |")
    bye()
  elif num == 8:
    olddate()
  elif num == 9:
    alldate()
  elif num == 0504:
    init()
  else:
    print("+==============================================================+" + '\n' +
          "|                      It is out of range.                     |" + '\n' +
          "+==============================================================+")
    raw_input()
    cnsl()
##### Chose case #####


##### Show holiday #####
def show():
  if result == True:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    select = 'SELECT * FROM dl ORDER BY day'
    print("+==============================================================+" + '\n' +
          "|                List of registered holidays.                  |" + '\n' +
          "+==============================================================+")
    for row in c.execute(select):
      print(str(row[0])[0:4] + "/"
         + str(row[0])[4:6] + "/"
         + str(row[0])[6:8] + " ("
         + row[1] + ")" + " :" + row[2])
    conn.close()
    print("+==============================================================+" + '\n' +
          "|              Please push enter. Go to manu.                  |" + '\n' +
          "+==============================================================+")
    raw_input()
    cnsl()
  elif result == False:
    exists()
##### Show holiday #####


##### Add holiday #####
def add():
  if result == True:
    os.system('clear')
    print("+==============================================================+" + '\n' +
          "|                          Add holiday                         |" + '\n' +
          "+==============================================================+")
    inyear  = input(" Please enter year  : ")
    inmonth = input(" Please enter month : ")
    inday   = input(" Please enter day   : ")
    try:
      indate = str(inyear) + str(inmonth).zfill(2) + str(inday).zfill(2)
      wkday = (datetime.datetime(inyear, inmonth, inday)).strftime('%a')
      desc = raw_input('Description(Within 50 characters) :  ')
      conn = sqlite3.connect("holidaylist.db")
      c = conn.cursor()
      c.execute("INSERT INTO dl(day, dotw, desc) VALUES(?, ?, ?)", [indate, wkday, desc])
      conn.commit()
      conn.close()
      print("+==============================================================+" + '\n' +
            "|           Add holiday: " + str(indate)[0:4] + "/" +
                                          str(indate)[4:6] + "/" +
                                          str(indate)[6:8] +
                                " (" + wkday + ")" + "                      |" + '\n' +
            "+==============================================================+")
      raw_input()
      cnsl()
    except ValueError:
      print("+==============================================================+" + '\n' +
            "|                  There is no such date.                      |" + '\n' +
            "+==============================================================+")
      raw_input()
      cnsl()
  elif result == False:
    exists()
##### Add holiday #####


##### Del holiday #####
def delete():
  if result == True:
    os.system('clear')
    now_dow = "{0:%a}".format(now)
    now_ymd = "{0:%Y/%m/%d}".format(now)
    print(color.RED + "+==============================================================+" + '\n' +
                      "|                                 | Today" + " | " + color.END +
          color.GREEN +  now_ymd + " (" + now_dow + ")" + color.END + color.RED + "   |" + '\n' +
                      "+==============================================================+" + '\n' +
                      '|          Delete holiday. Please enter the date.              |' + '\n' +
                      '+==============================================================+' + color.END)
    delyear  = input(" Please enter delete year  : ")
    delmonth = input(" Please enter delete month : ")
    delday   = input(" Please enter delete day   : ")
    try:
      date(int(delyear), int(delmonth), int(delday))
      deldate = str(delyear) + str(delmonth).zfill(2) + str(delday).zfill(2)
      wkday = (datetime.datetime(delyear, delmonth, delday)).strftime('%a')
      conn = sqlite3.connect("holidaylist.db")
      c = conn.cursor()
      c.execute("DELETE FROM dl WHERE day =?", [(deldate)])
      conn.commit()
      conn.close()
      print(color.RED + "+==============================================================+" + '\n' +
                        "|           Del holiday: " + str(deldate)[0:4] + "/" +
                                                      str(deldate)[4:6] + "/" +
                                                      str(deldate)[6:8] +
                                            " (" + wkday + ")" + "                      |" + '\n' +
                        "+==============================================================+" + color.END)
      raw_input()
      cnsl()
    except ValueError:
      print("+==============================================================+" + '\n' +
            "|                  There is no such date.                      |" + '\n' +
            "+==============================================================+")
      raw_input()
      cnsl()
  elif result == False:
    exists()
##### Del holiday #####


##### Del old date #####
def olddate():
  if result == True:
    os.system('clear')
    y_day = now - datetime.timedelta(days=1)
    del_day = "{0:%Y/%m/%d}".format(y_day)
    d_day = str("{0:%Y%m%d}".format(y_day))
    print(color.RED + '+==============================================================+' + '\n' +
                      '|              Delete old holiday. Is it OK?                   |' + '\n' +
                      '+==============================================================+' + '\n' +
                      '| ' + color.END + color.GREEN + '1) No. I stop erasing data.' + color.END +
                                       color.RED + ' | 2) Yes. I remove old holiday.  |' + '\n' +
                      '+==============================================================+' + color.END + '\n' +
          color.RED + '|                      Befor ' + color.END +
             color.GREEN + del_day + color.END + color.RED + '                        |' + '\n' +
                      '+==============================================================+' + color.END)
    try:
      adnum = input(" Please select Number: ")
      if adnum == 1:
        print("+==============================================================+" + '\n' +
              "|      Processing has been canceled. Return to the menu.       |" + '\n' +
              "+==============================================================+")
        raw_input()
        cnsl()
      elif adnum == 2:
        conn = sqlite3.connect("holidaylist.db")
        c = conn.cursor()
        c.execute('DELETE FROM dl WHERE day <=?',[(d_day)])
        conn.commit()
        conn.close()
        print(color.RED + "+==============================================================+" + '\n' +
                          "|                Deleted old registered dates.                 |" + '\n' +
                          "+==============================================================+" + color.END)
        raw_input()
        cnsl()
      else:
        print("+==============================================================+" + '\n' +
              "|                      It is out of range.                     |" + '\n' +
              "+==============================================================+")
        raw_input()
        cnsl()
    except:
      print("+==============================================================+" + '\n' +
            "|                        Please Number.                        |" + '\n' +
            "+==============================================================+")
      raw_input()
      cnsl()
  elif result == False:
    exists()
##### Del old date #####


##### Del all date #####
def alldate():
  if result == True:
    os.system('clear')
    print(color.RED + '+==============================================================+' + '\n' +
                      '|              Delete all holiday. Is it OK?                   |' + '\n' +
                      '+==============================================================+' + '\n' +
                      '| ' + color.END + color.GREEN + '1) No. I stop erasing data.' + color.END +
                                       color.RED + ' | 2) Yes. I remove all holiday.  |' + '\n' +
                      '+==============================================================+' + color.END)
    try:
      adnum = input(" Please select Number: ")
      if adnum == 1:
        print("+==============================================================+" + '\n' +
              "|      Processing has been canceled. Return to the menu.       |" + '\n' +
              "+==============================================================+")
        raw_input()
        cnsl()
      elif adnum == 2:
        conn = sqlite3.connect("holidaylist.db")
        c = conn.cursor()
        alldel = 'DELETE FROM dl'
        c.execute(alldel)
        conn.commit()
        conn.close()
        print(color.RED + "+==============================================================+" + '\n' +
                          "|                Deleted all registered dates.                 |" + '\n' +
                          "+==============================================================+" + color.END)
        raw_input()
        cnsl()
      else:
        print("+==============================================================+" + '\n' +
              "|                      It is out of range.                     |" + '\n' +
              "+==============================================================+")
        raw_input()
        cnsl()
    except:
      print("+==============================================================+" + '\n' +
            "|                        Please Number.                        |" + '\n' +
            "+==============================================================+")
      raw_input()
      cnsl()
  elif result == False:
    exists()
##### Del all date #####


##### Initialize database #####
def init():
  result = os.path.exists('holidaylist.db')
  if result == True:
    os.system('clear')
    print('\n' + '+==============================================================+' + '\n' +
                 '|                  Database file is exists.                    |' + '\n' +
                 '+==============================================================+')
    raw_input()
    os.system('clear')
  elif result == False:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    create = 'CREATE TABLE dl(day DATETIME, dotw VARCHAR(3), desc VARCHAR(50))'
    c.execute(create)
    print('\n' + '+==============================================================+' + '\n' +
                 '|              Create file "holidaylist.db".                   |' + '\n' +
                 '+==============================================================+')
    raw_input()
    cnsl()
##### Initialize database #####


##### Database file is not exists #####
def exists():
  os.system('clear')
  print('\n' + '+==============================================================+' + '\n' +
               '|                Database file is not exists.                  |' + '\n' +
               '+==============================================================+')
  raw_input()
  cnsl()
##### Database file is not exists #####


##### Note #####
def dbnotexists():
  print("+==============================================================+" + '\n' +
        "|                           Note !                             |" + '\n' +
        "+==============================================================+" + '\n' +
        "|  Database file is not exists. First initialize push '0504'   |")
##### Note #####


##### exit? #####
def bye():
  print(       '+==============================================================+')
  raw_input(   '|                 Please push Enter key:                       |' + '\n' +
               '+==============================================================+')
  os.system('clear')
##### exit? #####


##### Color #####
class color:
  RED = '\033[31m'
  GREEN = '\033[32m'
  END = '\033[0m'
##### Color #####


cnsl()
