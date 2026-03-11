import csv

def print_menu():
   print('\n**** Address Book ****')
   print('What would you like to do?')
   print(' (A)dd a name')
   print(' (R)emove a name')
   print(' (F)ind a name')
   print(' (Q)uit')

def print_address_book(list_of_dicts, search='', with_indexes=False):
   leader_title = ''
   leader_lines = ''
   if with_indexes:
      leader_title = 'Index '
      leader_lines = '------'
   print(f'{leader_title} {"First Name":^10} {"Last Name":^15} {"Address":^20} {"City":^15} {"State":^6}')
   print(f'{leader_lines} {"-"*10} {"-"*15} {"-"*20} {"-"*15} {"-"*6}')
   
   for index, row in enumerate(list_of_dicts):
      num_string = ''
      if with_indexes:
         num_string = f'{index + 1:6}. '
      
      matches_search = True
      if search:
         search_lower = search.lower()
         if not (search_lower in row["First Name"].lower() or \
         search_lower in row["Last Name"].lower() or \
         search_lower in row["Address"].lower() or \
         search_lower in row["City"].lower() or \
         search_lower in row["State"].lower()):
            matches_search = False
      if matches_search:
         print(f'{num_string} {row["First Name"]:10} {row["Last Name"]:15} {row["Address"]:20} {row["City"]:15} {row["State"]:^6}')

def find_user():
   return input('Enter a search term: ')

def add_user(address_book):
   print('Add a new User:')
   new_user = {}
   new_user["First Name"] = input(' First Name: ')
   new_user["Last Name"] = input('  Last Name: ')
   new_user["Address"] = input('    Address: ')
   new_user["City"] = input('       City: ')
   new_user["State"] = input('      State: ')
   
   address_book.append(new_user)


def remove_user(address_book):
   if not address_book:
      print("No users to remove.")
      return
   
   print_address_book(address_book, with_indexes=True)
   while True:
      try:
         user_input = int(input('Which user would you like to remove? (Enter number) '))
         if user_input < 1 or user_input > len(address_book):
            print("Invalid index. Please try again.")
         else:
            address_book.pop(user_input - 1)
            print("User removed!\n")
            break
      except ValueError:
         print("Please enter a valid number.")

def save_address_book(address_book):
   if not address_book: 
      print("No users to save.")
      return
   with open('address_book.csv', 'w', newline='') as csvout:
      csvwriter = csv.DictWriter(csvout, fieldnames=address_book[0].keys())
      csvwriter.writeheader()
      csvwriter.writerows(address_book)


# Load the address book
# Fields "First Name", "Last Name", "Address", "City", "State"]
address_book = []
try:
   with open('address_book.csv', 'r', newline='') as csvfile:
      csvreader = csv.DictReader(csvfile)
      for row in csvreader:
         address_book.append(row)
except FileNotFoundError:
   print("Address book file not found. Stating with an empty address book.")

search_term = ''

# Application Loop
while True:
   print_address_book(address_book, search=search_term)
   search_term = ''
   print_menu()
   user_input = input().upper()

   if user_input == 'A':
      add_user(address_book)
      print("New user added!\n")
      save_address_book(address_book)
   elif user_input == 'R':
      remove_user(address_book)
      print("User removed! \n")
      save_address_book(address_book)
   elif user_input == 'F':
      search_term = find_user()
   elif user_input == 'Q':
      break