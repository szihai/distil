import csv
from itertools import groupby

with open('distilAccessLog.tsv','rb') as fin :
	tsvin = csv.reader(fin, delimiter='\t')
	entries = []
	for row in tsvin:
		entries.append(row)

key1 = lambda x: x[3]
key2 = lambda x: int(x[1].split(".")[0])//120

bins = [(k, list(g)) for k,g in groupby(entries, key2)]
print len(bins)
with open('status.tsv', 'wb') as fout :
	tsvout = csv.writer(fout, delimiter='\t')
	for time, visits in bins:
		visits = sorted(visits,key = key1)
		status = [(k, len(list(g))) for k,g in groupby(visits, key1)]
		row = [time,status]
		tsvout.writerow(row)
