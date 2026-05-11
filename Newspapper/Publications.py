import datetime
from datetime import date, datetime

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


class UserInput:
    def request_type_of_publication_from_user(self):
        publication_id = input("Enter publication_id: 1 - for new article, 2 - for new advertisement, 3 - for new horoscope: ")
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

class Publish:
    def publish_to_file(self, text):
        with open('Newspapper.txt', 'a', encoding='utf-8') as f:
            print(text, file=f)


b = UserInput().request_type_of_publication_from_user()

Publish().publish_to_file(b)

