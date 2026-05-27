import re
import csv
csv.register_dialect('newspaper_counts_csv_dialect', delimiter='-', quoting=csv.QUOTE_MINIMAL)

path_to_file = 'Newspaper_from_files.txt'

def calculate_words(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file_text:
            source_text = file_text.read()
            words = re.findall(r'\w+', source_text.lower())
            words_count: dict = {}
            for word in words:
                result = words_count.get(word)
                if not result:
                        words_count.update({word: 1})
                else:
                        words_count.update({word: result + 1})
            return words_count

def calculate_letters(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file_text:
        source_text = file_text.read()
        letters = [char for char in source_text if char.isalpha()]
        letters_count: dict = {}
        for letter in letters:
            result = letters_count.get(letter)
            if not result:
                letters_count.update({letter: 1})
            else:
                letters_count.update({letter: result + 1})
        return letters_count

def create_letters_counts_for_csv(letters_count_dict):
    csv_letter_counts_dicts: dict = {}
    all_letters_count = sum(letters_count_dict.values())
    for key, value in letters_count_dict.items():
        if not csv_letter_counts_dicts.get(key.lower()):
            if str(key).isupper():
                csv_letter_counts_dicts.update({key.lower(): {"count_all": value, "count_uppercase": value}})
            else:
                csv_letter_counts_dicts.update({key.lower(): {"count_all": value, "count_uppercase": 0}})
        else:
            if str(key).isupper():
                csv_letter_counts_dicts.update({key.lower(): {"count_all": csv_letter_counts_dicts.get(key.lower()).get("count_all") + value,
                                                     "count_uppercase": value}})
            else:
                csv_letter_counts_dicts.update({key.lower(): {"count_all": csv_letter_counts_dicts.get(key.lower()).get("count_all") + value,
                                                     "count_uppercase": csv_letter_counts_dicts.get(key.lower()).get("count_uppercase")}})

        csv_letter_counts_dicts.update({key.lower(): {"count_all": csv_letter_counts_dicts.get(key.lower()).get("count_all"),
                                                     "count_uppercase": csv_letter_counts_dicts.get(key.lower()).get("count_uppercase"),
                                                      "percentage": round((csv_letter_counts_dicts.get(key.lower()).get("count_all") / all_letters_count) * 100)}})

    return csv_letter_counts_dicts



def create_csv_for_words_count(words_count_dict):
    with open('words_calculation.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, 'newspaper_counts_csv_dialect')
            for k, v in words_count_dict.items():
                    writer.writerow([k, v])


def create_csv_for_letters_count(csv_letters_counts):
    with open('letters_calculation.csv', 'w', newline='') as csvfile:
            headers = ["letter", "count_all", "count_uppercase", "percentage"]
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for key, value in csv_letters_counts.items():
                writer.writerow({"letter": key, "count_all": value.get("count_all"),
                                "count_uppercase": value.get("count_uppercase"),
                                 "percentage": value.get("percentage")})




words_count_dict = calculate_words(path_to_file)
create_csv_for_words_count(words_count_dict)

letters_count_dict = calculate_letters(path_to_file)
csv_letters_counts = create_letters_counts_for_csv(letters_count_dict)
create_csv_for_letters_count(csv_letters_counts)



