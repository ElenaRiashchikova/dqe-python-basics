from datetime import date, datetime
from pathlib import Path
import os
from normalize_text_func import make_text_lower_case, split_text_into_sentences, capitalize_sentences, replace_with_capitalized_sentences
import subprocess
import json
import xml.etree.ElementTree as ET
import pyodbc


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

class Advertisement(Publication):
    def __init__(self, ad_text, input_date, days_left):
        Publication.__init__(self, 'Advertisement')
        self.ad_text = ad_text
        self.input_date = input_date
        self.days_left = days_left

class Horoscope(Publication):
    def __init__(self, sign, horoscope_text):
        Publication.__init__(self, "Horoscope")
        self.sign = sign
        self.horoscope_text = horoscope_text

class UserInputSourceOfPublication:
    @staticmethod
    def request_source_of_publication():
        input_type = input("Enter type of publication input 'text file', 'json file', 'xml file' or 'text': ")
        if input_type == 'text':
            text_from_input = UserInputManual().get_text_of_publication_from_user()
            return text_from_input, "No file"
        else:
            path_to_file = input("Enter path to file or file name if file is in default folder: ")
            if input_type == 'text file':
                text_from_txt_to_print = UserInputByFile().get_file_for_publication_from_user(path_to_file)
                if text_from_txt_to_print is not None:
                    return text_from_txt_to_print, path_to_file
                else:
                    print("Publication text is empty")

            elif input_type == 'json file':
                text_from_json_to_print = UserInputByJson().get_json_file_for_publication_from_user(path_to_file)
                if text_from_json_to_print is not None:
                    return text_from_json_to_print, path_to_file
                else:
                    print("Publication text is empty")

            elif input_type == 'xml file':
                text_from_xml_to_print = UserInputByXml().get_xml_file_for_publication_from_user(path_to_file)
                if text_from_xml_to_print is not None:
                    return text_from_xml_to_print, path_to_file
                else:
                    print("Publication text is empty")
            else:
                print("Please enter a valid input")

class UserInputTypeOfPublication:
    @staticmethod
    def request_type_of_publication_from_user():
        publication_id = input("Enter publication_id: 1 - for new article, 2 - for new advertisement, 3 - for new horoscope: ")
        return publication_id

class UserInputManual:
    @staticmethod
    def get_text_of_publication_from_user():
        publication_id = UserInputTypeOfPublication().request_type_of_publication_from_user()
        if publication_id == '1':
            article_title = input("Enter article title: ")
            city = input("Enter city: ")
            article_text_to_print:list = []
            article_text_to_print.append(NewsArticle(article_title, city, date.today()))
            return article_text_to_print
        elif publication_id == '2':
            ad_text = input("Enter ad title: ")
            input_date = input("Enter end date in format YYYY-MM-DD: ")
            today_date = date.today()
            formatted_date = datetime.strptime(input_date, "%Y-%m-%d").date()
            date_difference = formatted_date - today_date
            advert_to_print:list = []
            advert_to_print.append(Advertisement(ad_text, input_date, date_difference.days))
            return advert_to_print
        elif publication_id == '3':
            sign = input("Enter sign: ")
            horoscope_text = input("Enter horoscope text: ")
            horoscope_to_print:list = []
            horoscope_to_print.append(Horoscope(sign, horoscope_text))
            return horoscope_to_print
        else:
            print("Please enter a valid input")

class UserInputByFile:
    @staticmethod
    def get_file_for_publication_from_user(path_to_file):
        try:
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
                    news_articles_list_to_print:list = []
                    news_articles_lines:list = []
                    for line in fully_fixed_case_text.splitlines():
                        print(line)
                        if line == '\n' or line == '':
                            news_articles_list_to_print.append(NewsArticle(news_articles_lines[0], news_articles_lines[1], date.today()))
                            news_articles_lines.clear()
                        else:
                            news_articles_lines.append(line.strip())
                    return news_articles_list_to_print
                elif publication_id == '2':
                    adverts_list_to_print:list = []
                    adverts_lines:list = []
                    for line in fully_fixed_case_text.splitlines():
                        if line == '\n' or line == '':
                            today_date = date.today()
                            formatted_date = datetime.strptime(adverts_lines[1].strip(), "%Y-%m-%d").date()
                            date_difference = formatted_date - today_date
                            adverts_list_to_print.append(Advertisement(adverts_lines[0], adverts_lines[1], date_difference.days))
                            adverts_lines.clear()
                        else:
                            adverts_lines.append(line.strip())
                    return  adverts_list_to_print
                elif publication_id == '3':
                    horoscope_list_to_print:list = []
                    horoscope_lines:list = []
                    for line in fully_fixed_case_text.splitlines():
                        if line == '\n' or line == '':
                            horoscope_list_to_print.append(Horoscope(horoscope_lines[0], horoscope_lines[1]))
                            horoscope_lines.clear()
                        else:
                            horoscope_lines.append(line.strip())
                    return horoscope_list_to_print
                else:
                    print("Please provide valid text")
        except FileNotFoundError:
            print("Please provide valid file")

class UserInputByJson:
    @staticmethod
    def get_json_file_for_publication_from_user(path_to_file):
        try:
            with open(path_to_file, 'r', encoding='utf-8') as file_text:
                publications_list = json.load(file_text)
                print(publications_list)
                publications_list_to_print: list = []
                for publication in publications_list:
                    print(publication)
                    publication_type = publication["publication_type"]
                    if publication_type == 'NewsArticle':
                        publications_list_to_print.append(NewsArticle(publication["article_title"], publication["city"], date.today()))
                    elif publication_type == 'Advert':
                        today_date = date.today()
                        formatted_date = datetime.strptime(publication["end_date"], "%Y-%m-%d").date()
                        date_difference = formatted_date - today_date
                        publications_list_to_print.append(Advertisement(publication["advert_text"], publication["end_date"], date_difference.days))
                    elif publication_type == 'Horoscope':
                        publications_list_to_print.append(Horoscope(publication["sign"], publication["horoscope_text"]))
                    else:
                        print("Please provide valid text")
                return publications_list_to_print
        except FileNotFoundError:
            print("Please provide valid file")

class UserInputByXml:
    @staticmethod
    def get_xml_file_for_publication_from_user(path_to_file):
        try:
            with open(path_to_file, 'r', encoding='utf-8') as file_text:
                xml_file = ET.parse(file_text)
                root = xml_file.getroot()
                publications_list_to_print: list = []
                for i in root:
                    if i.tag == 'NewsArticle':
                        publications_list_to_print.append(NewsArticle(root.findtext('NewsArticle/Title'), root.findtext('NewsArticle/City'), date.today()))
                    elif i.tag == 'Advert':
                        today_date = date.today()
                        formatted_date = datetime.strptime(root.findtext('Advert/End_date'), "%Y-%m-%d").date()
                        date_difference = formatted_date - today_date
                        publications_list_to_print.append(Advertisement(root.findtext('Advert/Text'), root.findtext('Advert/End_date'), date_difference.days))
                    elif i.tag == 'Horoscope':
                        publications_list_to_print.append(Horoscope(root.findtext('Horoscope/Sign'), root.findtext('Horoscope/Text')))
                    else:
                        print("Please provide valid text")
                return publications_list_to_print
        except FileNotFoundError:
            print("Please provide valid file")

class PublisherToFile:
    @staticmethod
    def publish_to_file(publications):
        with open('Newspaper_from_files.txt', 'a', encoding='utf-8') as f:
            for publication in publications:
                if publication.__class__.__name__ == 'NewsArticle':
                    print(publication.name + "\n" + publication.article_title + "\n" + publication.city + "\n" + "Publication date: " + str(publication.article_date) + "\n", file=f)
                elif publication.__class__.__name__ == 'Advertisement':
                    print(publication.name + "\n" + publication.ad_text + "\n" + "Advert is valid for: " + str(publication.days_left) + " days" + "\n", file=f)
                elif publication.__class__.__name__ == 'Horoscope':
                    print(publication.name + "\n" + publication.sign + "\n" + publication.horoscope_text + "\n", file=f)
                else:
                    pass

class PublisherToDb:
    @staticmethod
    def publish_to_db(publications):
        connection = pyodbc.connect(
            'Driver={SQLite3 ODBC Driver};'
            'Direct=True;Database=newspaper.db;'
            'encoding="utf-8";'
            'String Types=Unicode')
        cursor = connection.cursor()
        for publication in publications:
            if publication.__class__.__name__ == 'NewsArticle':
                cursor.execute("CREATE TABLE IF NOT EXISTS NewsArticle (article_title varchar(255), article_city varchar(255), article_date date)")
                cursor.execute("INSERT INTO NewsArticle VALUES (?, ?, ?)", (publication.article_title, publication.city, publication.article_date))
                connection.commit()
            elif publication.__class__.__name__ == 'Advertisement':
                cursor.execute("CREATE TABLE IF NOT EXISTS Advertisement (ad_text varchar(255), days_left varchar(255))")
                cursor.execute("INSERT INTO Advertisement VALUES (?, ?)", (publication.ad_text, str(publication.days_left)))
                connection.commit()
            elif publication.__class__.__name__ == 'Horoscope':
                cursor.execute("CREATE TABLE IF NOT EXISTS Horoscope (sign varchar(255), horoscope_text varchar(255))")
                cursor.execute("INSERT INTO Horoscope VALUES (?, ?)", (publication.sign, publication.horoscope_text))
                connection.commit()
            else:
                pass

class SourceFileDecommission:
    @staticmethod
    def delete_source_file(path_to_file):
        if os.path.isfile(path_to_file):
            try:
                os.remove(path_to_file)
            except FileNotFoundError:
                print("There are no file")

Publication_to_print = UserInputSourceOfPublication().request_source_of_publication()

print(Publication_to_print[0])
print(Publication_to_print[1])

PublisherToFile.publish_to_file(Publication_to_print[0])
PublisherToDb.publish_to_db(Publication_to_print[0])
SourceFileDecommission.delete_source_file(Publication_to_print[1])


subprocess.run(["python", "words_and_letters_calculation.py"])
