class Book:
    def main(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def print(self):
        print(self.library_name)
        print(self.book_name)
        print(self.author)
        print(self.pages)
obj=Book()
obj.main("kerala university library","alchemist","paulo coelho",546)
obj.print()
