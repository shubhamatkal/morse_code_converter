#imports
from morse_code import morse_code_dict

def morse_code_user_decision():
    dictionary = morse_code_dict
    user_decision = input("What you want to perform ? Encode or Decode? type E or D \n")


    if str.upper(user_decision) == "E":
        text_input = input("write text \n")
        capitalized_text = str.upper(text_input)
        letters_list = [letter for letter in capitalized_text]
        encoded_list = []

        for letter in letters_list:
            if letter in dictionary:
                encoded_list.append(dictionary[letter])
            else:
                print("You type something which is not in our database or which cant be encoded, "
                      "morse code cannot encode any emoji, svg etc")
                a = input("Do you want to try again ? type Y if u want to exit type EXIT")
                if a == "EXIT":
                    print("thank you ! hope when you use this program next time we could encode your inputs")
                elif a == "Y":
                    morse_code_user_decision()
                break
        encoded_text = " ".join(encoded_list)
        print(f"your encoded text in morse code is: {encoded_text}")


    elif str.upper(user_decision) == "D":
        print("this functionality is not yet been create in this project")
    else:
        user_error_decision = input("Invalid Input! if you want to try again type T or if you want to exit type EXIT\n")
        if user_error_decision == "EXIT":
            print("Thank you,you can exit the screen now")
        elif user_error_decision == "T":
            morse_code_user_decision()
        else:
            print("You are typing invalid inputs! Program has been stopped !")

morse_code_user_decision()