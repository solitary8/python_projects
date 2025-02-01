def welcome():
    print("Welcome to the library !")
    print("Here is your choice of activities :")
    print("1. Return a book")
    print("2.Search a book")
    print("3. Take out a book")
    print("4. Leave")
    choice = int(input("Enter your choice :"))
    
class Book:
    def __init__(self):
        self.is_lent = False
        self.book_dict = {
            "Harry Potter 1" :{"author" : "J.K Rowling","is_lent" : False}
        }

    def add_book(self, author, title):
        if title in self.book_dict:
            print("Sorry this book is already in the library !")
        else:
            self.book_dict[title] = {"author" : author, "is_lent" : False}
            print(f"{title} by {author} has been added to the library !")
        
    def lend_book(self, title):
            if title in self.book_dict:
                print("Your book has been found !")
                if self.book_dict[title]["is_lent"] == False:
                    print("Done ! You can now take this book out and enjoy !")
                    self.book_dict[title]["is_lent"] = True
                else:
                    print("Sorry ! This book is already lent out, please come back later.")
class Library(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
test = Book()