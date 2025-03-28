# Part 1
# Defining different Rent Prices
RENT1 = 0.5
RENT2 = 0.4
# Defining Discount
DISCOUNT = 0.1

# List of customers
customers = [{'name': 'Emily', 'member': True},{'name':'James', 'member':False}]

# List of Books
books = [
    {
        "name": "Programming FUndamentals",
        "price": 10,
        "rented": False,
    },
    {
        "name": "Pythonn",
        "price": 10,
        "rented": False,
    },
]

# Inputting Name
print("Please Enter your Name: ")
name = input()

# Inputting Book Name
print("Enter the name of the book you want to rent: ")
book = input()

# Inputting Days to rent
print("Enter the number of days you want to rent the book for:")
days = int(input())

# Calculating total amount based on days to rent
total_amount = 0
if(days <= 10):
    total_amount = days * RENT1
else:
    total_amount = days * RENT2

# Calculating discount and printing final output
final_amount = 0 
if name in [customer['name'] for customer in customers] and [customer['member'] for customer in customers if customer['name'] == name][0]:
    final_amount = total_amount * (1 - DISCOUNT)
    print("------------------------------------------------------------------------------------------ ")
    print(f"Receipt for {name} ")
    print("------------------------------------------------------------------------------------------ ")
    print(f"Books rented: -  {book} for {days} days ({total_amount/days} AUD/day)")
    print("------------------------------------------------------------------------------------------ ")
    print(f"Original cost:             {total_amount} (AUD) ")
    print(f"Discount:                  {total_amount * (DISCOUNT)} (AUD) ")
    print(f"Total cost:                {final_amount} (AUD) ")
else:
    final_amount = total_amount
    print("------------------------------------------------------------------------------------------ ")
    print(f"Books rented: -  {book} for {days} days ({total_amount/days} AUD/day)")
    print("------------------------------------------------------------------------------------------ ")
    print(f"Original cost:              {total_amount} (AUD) ")
    print(f"Discount:                   0 (AUD) ")
    print(f"Total cost::                {final_amount} (AUD/day) ")
    print("------------------------------------------------------------------------------------------ ")