import random

runs = 4
dictionaries: list = []
dictionary_keys: list = []
final_dictionary: dict = {}

for run in range(0, runs):
    dictionary: dict = {}
    for random_key in random.sample("abcdefghi", k=runs):
        dictionary_keys.append(random_key)
        dictionary[random_key] = random.randint(0, 100)
    dictionaries.append(dictionary)

print("source_dictionaries_list:", dictionaries)

dictionary_keys_set = set(dictionary_keys)

pre_final_dictionary: list = []

for random_key in dictionary_keys_set:
    c: dict = {}
    pre_final_dictionary.append(c)
    for run in range(0, runs):
        dictionary: dict = dictionaries[run]
        pre_key = str(random_key) + "_" + str(run)
        if random_key in dictionary.keys():
            c.update({pre_key: dictionary.get(random_key)})

print("pre_final_dictionary:", pre_final_dictionary)

for s in pre_final_dictionary:
    if len(s) > 1:
        final_key = None
        final_value = None
        for k, v in s.items():
            if final_key is None or v > final_value:
                final_key = k
                final_value = v
        final_dictionary.update({final_key: final_value})
    else:
        final_dictionary.update(s)

print("final_dictionary:",final_dictionary)
