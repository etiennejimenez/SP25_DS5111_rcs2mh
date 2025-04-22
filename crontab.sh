# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
# MAILTO=rcs2mh@virginia.edu
* * * * * cd home/ubuntu/SP25_DS5111_rcs2mh; make clean; make gainers SRC=yahoo; python yahoo_crontab.py; make gainers SRC=wsj; python wsj_crontab.py
31 13 21-25 4 1-5 cd home/ubuntu/SP25_DS5111_rcs2mh; . env/bin/activate; make clean; make gainers SRC=yahoo; python yahoo_crontab.py; make gainers SRC=wsj; python wsj_crontab.py >> /home/ubuntu/SP25_DS5111_rcs2mh/crontablog.txt 2>&1
30 16 21-25 4 1-5 cd home/ubuntu/SP25_DS5111_rcs2mh; . env/bin/activate; make clean; make gainers SRC=yahoo; python yahoo_crontab.py; make gainers SRC=wsj; python wsj_crontab.py >> /home/ubuntu/SP25_DS5111_rcs2mh/crontablog.txt 2>&1
01 20 21-25 4 1-5 cd home/ubuntu/SP25_DS5111_rcs2mh; . env/bin/activate; make clean; make gainers SRC=yahoo; python yahoo_crontab.py; make gainers SRC=wsj; python wsj_crontab.py >> /home/ubuntu/SP25_DS5111_rcs2mh/crontablog.txt 2>&1
* * * * * echo "Hello, World!" >> /home/ubuntu/SP25_DS5111_rcs2mh/crontablog.txt 2>&1
