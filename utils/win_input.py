date = "2017-01-02"
task = "DATAPROCESS" #DATAPROCESS   ,LOG_STATS_BATCH
file = "stocks.txt"
mode = "d"
startdate = "2019-06-26"
enddate = "2019-06-27"

# python start.py -t DATAPROCESS -m d -d 2019-06-28


# date = "2019-06-27"
# task = "DATAPROCESS" #DATAPROCESS   ,LOG_STATS_BATCH
# file = "stocks.txt"
# mode = "b"
# startdate = "2019-06-26"
# enddate = "2019-06-27"

from datetime import datetime
date = datetime.strptime(date,"%Y-%m-%d")

# startdate = 0
# enddate = 0