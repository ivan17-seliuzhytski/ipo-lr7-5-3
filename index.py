import json
def get():
	with open('cities.json', 'r', encoding='utf-8') as file:
			data = json.load(file)
			for city in data:
				print(f"№: {city['id']}")
				print(f"Название: {city['name']}")
				print(f"Страна: {city['country']}")
				print(f"Является ли большим(>100k): {city['is_big']}")
				print(f"Численность населения: {city['people_count']}")
			
def get_id():
	id_find = input("Введите id записи, по которой хотите сделать вывод информации: \n")
	with open('cities.json', 'r', encoding='utf-8') as file:
		data = json.load(file)
		found = False
		for city in data:
			if city['id'] == id_find:
				print(f"\n=============== Найдено ===============")
				print(f"№: {city['id']}")
				print(f"Название: {city['name']}")
				print(f"Страна: {city['country']}")
				print(f"Является ли большим(>100k): {city['is_big']}")
				print(f"Численность населения: {city['people_count']}")
				found = True
				break
		if not found:
			print(f"\n=============== Не найдено ===============")

def add():
	new_id = input("Введите номер записи: \n")
	new_name = input("Введите название города: \n")
	new_country = input("Введите страны города: \n")
	new_is_big = input("Введите является ли большим(>100k): \n")=="True"
	new_people_count = int(input("Введите численность населения города: \n"))
	new_city={
		"id": new_id,
		"name": new_name,
		"country": new_country,
		"is_big": new_is_big,
		"people_count": new_people_count}
	with open('cities.json', 'r+', encoding='utf-8') as file:
		data = json.load(file)
		data.append(new_city)
		file.seek(0)
		json.dump(data, file, ensure_ascii=False, indent=4)

def delete():
	findtodeletе = input("Введите номер записи которую вы хотите удалить: ")
	with open('cities.json', 'r+', encoding='utf-8') as file:
		data = json.load(file)
		found = False
		for city in data:
			if city['id'] == findtodeletе:
				print(f"\n=============== Найдено ===============")
				print(f"№: {city['id']}")
				print(f"Название: {city['name']}")
				print(f"Страна: {city['country']}")
				print(f"Является ли большим(>100k): {city['is_big']}")
				print(f"Численность населения: {city['people_count']}")
				proverka = input("Введите на русском языке 'да' если всё еще хотите удалить данный город: ")
				if proverka == "ДА" or "да" or "Да" or "Да!" or "ДА!" or "да!":
					data.remove(city)
					found = True
					break
		if not found:
			print("\n=============== Не найдено ===============")
		else:
			file.seek(0)
			file.truncate()
			json.dump(data, file, ensure_ascii=False, indent=4)

def main():
	kolvo_fun=0
	while True:
		print("\nМЕНЮ:")
		print("1. Вывести все записи")
		print("2. Вывести запись по id города")
		print("3. Добавить запись города")
		print("4. Удалить запись по id города")
		print("5. Выйти из программы")
		choice = input("\nВыберите пункт из предложенного МЕНЮ выше: \n")
		if choice =='1':	
			get()
			kolvo_fun+=1
		elif choice == '2':
			get_id()
			kolvo_fun+=1
		elif choice == '3':
			add()
			kolvo_fun+=1
		elif  choice =="4":
			delete()
			kolvo_fun+=1 
		elif choice =="5":
			print(f"\nВсего выполненных операций с записями: {kolvo_fun}")
			break
		else:
			print("Неправильный ввод, попробуйте снова.")
			
if __name__ == "__main__":
    main()