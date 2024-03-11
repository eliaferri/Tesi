import pandas as pd
import os

#path = "D:/Desktop/TESI/Dati 19-02-2024/dataset2023/"
path = os.path.dirname(os.path.realpath(__file__))+"/"

### PULISCO la tabella publications.csv tengo solo le colonne che mi servono ( pubid, eid, title, pubdate, pubname, subject_area, x, y, authors, doi )
pubs = pd.read_csv(path+'publications.csv', delimiter=',', low_memory=False)
print("-File publications.csv aperto con successo")

pubs = pubs.filter(['id', 'eid', 'title', 'pubdate', 'pubname', 'subject_area', 'doi'])
print("--File publications.csv ripulito da colonne superflue")

# CONVERTO subject_area in testuale
pubs['subject_area'] = pubs['subject_area'].map(lambda s: "A+"+str(s)+"")
print("--Subject_area modificata con successo")

# CONVERTO doi a link
pubs['doi'] = pubs['doi'].map(lambda s: "https://doi.org/"+str(s))
print("--DOI modificato con successo")

### MERGE publications.csv con publication_coordinates.csv
coords = pd.read_csv(path+'publications_coordinates.csv', delimiter=',', low_memory=False)
print("-File publications_coordinates.csv aperto con successo")

# INVERTO ASSE Y (limitazione framework)
coords['y'] = coords['y'].map(lambda y: y * -1)
print("--Asse Y modificato con successo")

# MERGE publications.csv con publication_coordinates.csv
pubs = pd.merge(pubs, coords, how='inner', on='id')
print("--Tabelle publications e coordinates unite con successo")


### LAVORO SU AUTHORS
auths = pd.read_csv(path+'authors.csv', delimiter=',', low_memory=False)
auths = auths.filter(['id', 'authname'])
print("--File authors filtrato correttamente")

# CONVERTO in nomi in Caps
auths['authname'] = auths['authname'].map(lambda s: s.title())
print("--Nomi autori modificati correttamente")

# UNISCO gli autori per paper -> un paper = un record con più autori
auths = auths.groupby("id", as_index=False).agg(lambda x: ', '.join(set(x)))
print("--Nomi autori uniti correttamente")

#MERGE tables Publications e Authors
pubs = pd.merge(pubs, auths, how='inner', on='id')
print("--File publications e authors uniti correttamente")


### LAVORO SU KEYWORDS
keys = pd.read_csv(path+'keywords.csv', delimiter=',', low_memory=False)
keys = keys.rename(columns={"pubid": "id"})
print("--File keywords aperto correttamente")

# UNISCO le keyword per paper -> un paper = un record con più keywords
keys = keys.groupby("id", as_index=False).agg(lambda x: ', '.join(set(map(lambda xx: str(xx), x))))
print("--Keywords unite correttamente")

#MERGE tables Publications e Keywords
pubs = pd.merge(pubs, keys, how='inner', on='id')
print("--File publications e keywords uniti correttamente")

#RINOMINO le colonne id -> pubid e authname -> authors per consistenza
pubs = pubs.rename(columns={"id": "pubid", "authname": "authors", "keyword": "keywords"})

#SALVO il file completo
pubs.to_csv(path+"publications_for_deepscatter.csv", index=False)
print("-File publications_for_deepscatter salvato correttamente")
print("--- fine ---")