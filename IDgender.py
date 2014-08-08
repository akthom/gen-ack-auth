#from http://ptigas.com/blog/2012/01/21/name2gender-in-python/

import json 
from collections import defaultdict

INF = 1000000

def medians( m, f ) :
    mm = median(m)
    mf = median(f)
    return {'male':mm, 'female':mf}

# via http://stackoverflow.com/questions/10482339/how-to-find-median
def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if length == 0 : return INF
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

def load_data( file ) :
    names = {}
    f = open( file, 'r' )
    for l in f :
        d = l.rstrip().split(',')

        name = d[0]
        rank = d[1]
        gender = d[2]
        year = d[3]

        if name not in names :
            names[name] = { 'male':[], 'female':[] }

        if gender == 'male' :
            names[name]['male'].append(int(rank))
        else :
            names[name]['female'].append(int(rank))

    return names

db = load_data('names.csv')

names = {}
for d in db:  
    m = medians( db[d]['male'], db[d]['female'])    

    if m['male'] < m['female'] :
        gender = 'male'
    elif m['male'] > m['female'] :
        gender = 'female'
    else:
        gender = 'both'

    names[d] = gender

print json.dumps( names )
