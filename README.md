Roman Holiday
====
Ver1.0
- - -
Table of contents
----
* [Overview](#chap1)
* [Environment](#chap2)
* [Usage](#chap3)
* [Details](#chap4)
* [Remarks](#chap5)


<a id="chap1"></a>
<a href="#chap1"></a>
- - -
Overview
----
This Python script is an aid to Linux cron. This script is effective when skipping a specific date (holiday). How to use is very easy!


<a id="chap2"></a>
<a href="#chap2"></a>
- - -
Environment
----
- Linux OS or MacOS
- Python 2.7.10 or later
- SQLite3


<a id="chap3"></a>
<a href="#chap3"></a>
- - -
Usage
----
1. Register a day (holiday) where you do not want to run cron. First, move to the directory where you placed the script.<br>
`cd <script directory>`<br><br>
Launch the script "Roman Holiday".<br>
`python roman_holiday.py`<br>

1. A message appears on the screen instructing you to create a database. This is displayed because there is no database for registering holidays. Follow the instructions on the screen and enter `0504`. `holidaylist.db` is created.

1. Select `2)add holiday` on the initial screen of the script. Follow the script guide to register holidays. Next, enter a description of the holiday.

1. Record the command you want to execute in `/etc/crontab`.<br>
_Example_<br>
`0 5 * * * root python anne.py sh /home/script/log/hello.sh`

1. cron skips the holiday run. You are relieved of the task of manually stopping script execution. You will have a peaceful holiday.


<a id="chap4"></a>
<a href="#chap4"></a>
- - -
Details
----
1. When `anne.py` is executed, the result is described in `log/roman_holiday.log`. `Execution time/Execution content/Execution result` is described. If you skip a holiday, a `Holiday Description` will be written.

1. When confirming the registered holiday.<br>
Select `1)show holiday list`. All registered holidays will be displayed.

1. If you accidentally register a holiday, you can delete it.<br>
Run `python roman_holiday.py` and select `3)del holiday`. Please enter a date to delete.

1. You can delete past holidays at once.<br>
Selecting `8)remove old date` will remove all holidays that have passed.

1. If you do not need a break on your computer.<br>
You can remove all holidays from your computer by selecting `9)remove all date`.


<a id="chap5"></a>
<a href="#chap5"></a>
- - -
Remarks
----
- If you accidentally delete the database file, run `python roman_holiday.py` to create a database file.
- Do not change the placement of scripts or database files. The script will stop working.
- If you find a bug, please report it. I also accept requests for improvements and new ideas. [issue](https://github.com/Yuki-Matsumura/roman_holiday/issues)
- The movie "Roman Holiday" gave me some ideas on creating this script. I am grateful.
