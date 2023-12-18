import time
import subprocess
import schedule
from dotenv import load_dotenv
import os

load_dotenv()

PYTHON_PATH = os.getenv("PYTHON_PATH")
SCRIPT_PATH = os.getenv("SCRIPT_PATH")

def run_ctkinter():
    subprocess.run([PYTHON_PATH, SCRIPT_PATH])

schedule.every(15).minutes.do(run_ctkinter)

while True:
    schedule.run_pending()
    time.sleep(10)  
