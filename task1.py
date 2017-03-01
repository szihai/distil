import csv

classmap = [127,191,223,239,255]

def ip_class(ip):
	first =  int(ip.split(".")[0])
	if first <= classmap[0]:
		return "A"
	elif first <= classmap[1]: 
		return "B"
	elif first <= classmap[2]: 
		return "C"
	elif first <= classmap[3]:
		return "D"
	elif first <= classmap[4]:
		return "E"




with open('distilAccessLog.tsv','rb') as tsvin , open('newlog.tsv', 'wb') as tsvout:
	tsvin = csv.reader(tsvin, delimiter='\t')
	tsvout = csv.writer(tsvout, delimiter='\t')
	for row in tsvin:
		ipclass = ip_class(row[0])
		row.append(ipclass)
		tsvout.writerow(row)