import random

def passwords(input):

    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                       'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                       'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                       'z']
    upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                       'Z']
    symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    combined_list=digit+lower_char+upper_char+symbol
    rand_digit=random.choice(digit)
    rand_lower=random.choice(lower_char)
    rand_upper=random.choice(upper_char)
    rand_symbol=random.choice(symbol)
    temp_pass=rand_digit+rand_lower+rand_upper+rand_symbol
    for i in range(4):
        temp_pass=temp_pass+random.choice(combined_list)
    if input==[]:
        temp_pass = temp_pass + random.choice(combined_list)
        return temp_pass
    else:
        temp_pass = temp_pass + random.choice(combined_list)
        password=random.choice(input)+temp_pass+random.choice(input)
        return password
if __name__ == "__main__":
    user_input=[]
    choice = input("Do you want a personalised password? (y/n):")
    if choice == 'y':
        user_input = input(
            "Enter keyword for personalised password,separated by spaces:").split()
        password = passwords(user_input)
        print(password)
    elif choice=='n':
        password = passwords(user_input)
        print(password)



