import argparse
from datetime import datetime, timedelta
import calendar
import yaml
import sys
from utils import config
import pandas as pd

sys_ver = "linux" # win  linux
if sys_ver == "linux":
    parser = argparse.ArgumentParser(description='Options and arguments (and corresponding environment variables):')
    parser.add_argument('-t','--task', type=str, help="The TASK to run:\n PREPROCESS ()",required=None)
    parser.add_argument('-d','--date', type=lambda s: datetime.strptime(s,"%Y-%m-%d").date(), help='The date to run task',default=0)
    parser.add_argument('-i', '--file', type=str,default=0)
    parser.add_argument('-m', '--mode', type=str,default=0)

    args = parser.parse_args()
else:
    import utils.win_input as args

print("args.task: {0}".format(args.task))
print("args.file: {0}".format(args.file))

if not args.date:

    today = datetime.now().date()
    if calendar.day_name[today.weekday()] == 'Monday':
        curDate = today - timedelta(days=3)
    elif calendar.day_name[today.weekday()] == 'Sunday':
        curDate = today - timedelta(days=2)
    else:
        curDate = today - timedelta(days=2)
else:
    print("args.date: {0}".format(args.date))
    curDate = args.date

if not args.startdate:
    startdate = curDate
else:
    startdate = args.startdate

if not args.enddate:
    enddate = curDate
else:
    enddate = args.enddate

print("curDate: {0}".format(curDate))

main_tasks = ["PREPROCESS"]

all_tasks = main_tasks

if not args.task:
    print("no task in the input")
    raise Exception("It is a wrong task cmd")
    # sys.exit()

elif args.task.upper() in main_tasks:
    if args.task.upper() == "PREPROCESS":
        # from modules import
        # from test import test
        pass
    elif args.task.upper() == "TASK1":
        pass

else:
    print("the task name no in the executed jobs: {0}".format(all_tasks))
    sys.exit()











