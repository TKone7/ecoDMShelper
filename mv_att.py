import os
from datetime import date,datetime
from shutil import move
import logging
import time
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

def formatLog(log):
    return datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + ' ' + log
# Working directory
src = '/share/CACHEDEV1_DATA/ecoDMS/scaninput/QmailAgent_xyz@gmail.com/attachment/'
dest = '/share/CACHEDEV1_DATA/ecoDMS/scaninput/'
# logger
# handler = RotatingFileHandler(src + 'move.log', maxBytes=1 * 1024 * 1024, backupCount=5)
handler = TimedRotatingFileHandler(src + 'move.log', when='D', interval=1, backupCount=5)

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

# add a rotating handler
logger.addHandler(handler)

d = date.today()
path = src + str(d.year)

pdf = [x for x in os.listdir(path) if os.path.isfile(path + '/' + x) and x.endswith('.pdf')]
unhandled = [x for x in os.listdir(path) if x not in pdf]

if (len(pdf) == 0):
    logger.info(formatLog('nothing to move this time ... sleep...'))
if (len(unhandled) > 0):
    logger.info(formatLog('Following files are not handled automatically: ' + ', '.join(unhandled)))
for f in pdf:
    move(path + '/' + f, dest)
    logger.info(formatLog('moved ' + f + ' to ' + dest))
