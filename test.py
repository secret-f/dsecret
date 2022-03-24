import dsecret, os

dsecret.encode('test.zip', 'test.ds', 'test.txt', True)
print("Encode done")
dsecret.decode('test.ds', 'test.2.zip', 'test.txt', True)
print("Decode done")
os.system('fc test.zip test.2.zip')