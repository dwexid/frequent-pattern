import re   
import pyfpgrowth
import pprint

datas = open("data1.txt", "r")
twits = datas.readlines()

clearedTwits = []
for twit in twits:
    clearS = re.sub("[^a-zA-Z ]", "", twit)
    clearS = re.sub("  |   ", " ", clearS)
    clearS = re.sub(" at ", " ", clearS)
    clearS = re.sub(" and ", " ", clearS)
    clearS = re.sub("amp", "", clearS)
    clearS = re.sub("dan", "", clearS)
    clearS = re.sub("and", "", clearS)
    clearS = re.sub("with", "", clearS)
    clearS = re.sub("RT", "", clearS)
    clearS = re.sub(" yang ", " ", clearS)
    clearS = re.sub("Yang", "", clearS)
    clearS = re.sub("With", "", clearS)
    clearedTwits.append(clearS)

dataset = []
for dt in clearedTwits:
    data = dt.split(' ')
    dataset.append(data)

patterns = pyfpgrowth.find_frequent_patterns(dataset, 2)
rules = pyfpgrowth.generate_association_rules(patterns, 1)    

pprint.pprint(rules)
datas.close()
 
