# DEBUGGING ASSIGNMENT

# Line 34 is missing a quotation at the end of the formatted string
# Line 28 need to put a space between Last and Name 
# Line 23 Adust index to start from 1 for user by adding a + 1:
# Under line 26 add  search_lower = search.lower()   to make the search case-insensitive
#        which also means you'll need to change all the "search" variables underneath that to "search_lower"
# The remove_user function on line 52 needs to be changed to ensure the address book isn't empty 
#        because the csv.DictWriter would fail if there are no fieldnames to write.
# In the save_address_book function I added an if statement to ensure there are actually users to save
# Added a try and except after the address_book variable list address_book = [] so that you can load the list
#       even if it's empty and it will tell the user it is empty.
# After user_input = input() down on line 98 now  I added a .upper() to allow it to be case-insensitive
# The 'q' in the second to last line needs to be an upper case Q due to the .upper() I added
# The find user function is printing 'Enter search term:' and allowing the user to enter something, but
#       it's not returning any results back to the user. So we needed to add some code for their search
#       results to be returned to them. One thing I added was the .lower() after First Name, Last Name,
#       Address, City and State (under the matches_search=True)



# **********************BUG_REPORT****************************************
# 1. What? What happened while using the application. What was the manifestation of the error?
# 2. How? How did we uncover this issue? What were the steps to reproduce the error?
# 3. Where? Exactly where in the application did we find the bug? Which page? Which action? Which server or application version?

# 1. Bug ID: address-book
# 2. Bug Summary/Description: When user inputs 'A', 'R', or 'F' nothing happens
# 3. Bug Details: VS Code
# 4. Bug Severity: critical
# 5. Steps to Reproduce: In the debug_address_book.py file, run the code. When it prompts you for an input try
#           'A', 'R', or 'F'. It will print the current address book, but will not give you an option to add,
#           remove, or find anything in the address book, as expected that it would.



# 1. Bug ID: address-book
# 2. Bug Summary/Description: Space needed between 2 words
# 3. Bug Details: VS Code
# 4. Bug Severity: low
# 5. Steps to Reproduce: In the debug_address_book.py file, navigate to line 28, it's in the print_address_function.
#           search in row["LastName"] or \    a space is needed between Last and Name
