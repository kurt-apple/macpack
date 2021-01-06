import csv
with open('data/mac.list') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        def search_hosts(dict, query):
                for i in dict:
                        if query in i['hostname']:
                                return i
                return None
        print search_hosts(reader, 'B')
