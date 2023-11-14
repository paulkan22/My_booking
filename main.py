import requests

# Данные для броинроания (Имя,Фамилия,цена,даты,статус депозита)
booking_data = {
    "firstname": "Pavel",

    "lastname": "Kanunnikov",

    "totalprice": 200,

    "depositpaid": True,

    "bookingdates": {
        "checkin": "2023-01-15",

        "checkout": "2023-01-20"
    },
    "additionalneeds": "Breakfast"
}
#отправляет данные с помощью метода post. В случае успеха получаем 200
response = requests.post("https://restful-booker.herokuapp.com/booking", json=booking_data)
print(response)
booking_id = response.json()["bookingid"]

# Данные которые хотим поменять
updated_booking_data = {
    "bookingdates": {

        "checkin": "2023-01-18",

        "checkout": "2023-01-25"
    }
}
#используем метод put для обновления данных(подмена записей)
requests.put(f"https://restful-booker.herokuapp.com/booking/{booking_id}", json=updated_booking_data)

# Распечатать информацию о бронировании
info_response = requests.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")
print("Информация о бронировании:")
print(info_response.json())

# Удалить бронь
delete_booking = requests.delete(f"https://restful-booker.herokuapp.com/booking/1{booking_id}")

# Убедиться, что бронь удалена
check_booking = requests.get(f"https://restful-booker.herokuapp.com/booking/1{booking_id}")
#Делаем проверку , мы ожидаем получть 404.
if check_booking.status_code == 404:
    print("Бронрование удалено")
else:
    print("Не удалось бронирование")