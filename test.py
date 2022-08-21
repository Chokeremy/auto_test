import os


abspath = os.path.dirname(os.path.abspath(__file__))
dirpath = os.path.dirname(__file__)
testpath = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))

print(abspath)
print(dirpath)
print(testpath)
