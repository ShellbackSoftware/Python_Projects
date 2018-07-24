# Script that blocks sites between certain periods of time
import time
from datetime import datetime as dt
# Windows
# Automate using Task Scheduler
# host_path = "C:\Windows\System32\drivers\etc\hosts"
# Mac
# Automate using Cron
host_path = "etc/hosts"
host_temp = "SiteBlocker/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    # Check if hours are between 8 AM and 4 PM (Working hours)
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        with open(host_temp,'r+') as file:
            content=file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            # The number is where the pointer goes; 0 goes to before the first character
            file.seek(0)
            for line in content:
                # Checks for sites from the website_list above, and if they aren't in it, add them.
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
    # Wait 5 seconds
    time.sleep(5)