
from dirsync import sync
import os,re,sys,traceback
from datetime import datetime

path_def = os.getcwd()
flogs = open(path_def + '/errors', 'w')

try:
    nfile = open(path_def+'/settings', 'r', encoding="utf-8")
    ldata = nfile.readlines()

    for i in ldata:
        lFolders = i.split('-->')
        f1 = lFolders[0]
        f2 = lFolders[1]

        nf1 = re.sub(r"[u'\']", "", f1)
        nf2 = re.sub(r"[u'\'u'\n']", "", f2)

        flogs.write("Run script " + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
                    + "\n" + "out folder " + f1 + "\n")
        sync(nf1, nf2, 'sync', purge = False)

    nfile.close()

    flogs.write("Complete script " + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
                + "\n" + "inp folder " + f2 + "\n")
    flogs.close()

except Exception:

    flogs.write("Errors: " + path_def + "\n"+traceback.format_exc())
    flogs.close()