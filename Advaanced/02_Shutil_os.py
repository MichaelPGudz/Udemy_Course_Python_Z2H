import os
import shutil

f = open('practice.txt', 'w+')
f.write('This a test sentence')
f.close()

print(os.getcwd())
print(os.listdir())

shutil