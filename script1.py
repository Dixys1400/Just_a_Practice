class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        """Добавить книгу в библиотеку."""
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Книга '{title}' добавлена в библиотеку.")

    def remove_book(self, title):
        """Удалить книгу по названию."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга '{title}' удалена из библиотеки.")
                return
        print(f"Книга '{title}' не найдена.")

    def show_books(self):
        """Вывести информацию о всех книгах в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("Список книг в библиотеке:")
            for book in self.books:
                print(book)

def main():
    library = Library()

    while True:
        print("\nДоступные действия:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Показать все книги")
        print("4. Выйти")

        action = input("Выберите действие (1-4): ")

        if action == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            try:
                year = int(year)  # Преобразуем год в число
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: год должен быть числом.")
        elif action == "2":
            title = input("Введите название книги, которую хотите удалить: ")
            library.remove_book(title)
        elif action == "3":
            library.show_books()
        elif action == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 4.")

if __name__ == "__main__":
    main()

