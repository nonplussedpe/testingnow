import csv 

with open("mod3/task3/hospital.csv", encoding='utf-8') as file:
    for i in csv.reader(file, delimiter=";"):
        print(i)