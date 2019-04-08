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
  print("1)show holiday list  2)add holiday  3)del holiday  4)Exit")

  global result
  result = os.path.exists('holidaylist.db')
  if result == False:
    print("+===========================================================+")
    print("| Database file is not exists. First initialize push '0504' |")
    print("+===========================================================+")
  global num
  num = input("Please select Number: ")


##### Chose case #####
def action():
  if num == 1:
    show()
  elif num == 2:
    add()
  elif num == 3:
    delete()
  elif num == 4:
    print("bye...")
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
    select = 'SELECT * FROM daylist'
    for row in c.execute(select):
      print row[0]
  elif result == False:
    exists()


##### Add holiday #####
def add():
### refact start ####
  if result == True:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    select = 'SELECT * FROM daylist'
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
    select = 'SELECT * FROM daylist'
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
    print('+==========================+')
    print('| Database file is exists. |')
    print('+==========================+')
  elif result == False:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    create = 'CREATE TABLE daylist(doy varchar(10), dayy datetime)'
    c.execute(create)
    print('+===============================+')
    print('| Create file "holidaylist.db". |')
    print('+===============================+')


##### Database file is not exists #####
def exists():
  os.system('clear')
  print('+==============================+')
  print('| Database file is not exists. |')
  print('+==============================+')


cnsl()
action()
