import sqlite3 
from tkinter import * 
 
# Подключение к базе данных или создание новой, если ее нет 
conn = sqlite3.connect('flight_booking.db') 
cursor = conn.cursor() 
 
# Создание таблицы Flights, если она не существует 
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Flights ( 
    flight_number INT PRIMARY KEY, 
    aircraft_type TEXT, 
    departure_datetime TEXT, 
    economy_seats INT, 
    business_seats INT, 
    first_class_seats INT, 
    economy_price DECIMAL(10, 2), 
    business_price DECIMAL(10, 2), 
    first_class_price DECIMAL(10, 2) 
) 
''') 
 
# Добавление данных о рейсе 
cursor.execute(''' 
INSERT OR REPLACE INTO Flights (flight_number, aircraft_type, departure_datetime, economy_seats, business_seats, first_class_seats, economy_price, business_price, first_class_price) 
VALUES (101, 'Boeing 737', '2022-12-31 08:00:00', 100, 20, 10, 200.00, 400.00, 600.00) 
''') 
 
conn.commit() 
 
# Добавление нового рейса 
def add_flight(): 
    flight_info = [entry.get() for entry in entries] 
    cursor.execute(''' 
    INSERT INTO Flights (flight_number, aircraft_type, departure_datetime, economy_seats, business_seats, first_class_seats, economy_price, business_price, first_class_price) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) 
    ''', flight_info) 
    conn.commit() 
 
# Просмотр данных о рейсах 
def view_flights(): 
    cursor.execute('SELECT * FROM Flights') 
    flights = cursor.fetchall() 
    for flight in flights: 
        print(flight) 
 
# Создание графического интерфейса 
root = Tk() 
root.title("АвиаКасса Аня") 
 
labels = [ 
    "Номер рейса:", 
    "Тип самолета:", 
    "Дата и время вылета:", 
    "Кол-во мест эконом класса:", 
    "Кол-во мест бизнес класса:", 
    "Кол-во мест первый класс:", 
    "Стоимость билета эконом класса:", 
    "Стоимость билета бизнес класса:", 
    "Стоимость билета первый класс:" 
] 
 
entries = [] 
 
for label_text in labels: 
    label = Label(root, text=label_text) 
    label.pack() 
    entry = Entry(root) 
    entry.pack() 
    entries.append(entry) 
 
button_add_flight = Button(root, text="Добавить рейс", command=add_flight) 
button_add_flight.pack() 
 
button_view_flights = Button(root, text="Просмотр рейсов", command=view_flights) 
button_view_flights.pack() 
 
root.mainloop() 
 

conn.close()