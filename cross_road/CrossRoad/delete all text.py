

import os

os.chdir('C:/Users/USER/Desktop')

text_files  = []

files = os.listdir()
print(files)


for f in files:
    print(f[-3:])
    if f[:-3]  == 'txt':
        print (f)

        text_files.append(f)

def delete_all_text_files():
    print("[  INITIALIZING  DELETION ]  ")
    for file in text_files:
        print(f'y / n     do you want to delete        {file}')
        option = input(':')
        if option == 'y':
            os.remove(file)

        elif option == 'n':
            continue
    
delete_all_text_files()
