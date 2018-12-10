import csv
import urllib.request
count=0
with open('Hyundai_alltyres.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        if len(row)==0:
            continue
        words = row[0].split('/')
        urllib.request.urlretrieve(row[0], "E:\\abc\\Documents\Hyundai_images"+str(count)+"_"+str(words[5]))
        count+=1
        print(str(count)+"_"+str(words[5]))
