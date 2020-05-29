import os

def makeDirIfNotEmpty(dirName):
  try:
    os.makedirs(dirName)
  except OSError:
    pass

def storeId(parentId, childId, type):
  makeDirIfNotEmpty("db")
  makeDirIfNotEmpty(f"db/{type}")

  file = open(f"db/{type}/{parentId}", "w+")
  file.write(childId)
  file.close()


if __name__ == "__main__":
  from sys import argv
  storeId(argv[1], argv[2], argv[3])
