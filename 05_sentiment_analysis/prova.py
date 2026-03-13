import csv
righe = []
with open('/home/biar/Desktop/lab_informatica/05_sentiment_analysis/IMDB_validation.tsv','r',encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for riga in csv_reader:
        righe.append((riga[0],riga[1]))

print(righe[1])