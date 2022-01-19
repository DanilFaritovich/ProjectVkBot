import time
from ftplib import FTP
import os
from os import path as ospath
import pickle

ftp = FTP('j92745ms.beget.tech')
ftp.login('j92745ms','Gs8fub0N')
print(ftp.retrlines('LIST') )
ftp.cwd('/vkatorez/public_html')

with open('string.bin', 'wb') as fp:
    print(ftp.retrbinary('RETR somefile.txt', fp.write))


with open('string.bin', 'rb') as fh:
    last_content = fh.read()
    len_of_last_content = len(last_content)

while 1:
    file = open('string.bin', 'wb')
    ftp.retrbinary('RETR somefile.txt', file.write)
    file.close()
    time.sleep(0.1)
    print("Yes")
    file = open('string.bin', 'rb')
    content = file.read()
    len_of_content = len(content)
    print(len_of_content)
    if len_of_content != len_of_last_content:
        print("Фаил изменился")
        file.close()
        import authorize
        break
    file.close()
