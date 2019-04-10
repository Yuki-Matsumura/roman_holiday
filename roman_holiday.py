import datetime
import os
import sqlite3
now = datetime.datetime.now()

##### Input number #####
def cnsl():
  os.system('clear')
  now_dow = "{0:%a}".format(now)
  now_ymd = "{0:%Y/%m/%d}".format(now)
  print("Today" + "          " + now_ymd + "(" + now_dow + ")" + "\n" + "\n")
  global result
  result = os.path.exists('holidaylist.db')
  if result == False:
    dbnotexists()
  print("+=====================+===============+===============+========+")
  print("| 1)show holiday list | 2)add holiday | 3)del holiday | 4)Exit |")
  print("+=====================+===============+===============+========+")
  global num
  num = input(" Please select Number: ")


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
  elif num == 0504:
    init()
  else:
    print("It is out of range.")


##### Show holiday #####
def show():
  if result == True:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    select = 'SELECT * FROM dl'
    for row in c.execute(select):
      print(str(row[0]) + " /" + row[1] + " :" + row[2])
    bye()
  elif result == False:
    exists()


##### Add holiday #####
def add():
### refact start ####
  if result == True:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    select = 'SELECT * FROM dl'
    for row in c.execute(select):
      print row[0]
### refact end ###
  elif result == False:
    exists()

##### Del holiday #####
def delete():
### refact start ####
  if result == True:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    select = 'SELECT * FROM dl'
    for row in c.execute(select):
      print row[0]
### refact end ###
  elif result == False:
    exists()


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
    os.system('clear')


##### Database file is not exists #####
def exists():
  os.system('clear')
  print('\n' + '+==============================================================+' + '\n' +
               '|                Database file is not exists.                  |' + '\n' +
               '+==============================================================+')
  raw_input()
  os.system('clear')


##### Note #####
def dbnotexists():
  print("+==============================================================+" + '\n' +
        "|                           Note !                             |" + '\n' +
        "+==============================================================+" + '\n' +
        "|  Database file is not exists. First initialize push '0504'   |")


##### exit? #####
def bye():
  print(       '+==============================================================+')
  raw_input(   '|                 Please push Enter key:                       |' + '\n' +
               '+==============================================================+')
  os.system('clear')


cnsl()
action()
