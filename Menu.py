def RLE(message):
    final_string = ''
    previous_character = ''
    count = 0
    length = len(message)
    for i in range(0,length):
        character =  message[i]
        if character == previous_character:
            count = count + 1
        else:
            if previous_character:
                final_string += previous_character + str(count)
            count = 1
            previous_character = character
    final_string += previous_character + str(count)
    print("Encoded message is:",final_string)


def prime_numbers(number):
    flag = True
    for i in range(2,number//2):
        if number % i == 0:
            flag = False
    if flag == False:
        print(number,"is not a prime number")
    elif flag == True:
        print(number,"is a prime number")

def subset(word1,word2):
    length = len(word2)
    final_string = ''
    message_before = word1
    for i in range(0,length):
        character = word2[i]
        if character in word1:
            word1 = word1.replace(character,'',1)
            final_string += character
    if len(final_string) == len(message_before):
        print(message_before,"can be made using character from",word2)
    else:
        print(message_before,"cannot be made using characters from",word2)

def denary_conversion(denary_value):
    number = denary_value
    final_string = ''
    while number != 0:
        if number % 2 == 0:
            final_string += '0'
            number = number // 2
        elif number % 2 == 1:
            final_string += '1'
            number = number // 2
    final_string = final_string[::-1]
    print(denary_value,"converted to binary is",final_string)
    

def mode(number1,number2):
    try:
        import statistics
        list_numbers = []
        for i in range(0,number1):
            list_numbers.append(number2[i])
        modal_value = statistics.mode(list_numbers)
        mode_string = str(modal_value)
        list_string = str(list_numbers)
        final_count = list_string.count(mode_string)
        print("Modal value of",modal_value,"occurs",final_count,"times")
    except:
        print("Data was multimodal")

def menu():
    print("""--------------------------------------------------------------------------------
             Enter 1 for RLE
             Enter 2 for Prime Numbers
             Enter 3 for Subset
             Enter 4 for Denary Conversion
             Enter 5 for Mode
             Enter 6 for Quit Function
--------------------------------------------------------------------------------""")
    print('\n')
    
    user_input = int(input("Please select the menu option you would like: "))
    if user_input == 1:
        user_input_RLE = input("\nPlease enter the message you would like encoded: ")
        RLE(user_input_RLE)
    elif user_input == 2:
        user_input_prime = int(input("\nPlease enter your number: "))
        prime_numbers(user_input_prime)
    elif user_input == 3:
        user_input_subset_1 = input("\nPlease enter the first word: ")
        user_input_subset_2 = input("\nPlease enter the second word: ")
        subset(user_input_subset_1,user_input_subset_2)
    elif user_input == 4:
        user_input_denary = int(input("\nPlease enter the denary number to be converted: "))
        denary_conversion(user_input_denary)
    elif user_input == 5:
        user_input_mode_1 = int(input("\nPlease enter the number of digits you would like to enter: "))
        user_input_mode_2 = str(input("\nPlease enter the string of digits: "))
        mode(user_input_mode_1,user_input_mode_2)
    elif user_input == 6:
        quit()

menu()
