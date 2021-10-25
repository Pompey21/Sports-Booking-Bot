# Copyright (c) 2021 Apurv Mishra
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from bot import main

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(main, "cron", id="job_1", hour=6, minute=31)

scheduler.start()