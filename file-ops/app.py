import shelve

shelveFile = shelve.open('data')
cats = ['Eggy 1', 'Eggy 2', 'Eggy 3', 'Pupu']
shelveFile['cats'] = cats
shelveFile.close()

