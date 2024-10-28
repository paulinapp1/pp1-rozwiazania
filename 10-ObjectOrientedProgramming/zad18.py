from ebooks import EBook
my_book=EBook("Harry Potter", "J.K Rowling", 1000)
my_book.open()
my_book.status()
my_book.next_page(5)
my_book.status()
my_book.close()
my_book.next_page(15)

