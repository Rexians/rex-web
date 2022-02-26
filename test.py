from operator import itemgetter

d = {'key':10, 'key2':20}
l = [{'age':30},{'age':40}]
nlist = sorted(l, key=itemgetter('age'), reverse=True)
print(nlist)