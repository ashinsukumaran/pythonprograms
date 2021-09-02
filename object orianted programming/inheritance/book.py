class Book:
    def __init__(self,Library_name, book_name, author, pages):
        self.Library_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def print(self):
        print(self.Library_name)
        print(self.book_name)
        print(self.author)
        print(self.pages)
b=Book("elysium","ab","bc","2")
b.print()