import re   
import pyfpgrowth
import pprint

datas = open("dataset.txt", "r")
twits = datas.readlines()

clearedTwits = []
for twit in twits:
    clearS = re.sub("[^a-zA-Z ]", "", twit)
    clearS = re.sub("  |   ", " ", clearS)
    clearedTwits.append(clearS)

dataset = []
for dt in clearedTwits:
    data = dt.split(' ')
    dataset.append(data)

patterns = pyfpgrowth.find_frequent_patterns(dataset, 2)
#rules = pyfpgrowth.generate_association_rules(patterns, 0.3)    

print(patterns)
datas.close()
