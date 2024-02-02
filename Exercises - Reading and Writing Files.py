#Exercises - Reading and Writing Files - Q.ipynb
#Exercice 1
   
import os, datetime

def create_today_directory():
    today_date = str(datetime.date.today())
    list_folders = os.listdir()
    if today_date in list_folders:
        print("Folder already exists")
    else:
        os.makedirs(today_date)
        print("New directory has been created")
create_today_directory()

#Exercice 2
import os, datetime

path= "C:/Users/Cleme/OneDrive/Documents/SKEMA/FMI SOPHIA/S6/PYTHON 2/"
today_date = str(datetime.date.today())
folders_name = str(input("Donne un nom:"))
my_file = open(path + folders_name+".txt",'w')
my_file.write(today_date + "\n")
my_file.close()




