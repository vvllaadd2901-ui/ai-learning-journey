def main():
    # ввод текста
    text = input("Вставь текст для анализа:\n")

    # убираем знаки препинания
    text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")

    # разбиваем текст на слова
    words = text.split()

    # количество слов
    print(f"\nКоличество слов: {len(words)}")

    # уникальные слова
    unique_words = set(words)
    print(f"Уникальных слов: {len(unique_words)}")

    # подсчёт частоты слов
    word_count = {}

    for word in words:
        word = word.lower()  # приводим к нижнему регистру
        word_count[word] = word_count.get(word, 0) + 1

    # самое частое слово
    most_common = max(word_count, key=word_count.get)
    print(f"Самое частое слово: {most_common}")

    # ТОП-3 слова
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print("\nТоп 3 слова:")
    for word, count in sorted_words[:3]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()