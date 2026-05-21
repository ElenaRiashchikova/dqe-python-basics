from datetime import date, datetime
from pathlib import Path
import os
from normalize_text_func import make_text_lower_case, split_text_into_sentences, capitalize_sentences, replace_with_capitalized_sentences

class Publication:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Publication:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class NewsArticle(Publication):
    def __init__(self, article_title, city, article_date):
        Publication.__init__(self, 'News Article')
        self.article_title = article_title
        self.city = city
        self.article_date = article_date
    def __str__(self):
        return self.name + "\n" + self.article_title + "\n" + self.city + "\n" + "Publication date: " + str(self.article_date) + "\n"

class Advertisement(Publication):
    def __init__(self, ad_text, input_date, days_left):
        Publication.__init__(self, 'Advertisement')
        self.ad_text = ad_text
        self.input_date = input_date
        self.days_left = days_left
    def __str__(self):
        return self.name + "\n" + self.ad_text + "\n" + "Advert is valid for: " + str(self.days_left) + " days" + "\n"

class Horoscope(Publication):
    def __init__(self, sign, horoscope_text):
        Publication.__init__(self, "Horoscope")
        self.sign = sign
        self.horoscope_text = horoscope_text
    def __str__(self):
        return self.name + "\n" + self.sign + "\n" + self.horoscope_text + "\n"


class UserInputSourceOfPublication():
    @staticmethod
    def request_source_of_publication():
        input_type = input("Enter type of publication input 'file' or 'text': ")
        if input_type == 'text':
            a = UserInputManual().get_text_of_publication_from_user()
            Publisher.publish_to_file(a)
        elif input_type == 'file':
            path_to_file = input("Enter path to file or 'default' if file is in default folder: ")
            if path_to_file == 'default':
                b = UserInputByFile().get_file_for_publication_from_user('Publication_text_to_print.txt')
                for i in b:
                    Publisher.publish_to_file(i)
                os.remove('Publication_text_to_print.txt')
            elif path_to_file != 'file':
                b = UserInputByFile().get_file_for_publication_from_user(Path(path_to_file))
                for i in b:
                    Publisher.publish_to_file(i)
                os.remove(path_to_file)
        else:
            print("Please enter a valid input")

class UserInputTypeOfPublication():
    @staticmethod
    def request_type_of_publication_from_user():
        publication_id = input("Enter publication_id: 1 - for new article, 2 - for new advertisement, 3 - for new horoscope: ")
        return publication_id

class UserInputManual():
    @staticmethod
    def get_text_of_publication_from_user():
        publication_id = UserInputTypeOfPublication().request_type_of_publication_from_user()
        if publication_id == '1':
            article_title = input("Enter article title: ")
            city = input("Enter city: ")
            return NewsArticle(article_title, city, date.today())
        elif publication_id == '2':
            ad_text = input("Enter ad title: ")
            input_date = input("Enter end date in format YYYY-MM-DD: ")
            today_date = date.today()
            formatted_date = datetime.strptime(input_date, "%Y-%m-%d").date()
            date_difference = formatted_date - today_date
            return Advertisement(ad_text, input_date, date_difference.days)
        elif publication_id == '3':
            sign = input("Enter sign: ")
            horoscope_text = input("Enter horoscope text: ")
            return Horoscope(sign, horoscope_text)
        else:
            print("Please enter a valid input")

class UserInputByFile:
    @staticmethod
    def get_file_for_publication_from_user(path_to_file):
            with open(path_to_file, 'r', encoding='utf-8') as file_text:
                source_text = file_text.read()
                lower_case_only_text = make_text_lower_case(source_text)
                lower_case_sentences = split_text_into_sentences(lower_case_only_text)
                capitalize_sentences_list = capitalize_sentences(lower_case_sentences)
                fully_fixed_case_text = replace_with_capitalized_sentences(lower_case_only_text,
                                                                           capitalize_sentences_list,
                                                                           lower_case_sentences)
                publication_id = UserInputTypeOfPublication().request_type_of_publication_from_user()
                if publication_id == '1':
                    news_articles_list:list = []
                    news_articles_lines:list = []
                    for line in fully_fixed_case_text.splitlines():
                        print(line)
                        if line == '\n' or line == '':
                            news_articles_list.append(NewsArticle(news_articles_lines[0], news_articles_lines[1], date.today()))
                            news_articles_lines.clear()
                        else:
                            news_articles_lines.append(line.strip())
                    return  news_articles_list
                elif publication_id == '2':
                    adverts_list:list = []
                    adverts_lines:list = []
                    for line in fully_fixed_case_text.splitlines():
                        if line == '\n' or line == '':
                            today_date = date.today()
                            formatted_date = datetime.strptime(adverts_lines[1].strip(), "%Y-%m-%d").date()
                            date_difference = formatted_date - today_date
                            adverts_list.append(Advertisement(adverts_lines[0], adverts_lines[1], date_difference.days))
                            adverts_lines.clear()
                        else:
                            adverts_lines.append(line.strip())
                    return  adverts_list
                elif publication_id == '3':
                    horoscope_list:list = []
                    horoscope_lines:list = []
                    for line in fully_fixed_case_text.splitlines():
                        if line == '\n' or line == '':
                            horoscope_list.append(Horoscope(horoscope_lines[0], horoscope_lines[1]))
                            horoscope_lines.clear()
                        else:
                            horoscope_lines.append(line.strip())
                    return horoscope_list
                else:
                    print("Please enter a valid input")


class Publisher:
    @staticmethod
    def publish_to_file(text):
        with open('Newspapper_from_files.txt', 'a', encoding='utf-8') as f:
            print(text, file=f)


UserInputSourceOfPublication().request_source_of_publication()

