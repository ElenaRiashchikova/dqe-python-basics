from datetime import datetime
import pyodbc
from geopy.distance import geodesic as GD

connection = pyodbc.connect(
    'Driver={SQLite3 ODBC Driver};'
    'Direct=True;Database=city_coordinates.db;'
    'encoding="utf-8";'
    'String Types=Unicode')
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS CityCoordinates (city_name varchar(255), city_latitude float, city_longitude float, add_date datetime)")
connection.commit()

class City:
    def __init__(self, city_name, city_latitude, city_longitude):
        self.city_name = city_name
        self.city_latitude = city_latitude
        self.city_longitude = city_longitude

class CityInput:
    @staticmethod
    def provide_city_by_input_for_calculation():
        cities_list:list = []
        runs = 2
        for run in range(0, runs):
            city_name = input("Provide city: ")
            if CityInfoInDb.select_city_from_db(city_name) is not None:
                cities_list.append(CityInfoInDb.select_city_from_db(city_name))
            else:
                city_latitude = input("Provide city latitude: ")
                city_longitude = input("Provide city longitude: ")
                city_data = City(city_name, city_latitude, city_longitude)
                CityInfoInDb.insert_city_in_db(city_data)
                cities_list.append(city_data)
        return cities_list


class CityInfoInDb:
    @staticmethod
    def select_city_from_db(city_name):
        cursor = connection.cursor()
        cursor.execute("SELECT city_name, city_latitude, city_longitude FROM CityCoordinates WHERE city_name = ?",
                       city_name)
        connection.commit()
        city_data = cursor.fetchone()
        return City(city_data.city_name, city_data.city_latitude, city_data.city_longitude)

    @staticmethod
    def insert_city_in_db(city_data):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO CityCoordinates VALUES (?, ?, ?, ?)",
                       (city_data.city_name, city_data.city_latitude , city_data.city_longitude, datetime.now()))
        connection.commit()

class DistanceCalculator:
    @staticmethod
    def calculate_distance_between_cities(cities_list):
        city1 = (cities_list[0].city_latitude, cities_list[0].city_longitude)
        city2 = (cities_list[1].city_latitude, cities_list[1].city_longitude)
        print("Distance between", cities_list[0].city_name, "and", cities_list[1].city_name, "is", GD(city1, city2))


DistanceCalculator().calculate_distance_between_cities(CityInput.provide_city_by_input_for_calculation())


