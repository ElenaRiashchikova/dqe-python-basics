import random

runs = 4
dictionaries:list = []
dictionary_keys:list = []
final_dictionary: dict = {}

for run in range(0, runs):
    dictionary:dict = {}
    for i in random.sample("abcdefghi", k=runs):
        dictionary_keys.append(i)
        dictionary[i] = random.randint(0, 100)
    dictionaries.append(dictionary)

print(dictionaries)

dictionary_keys_set = set(dictionary_keys)
print(dictionary_keys_set)

pre_final_dictionary: list = []

for i in dictionary_keys_set:
    c: dict = {}
    pre_final_dictionary.append(c)
    for run in range(0, runs):
        dictionary: dict = dictionaries[run]
        d = str(i) + "_" + str(run)
        if i in dictionary.keys():
            c.update({d: dictionary.get(i)})

print(pre_final_dictionary)


for s in pre_final_dictionary:
    if len(s) > 1:
        t = None
        p = None
        for k,v in s.items():
            if t is None or v > p:
                t = k
                p = v
                # final_dictionary.update({k: v})
        final_dictionary.update({t: p})
    else:
        final_dictionary.update(s)

print(final_dictionary)



