class Library:
    
    def __init__(self):
        self.noBook = 0
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        self.noBook = len(self.books)

    def ShowInfo(self):
        print(f"The library has {self.noBook} books. The books are")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Bhagavat Gtta")
l1.addBook("Bhagavat Gtt2")
l1.addBook("Bhagavat Gtt3")
l1.addBook("Bhagavat Gtt4")
l1.ShowInfo()