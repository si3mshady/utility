#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import subprocess,time

def launch(seconds=3):
    time_remaining = seconds
    while time_remaining > 0:        
        time.sleep(1)
        time_remaining -= 1
    subprocess.Popen(['/bin/bash','error_uptime_date.sh'])
    subprocess.Popen(['/Library/Frameworks/Python.framework/Versions/3.7/bin/python3','send_googlemail.py'])

launch()

