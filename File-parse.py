import pandas
import glob

files = glob.glob('**')
for file in files:
    print(file)