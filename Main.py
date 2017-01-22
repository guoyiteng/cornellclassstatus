from Mail import sendEmail
from AddDrop import getHTML, parseHTML
from threading import Timer
from datetime import datetime
import functools
import time
import sys

def checkStatus(subject, number, section):
    check = functools.partial(checkStatus, subject = subject, number = number, section = section)
    url = "https://classes.cornell.edu/browse/roster/SP17/class/%s/%s" % (subject, number)
    html = getHTML(url)
    resultDict = parseHTML(html)
    if resultDict.get("Class Section " + section) == "open-status-open":
        sendEmail("%s %s %s" % (subject, number, section))
        print("Ding Ding Ding")
    else: 
        print(str(datetime.now()) + ": Not available")
        Timer(3,check).start()

def main():
    args = sys.argv
    if len(args) != 5:
        print("Usage: python Main.py CS 3410 Lec 001")
    else:
        print("start")
        checkStatus(args[1], args[2], "%s %s" % (args[3], args[4]))

if __name__ == '__main__':
    main()
