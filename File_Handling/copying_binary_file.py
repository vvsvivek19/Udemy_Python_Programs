file = open('AWS.jpg','r')
data = file.read()
copyfile = open('AWS2.jpg','w')
copyfile.write(data)
file.close()
copyfile.close()