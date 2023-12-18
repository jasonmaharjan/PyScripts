import subprocess
import time
import schedule
from dotenv import load_dotenv
import os

load_dotenv()

PYTHON_PATH = os.getenv("PYTHON_PATH")
SCRIPT_PATH = os.getenv("SCRIPT_PATH")

def run_ctkinter():
    print("RUNNING TASK....")
    subprocess.run([PYTHON_PATH, SCRIPT_PATH])
    print("TASK RAN SUCCESSFULLY")

schedule.every(45).minutes.do(run_ctkinter)

while True:
    schedule.run_pending()
    time.sleep(15)  
