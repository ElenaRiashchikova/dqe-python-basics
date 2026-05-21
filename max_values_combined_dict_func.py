import random

def create_source_dictionaries(number_of_dicts = 4, number_of_pairs = 4):
    dictionaries: list = []
    dictionary_keys: list = []
    for run in range(0, number_of_dicts):
        dictionary: dict = {}
        for random_key in random.sample("abcdefghi", k=number_of_pairs):
            dictionary_keys.append(random_key)
            dictionary[random_key] = random.randint(0, 100)
        dictionaries.append(dictionary)
    return dictionaries, dictionary_keys

def create_dictionary_grouped_by_keys (dictionaries_list_to_group, dictionary_keys_to_group):
    pre_final_dictionary: list = []
    for random_key in dictionary_keys_to_group:
        c: dict = {}
        pre_final_dictionary.append(c)
        for run in range(0, len(dictionaries_list_to_group)):
            dictionary: dict = dictionaries_list_to_group[run]
            pre_key = str(random_key) + "_" + str(run)
            if random_key in dictionary.keys():
                c.update({pre_key: dictionary.get(random_key)})
    return pre_final_dictionary

def create_final_dictionary(dictionary_grouped_by_key_maxvalue):
    final_dictionary: dict = {}
    for dictionary in dictionary_grouped_by_key_maxvalue:
        if len(dictionary) > 1:
            final_key = None
            final_value = None
            for k, v in dictionary.items():
                if final_key is None or v > final_value:
                    final_key = k
                    final_value = v
            final_dictionary.update({final_key: final_value})
        else:
            final_dictionary.update(dictionary)
    return final_dictionary


dictionaries_list, dictionary_keys_global = create_source_dictionaries()

print("source_dictionaries_list:", dictionaries_list)
print("source_dictionaries_list:", dictionary_keys_global)

pre_final_dictionary_grouped = create_dictionary_grouped_by_keys(dictionaries_list, dictionary_keys_global)

print("pre_final_dictionary_grouped:", pre_final_dictionary_grouped)

final_dictionary_results = create_final_dictionary(pre_final_dictionary_grouped)

print("final_dictionary:",final_dictionary_results)
