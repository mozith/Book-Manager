import os
import json
import requests

BOOKS_FILE = "books.json"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file)


def search_book(title_or_isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q={title_or_isbn}"
    response = requests.get(url)
    data = response.json()

    if data["totalItems"] > 0:
        book_info = data["items"][0]["volumeInfo"]
        return {
            "title": book_info["title"],
            "author": ", ".join(book_info["authors"]),
            "description": book_info.get("description", "No description available."),
            "isbn": book_info["industryIdentifiers"][0]["identifier"]
        }
    else:
        return None


def add_book(books):
    title_or_isbn = input("Enter the book title or ISBN: ").strip()
    book = search_book(title_or_isbn)

    if book:
        books.append(book)
        save_books(books)
        print(f"Book '{book['title']}' by {book['author']} added.")
    else:
        print("Book not found. Please try again.")


def remove_book(books):
    title = input("Enter the title of the book you want to remove: ").strip()
    book = next((book for book in books if book["title"].lower() == title.lower()), None)

    if book:
        books.remove(book)
        save_books(books)
        print(f"Book '{book['title']}' by {book['author']} removed.")
    else:
        print("Book not found. Please try again.")


def search_book_in_collection(books):
    title = input("Enter the title of the book you want to search for: ").strip()
    found_books = [book for book in books if title.lower() in book["title].lower()]

    if found_books:
        for book in found_books:
            print(f"{book['title']} by {book['arthur']}")
            print(f"ISBN: {book['isbn']}")
            print(f"Description: {book['descripition']}")
            print()
    else:
        print("No matching books found.")

def main():
    books = load_books()

    while True:
        clear_screen()
        print("Book Manager")
        print("1. List books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            clear_screen()

            list_books(books)
            input("Press Enter to continue...")
        elif choice == "2":
            clear_screen()
            add_book(books)
            input("Press Enter to continue...")
        elif choice == "3":
            clear_screen()
            remove_book(books)
            input("Press Enter to continue...")
        elif choice == "4":
            break
        else:
            input("Invalid choice. Press Enter to continue...")


if __name__ == "__main__":
    main()
