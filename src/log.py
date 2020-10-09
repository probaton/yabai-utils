import sys
import os
from datetime import datetime

def log(message):
  print(message)

  os.chdir(os.path.abspath(__file__)[:-10])
  try:
    os.makedirs("logs")
  except OSError:
    pass

  file = open(f"logs/{str(datetime.now()).replace(' ', '_')}", "w+")
  file.write(message)
  file.close()
