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

def update_book_info(books):
    title = input("Enter the title of the book you want to update: ").strip()
    book = next((book for book in books if book['title'].lower() == title.lower()), None)
     if book:
        new_title = input(f"Enter the new title (current: {book['title']}): ").strip()
        new_author = input(f"Enter the new author (current: {book['author']}): ").strip()
        new_description = input(f"Enter the new description (current: {book['description']}): ").strip()
        new_isbn = input(f"Enter the new ISBN (current: {book['isbn']}): ").strip()

    if new_title:
        book['title'] = new_title
    if new_author:
        book['author'] = new_author
    if new_description:
        book['description'] = new_description
    if new_isbn:
        book['isbn'] = new_isbn

    save_books(books)
    print("Book details updated successfully!")
else:
print("Book not found. Please try again")

def list_books(books, start_index = 0):
    end_index = start_index + BOOKS_PER_PAGE
    displayed_books = start_index + BOOKS_PER_PAGE
    for idx, books in enumerate(displayed_books, start = start_index + 1):
        print(f"{idx}. {book['title']} by {book['author']}")
        
    return len(displayed_books)
         

def main():
    books = load_books()

    while True:
        clear_screen()
        print("Book Manager")
        print("1. List books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Search for book in collection")
        print("5. Update book information")
        print("6. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_index = 0
            while True:
                clear_screen()
                displayed_count = list_books(books, start_index = start_index)
                if displayed_count == BOOKS_PER_PAGE and input("Next page? (Y/N)").lower() == 'y':
                    start_index += BOOKS_PER_PAGE
                else:
                    break

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
            clear_screen()
            search_book_in_collection(books)
            input("Press Enter to continue...")
        elif choice == "5":
            clear_screen()
            update_book_info(books)
            input("Press Enter to continue...")
        elif choice == "6":
            break
            
        else:
            input("Invalid choice. Press Enter to continue...")


if __name__ == "__main__":
    main()
