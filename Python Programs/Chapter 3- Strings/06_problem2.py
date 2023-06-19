# WAP to fill in a letter template given below with the name and date
'''
letter = "Dear <|NAME|>
                You are selected!
               <|DATE|>
'''
letter = '''Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter your Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)