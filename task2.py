import csv
from itertools import groupby

with open('distilAccessLog.tsv','rb') as fin :
	tsvin = csv.reader(fin, delimiter='\t')
	entries = []
	for row in tsvin:
		entries.append(row)

key1 = lambda x: x[0]
key2 = lambda x: int(x[1].split(".")[0])//60
key3 = lambda x: int(x[1].split(".")[0])//1200

entries = sorted(entries, key = key1)
bins = [(k, list(g)) for k,g in groupby(entries, key1)]

with open('pagecount.tsv', 'wb') as fout :
	tsvout = csv.writer(fout, delimiter='\t')
	for key, visits in bins:
		pagesperminute = [(k, len(list(g))) for k,g in groupby(visits, key2)]
		pagespersession = [(k, len(list(g))) for k,g in groupby(visits, key3)]
		minave = sum(j for i, j in pagesperminute)//len(pagesperminute)
		sessionave = sum(j for i, j in pagespersession)//len(pagespersession)
		row = [key, minave,sessionave]
		tsvout.writerow(row)
