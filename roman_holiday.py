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
  os.system('clear')
  conn = sqlite3.connect("holidaylist.db")
  c = conn.cursor()
  select = 'SELECT * FROM TEST'
  for row in c.execute(select):
    print row[0]


##### Add holiday #####
def add():
  print("add")


##### Del holiday #####
def delete():
  print("delete")


##### Initialize database #####
def init():
### refact start ###
  result = os.path.exists('holidaylist.db')
  if result == True:
    os.system('clear')
    print("Database file is exists.")
  elif result == False:
    os.system('clear')
    conn = sqlite3.connect("holidaylist.db")
    c = conn.cursor()
    create = 'CREATE TABLE daylist(doy varchar(10), dayy datetime)'
    c.execute(create)
    print('Initialize holiday list database.')
### refact end ###



cnsl()
action()
