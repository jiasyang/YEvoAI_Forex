# --------------------------------#
#     Author: Jiasheng Yang       #
#     Date: 2019-07-13            #
# --------------------------------#

import yaml
import os
import datetime
import pytz
import logging
import time
# print(os.path.abspath(__file__))
current_path=os.path.dirname(os.path.abspath(__file__))
# go back one step
current_path = os.path.dirname(current_path)

config_path=os.path.join(current_path,'config.yaml')

# print("config_path :{0}".format(config_path))

yaml.warnings({'YAMLLoadWarning': False})
with open(config_path,'r') as stream:
    env=yaml.load(stream)

env_type=env['env_type']
env=env[env_type]
# print("env-"+str(env))

# --------------------------------#
#     system configuration        #
# --------------------------------#
intervel_time = env["intervel_time"]

intervel_time_split = intervel_time.split(sep="-")

intervel_time_number = int(intervel_time_split[0])

#type={"day","month","Second"}
intervel_time_type = intervel_time_split[1]

his_time_length = env["his_time_length"]

initialDate = env["initialDate"]

if intervel_time_type=="day":
    time_freq = str(intervel_time_number) +"D"
    timedelta=datetime.timedelta(days=1)

# initialDate = datetime.datetime.strptime("2017-08-26", "%Y-%m-%d")

if intervel_time_type=="day":
    if env=='developing':
        curDate=env['curDate']
        curDate = datetime.datetime.strptime(curDate, "%Y-%m-%d")
    else:
        if intervel_time_type == "day":
            # to make h-m-s to be 0-0-0
            curDate_US = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
            str_curDate = curDate_US.strftime("%Y-%m-%d")
            curDate = datetime.datetime.strptime(str_curDate, "%Y-%m-%d")
            # print("init curDate: " + str(curDate))
            interval_day = timedelta
            weekday = curDate.weekday()
            # print("init weekday: " + str(weekday))
            # Monday
            if weekday == 0:
                curDate = curDate - 3*interval_day
            elif weekday == 6:
                curDate = curDate - 2 * interval_day
            else:
                curDate = curDate - 1 * interval_day

curTime = datetime.datetime.today()
curTime = curTime.date()

# --------------------------------#
#     Database configuration      #
# --------------------------------#
host = env["host"]
database = env["database"]
user = env["user"]
password = env["password"]
port = env["port"]

# --------------------------------#
#     specifying data path        #
# --------------------------------#
dataPath = env["dataPath"]
outputPath = env["outputPath"]
inputPath = env["inputPath"]
logPath = env["logPath"]
modelPath = env["modelPath"]

# --------------------------------#
#     data analytics             #
# --------------------------------#
his_daynum_set = env["his_daynum_set"]
initialDate_analytics = env["initialDate_analytics"]
endDate_analytics = env["endDate_analytics"]
date_range_flg = env["date_range_flg"]
import pandas as pd
pd.to_datetime(env["initialDate_analytics"])

# --------------------------------#
#     logging                     #
# --------------------------------#
logging_level = env["logging_level"]
tz_us = pytz.timezone('US/Eastern')
tz_cn = pytz.timezone('Asia/Shanghai')
tz_eu = pytz.timezone('Europe/Berlin')
import __main__
if logging_level == "DEBUG":
    level = logging.DEBUG #logging.INFO
logger = logging.getLogger()
logger.setLevel(level)
rq = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
log_path = logPath

main_file = os.path.basename(__main__.__file__)
main_file = main_file.split('.')[0]
logfile = os.path.join(log_path,main_file + "-" + rq + '.log')

fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info("[configuration] main_file: {0}".format(main_file))
logger.info("[configuration] curDate: {0}".format(curDate))
logger.info("[configuration] host: {0}".format(host))
logger.info("[configuration] database: {0}".format(database))
