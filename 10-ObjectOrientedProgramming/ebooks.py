class EBook:
    def __init__(self, title, author, num_of_pages):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def status(self):
        if self.is_open:
            print(f"You are reading '{self.title}' by {self.author}.")
            print(f"The book has {self.num_of_pages} pages, and you are currently on page {self.current_page}.")
        else:
            print("The book is closed.")

    def next_page(self,num):
        if self.is_open==False:
           print("The book is closed")
        elif self.is_open and self.current_page<self.num_of_pages:
            self.current_page+=num
            print(f"You're on the {self.current_page} page")
        else:
            print("You have reached the end of the book")
    def previous_page(self,num):
        if self.is_open==False:
            print("The book is closed")
        elif self.is_open and self.current_page>self.num_of_pages:
            self.current_page-=num
            print(f"You're on the {self.current_page} page")
        else:
            print("You have reached the beginning of the book")



