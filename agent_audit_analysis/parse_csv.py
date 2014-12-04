#!/usr/bin/env python

import csv
import sys
import datetime

def print_job( list ):
  "This prints the details of a job"
  # time_format: 2014-11-06 00:00:01
  time_format = "%Y-%m-%d %H:%M:%S"
  job_start = None
  job_end = None
  rows = None
  duration = None
  rate = None
  for row in list:
    if row['status']=='COMPLETED':
      job_start = datetime.datetime.strptime(row['job_start_dt'], time_format)
      job_end = datetime.datetime.strptime(row['job_completed_dt'], time_format)
      duration = int(row['rows|sec'])
    elif row['status']=='PROCESSED_EMAIL' or row['status']=='LIST_ROWS_PROCESSED':
      rows = int(row['rows|sec']) 

  if duration > 0 and rows:
    rate = rows / duration
  print("%s,%s,%s,%s,%s" % (job_start, job_end, rows, duration, rate))
  return

f = open(sys.argv[1], 'rt')
try:
    reader = csv.DictReader(f)
    group = []
    for row in reader:
      if row['status']=='STARTING' or row['status']=='RESTARTING':
        if len(group)>=3:
          print_job(group)
        group = []
        group.append(row)
      else:
        group.append(row)
finally:
    f.close() 