from zipfile import *

f = ZipFile('images.zip','w',ZIP_DEFLATED)

f.write('AWS.jpg')
f.write('Django.png')
f.write('Linux.jpg')
f.write('Python-Symbol.png')
f.write('MySQL.png')

f.close()

