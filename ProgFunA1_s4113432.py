# RMIT Book Rental System Assingment 1
# Defining Discount
DISCOUNT = 0.1

# List of customers
customers = [{'name': 'Emily', 'member': True},{'name':'James', 'member':False}]

# List of books with following  data in dictionary
list_of_books = [
    {
        "category": "Fantasy",
        "type": "rental",
        "books": ["Harry Potter", "The Hobbit"],
        "rent": [0.5, 0.4],
    },
    {
        "category": "Crime",
        "type": "rental",
        "books": ["Gone Girl", "Sherlock Holmes 1 "],
        "rent": [0.5, 0.4],
    },
    {
        "category": "Classics",
        "type": "rental",
        "books": ["Pride and Prejudice"],
        "rent": [0.3, 0.25],
    },
    {
        "category": "Modern Classics",
        "type": "rental",
        "books": ["To Kill a Mockingbird"],
        "rent": [0.4, 0.3],
    },
    {
        "category": "History",
        "type": "rental",
        "books": ["The Diary of a Young Girl"],
        "rent": [0.4, 0.3],
    },
    {
        "category": "Philosophy",
        "type": "rental",
        "books": ["The Republic"],
        "rent": [0.3, 0.25],
    },
    {
        "category": "Science",
        "type": "rental",
        "books": ["A Brief History of Time"],
        "rent": [0.5, 0.4],
    },
    {
        "category": "Textbooks",
        "type": "reference",
        "books": ["Introduction to the Theory of Computation"],
        "rent": [0.75, 0.6],
    },
    {
        "category": "Art",
        "type": "rental",
        "books": ["The Story of Art"],
        "rent": [0.5, 0.4],
    },
    {
        "category": "Other",
        "type": "reference",
        "books": ["Thinking Fast and Slow", "Atomic Habits"],
        "rent": [0.5, 0.4],
    },
]

books_to_rent = []

# validate if the input string contains only alphabets
def validate_input(name):
    if isinstance(name, str) and name.replace(" ", "").isalpha():
        return True
    return False

# validate if the book name is in the list of books
def validate_book(entered_book):
    found_book = [book for book in list_of_books if entered_book in book['books']]
    return found_book[0] if len(found_book) > 0 else []

# validate if the number of days is valid
def validate_days(days, bookset):
    if bool(isinstance(days, int) and days > 0):
        if(bookset['type'] == 'reference' and days > 14):
            print('Cannot Rent this book for more than 14 days')
            return False
        return True
    return False

# Print the receipt for the rented books
def print_reciept(name, books_to_rent, is_member):
    gross_total_amount = 0
    gross_final_amount = 0
    print("-"*80)
    print(f"Receipt for {name} ")
    print("-" * 80)
    print("Books Rented")
    for book in books_to_rent:
        print(f"\t-  {book['name']} for {book['days']} days ({book['total_amount']/book['days']} AUD/day)")
        gross_total_amount += book['total_amount']
        gross_final_amount += book['final_amount']
    print("-"*80)
    print(f"Original cost:             {gross_total_amount:.2f} (AUD) ")
    if is_member:
        print(f"Discount:                  {(gross_total_amount * DISCOUNT):.2f} (AUD) ")
    else:
        print(f"Discount:                   0.00 (AUD) ")
    print(f"Total cost:                {gross_final_amount:.2f} (AUD) ")
    print("-"*80)

# Function to enter customer name and validate it
def enter_customer_name():
    # Inputting Name
    print("Please Enter your Name: ")
    name = input().strip()

    while not validate_input(name):
        print("Invalid Name. Please Enter valid name(use Alphabets only): ")
        name = input().strip()
    return name

# Function to rent a book
def rent_a_book(name):
    # Inputting Book Name
    print("Enter the name of the book you want to rent: ")
    book = input().strip()
    found_bookset = validate_book(book)
    while not len(found_bookset) > 0:
        print("Invalid Book Name. Please Enter valid name(use Alphabets only): ")
        book = input().strip()
        found_bookset = validate_book(book)

    # Inputting Days to rent
    print("Enter the number of days you want to rent the book for:")
    try:
        days = int(input().strip())
    except:
        print("Invalid Days(use numbers only)")
    finally:
        while not validate_days(days, found_bookset):
            print("Invalid Input. Please Enter a valid number of days:")
            days = int(input().strip())
    # Calculating total amount based on days to rent
    total_amount = 0
    if(days <= 10):        
        total_amount = days * found_bookset['rent'][0]
    else:        
        total_amount = days * found_bookset["rent"][1]

    # Calculating discount and printing final output
    final_amount = 0 
    memberFlag = False
    if name in [customer['name'] for customer in customers] and [customer['member'] for customer in customers if customer['name'] == name][0]:
        final_amount = total_amount * (1 - DISCOUNT)
        memberFlag = True
    else:
        final_amount = total_amount
    global books_to_rent
    books_to_rent.append({'name':book, 'days': days, 'total_amount': total_amount, 'final_amount': final_amount})
    # Ask user if they want to rent another book
    print("Do you want to rent another book? YES(y)/NO(n): ")
    another_book = input().strip().lower()
    while another_book not in ['y', 'n']:
        print("Invalid Input. Please Enter valid choice(y/n):")
        another_book = input().strip().lower()
    if another_book == 'y':
            rent_a_book(name)
    elif another_book == 'n':
        for customer in customers:
            if customer['name'] == name:                
                if 'rentals' in customer.keys():                    
                    customer['rentals'].append(books_to_rent)
                else:
                    customer['rentals'] = [books_to_rent]
        print_reciept(name,books_to_rent, memberFlag)  
        if name not in [customer['name'] for customer in customers]:
            print('Do you wish to become a member Yes/No: ')
            wannabeMember = input()
            customers.append({'name': name, 'member': True if wannabeMember.lower() == 'yes' else False, 'rentals': [books_to_rent]})
    books_to_rent = []      

# Function to update book category
def update_book_category():
    validated = False
    while not validated:
        print("enter updated data as category, type, rent1, rent2")
        inp = input().strip()
        category, type, rent1, rent2 = inp.strip().split(',')
        if category.strip() not in [book['category'] for book in list_of_books]:
            print("Invalid Input. Please Enter a valid category:")
        elif type.strip().lower() not in ["rental", "reference"]:
            print("Type of Book is not recognised! Try Again.")
        else:
            try:
                float(rent1)
                float(rent2)
            except ValueError:
                print("Rent must be a floating number!")
            else:
                validated = True
                
    for book in list_of_books:
        if book['category'] == category:
            book['type'] = type.strip().lower()
            book['rent'] = [float(rent1), float(rent2)]
            print('Updated!')
            break


def update_books():
    inp = ''
    while inp.strip().lower() not in ['a','r']:
        print("Do you want to add(A) or remove(R) a book (a/r): ")
        inp = input().strip()
        if(inp.strip().lower() not in ['a','r']):
            print("Wrong input, enter either a or r")
    print("Enter book category, list of books(book1, book2): ")
    inputs = input().strip().split(',')
    inputs = [value.strip() for value in inputs]
    category, booksList = inputs[0], inputs[1:]
    if inp.lower() == 'a':
        not_new_books = []
        for book in list_of_books:
            if book['category'] == category:
                for new_book in booksList:
                    if new_book in book['books']:
                        not_new_books.append(new_book)                
                if len(not_new_books) > 0:
                    print('Following books will not be added as they are already in Stock')
                    for nnb in not_new_books:
                        print(f'\t- {nnb}')
                booksList = [bk for bk in booksList if bk not in not_new_books]                    
                book['books'].extend(booksList)
                print('Added new books!')
                break
    elif inp.lower() == 'r':
        for book in list_of_books:
            if book['category'] == category:
                for b in booksList:
                    if b not in book['books']:
                        print(f'{b} don\'t exist in the stock.')
                book['books'] = [b for b in book['books'] if b not in booksList]
                print('Removed!')
                break

def display_customers():
    print(f'{"Name":<20}{"Membership":<15}')
    print("-"*50)
    for customer in customers:
        print(f'{customer["name"]:<20}{customer["member"]:<15}')
    print("-"*50+"\n\n")

def display_book_categories():
    print(f"{'Category':<20} {'Type':<15} {'Books':<50} {'Rent'}")
    print("-"*100)
    for book in list_of_books:
        category = book['category']
        book_type = book['type']
        books = ", ".join(book['books'])
        rent = ",".join([str(r) for r in book['rent']])
        print(f"{category:<20} {book_type:<15} {books:<50} {rent}")    
    print("-"*100+"\n\n")

def display_most_valuable_customer():
    most_valuable_customer = None
    max_rent = 0
    for customer in customers:
        if 'rentals' in customer.keys():  
            total_rent = 0       
            for rental in customer['rentals']:   
                total_rent = sum([book['final_amount'] for book in rental])
            if total_rent > max_rent:
                max_rent = total_rent
                most_valuable_customer = customer['name']
    if most_valuable_customer:
        print(f"Most valuable customer is {most_valuable_customer} with a total rent of {max_rent:.2f} AUD")
    else:
        print("No rentals found.")

def display_customer_rental_history():
    name = enter_customer_name()
    for customer in customers:
        if customer['name'].lower() == name.strip().lower():
            if 'rentals' in customer.keys():
                print(f"\nRental history for {name}:")
                print("-" * 120)
                print(f"{'Rental #':<10} {'Books Rented':<70} {'Total Amount':<15} {'Discount':<15} {'Final Amount':<15}")
                print("-" * 120)
                for index, rental in enumerate(customer['rentals']):
                    rental_books_info = ", ".join([f"{book['name']} | {book['days']} days" for book in rental])
                    total_amount = sum([book['total_amount'] for book in rental])
                    discount = sum([(book['total_amount'] - book['final_amount']) for book in rental])
                    final_amount = sum([book['final_amount'] for book in rental])

                    print(f"{index + 1:<10} {rental_books_info:<70} {f"{total_amount:.2f} AUD":<15} {f"{discount:.2f} AUD":<15} {f"{final_amount:.2f} AUD":<15}")
                    print("-" * 120)
            else:
                print(f"No rentals found for {name}.")
            break
    else:
        print(f"{name} not found.")


def menu():
    print('Welcome to RMIT book Rental System')
    print()
    print("#######################################")
    print("You can choose from following options: ")
    print("1. Rent a book")
    print("2. Update information of a book category")
    print("3. Update books of a book category")
    print("4. Display existing customer")
    print("5. Display existing book categories")
    print("6. Display the most valueable customer")
    print("7. Display a customer rental history")
    print("8. Exit")
    print("#######################################")
    print()

    choice = 0
    while choice not in range(1, 8):
        try:
            choice = int(input("Please select an option: "))
            if choice > 8 or choice < 1:
                print("Invalid choice. Please try again.")
        except ValueError:
            print('Invalid Input. Please Enter a valid number')

    if choice == 1:
        name = enter_customer_name()
        rent_a_book(name)
    elif choice == 2:
        update_book_category()
    elif choice == 3: 
        update_books()
    elif choice == 4: 
        display_customers()
    elif choice == 5:
        display_book_categories()
    elif choice == 6:
        display_most_valuable_customer()
    elif choice == 7:
        display_customer_rental_history()
    elif choice == 8:
        print("Goodbye!")
        exit()

# Main program loop
while True:
    menu()
