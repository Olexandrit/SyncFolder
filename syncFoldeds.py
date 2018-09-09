# -*- coding: utf-8 -*-

from dirsync import sync
import os,re,sys,traceback

path_def = os.getcwd()

try:
    nfile = open(path_def+'/settings', 'rt')
    ldata = nfile.readlines()

    for i in ldata:
        lFolders = i.split('-->')
        f1 = lFolders[0]
        f2 = lFolders[1]

        nf1 = re.sub(r"[u'\\']", "", f1)
        nf2 = re.sub(r"[u'\\'u'\n']", "", f2)

        sync(nf1, nf2, 'sync', purge = False)

    nfile.close()

except Exception:
    flogs = open(path_def + '/errors', 'w')
    flogs.write("File not found or path is incorrect from " + path_def + "\n"+traceback.format_exc())
    flogs.close()