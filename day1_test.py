def main():
    name = input("Как тебя зовут? ")

    # проверка пустого имени
    while name.strip() == "":
        name = input("Имя не может быть пустым. Введи снова: ")

    goal = input("Зачем ты изучаешь AI? ")

    print(f"\n{name}, отличный выбор!")
    print(f"Цель: {goal}")
    print(f"Длина цели: {len(goal)} символов")
    print("Ты начал путь AI разработчика 🚀")


if __name__ == "__main__":
    main()