import datetime
import os
# os.getcwd()

class library:
    """
    This class is used to keep records of books library.
    It has total four modules: 'Display Books', 'Lend Books', 'Add Books', 'Return Books'
    'list_of_books' should be txt file. 'library_name' should be string.
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Isbn = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(Isbn):{'books_title':line.replace("\n",""),'lender_name':'','lend_date':'', 'status':'Available'}})
            Isbn += 1    

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books Isbn","\t", "Title")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t", value.get("books_title"), "- [", value.get("status"),"]")

    def Issue_books(self):
        books_Isbn = input("Enter Books Isbn : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_Isbn in self.books_dict.keys():
            if not self.books_dict[books_Isbn]['status'] == 'Available':
                print(f"This book is already issued to {self.books_dict[books_Isbn]['lender_name']} on {self.books_dict[books_Isbn]['lend_date']}")
                return self.lend_books()
            elif self.books_dict[books_Isbn]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_Isbn]['lender_name'] = your_name
                self.books_dict[books_Isbn]['lend_date'] = current_date
                self.books_dict[books_Isbn]['status']= 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book Isbn Not Found !!!")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter Books Title : ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 20:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','lend_date':'', 'status':'Available'}})
            print(f"The books '{new_books}' has been added successfully !!!")

    def return_books(self):
        books_Isbn = input("Enter Books Isbn : ")
        if books_Isbn in self.books_dict.keys():
            if self.books_dict[books_Isbn]['status'] == 'Available':
                print("This book is already available in library. Please check book Isbn. !!! ")
                return self.return_books()
            elif not self.books_dict[books_Isbn]['status'] == 'Available':
                self.books_dict[books_Isbn]['lender_name'] = ''
                self.books_dict[books_Isbn]['lend_date'] = ''
                self.books_dict[books_Isbn]['status']= 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book Isbn Not Found !!!")

if __name__ == "__main__":
    try:
        mylms = library("list_of_books.txt", "Python's")
        press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}    
        
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.Issue_books()
                
            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books()
            
            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")
