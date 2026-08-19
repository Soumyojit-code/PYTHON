#CODE WITHOUT ANY FUNCTIONS
import random as r
import string as s
from word2number import w2n as w
while True:
    text=input("\n\t ENTER PASSWORD LENGTH : ")
    try:
        password_length=w.word_to_num(text)
        if password_length is not None:
            password_characters=s.digits+s.ascii_letters+s.punctuation
            password=''.join(r.choice(password_characters) for _ in range(password_length))
            print("\n\t YOUR PASSWORD OF LENGTH",password_length,"IS :",password)
    except ValueError:
        print("\n\t INVALID INPUT FOR LENGTH, TRY AGAIN ! ")
        
#CODE USING ONLY ONE FUNCTION(FOR THE WORD TO NUMBER CONVERTER)
import random as r
import string as s
from word2number import w2n as w
def convert_text_to_number(text):
    try:
        n=w.word_to_num(text)
        return n
    except ValueError:
        return None
while True:
    a=input("\n\t ENTER PASSWORD LENGTH : ")
    password_length=convert_text_to_number(a)
    if password_length is not None:
        password_characters=s.digits+s.ascii_letters+s.punctuation
        password=''.join(r.choice(password_characters) for _ in range(password_length))
        print("\n\t YOUR PASSWORD LENGTH OF",password_length,"IS :",password)
    else:
        print("\n\t INVALID INPUT FOR LENGTH, TRY AGAIN !")

#CODE USING TWO FUNCTIONS(FOR THE WORD TO NUMBER CONVERTER AND THE PASSWORD GENERATOR)
import random as r
import string as s
from word2number import w2n as w
def convert_text_to_number(text):
    try:
        a=w.word_to_num(text)
        return a
    except ValueError:
        return None
def passwords():
    while True:
        a=input("\n\t ENTER PASSWORD LENGTH : ")
        password_length=convert_text_to_number(a)
        if password_length is not None:
            password_characters=s.digits+s.ascii_letters+s.punctuation
            password=''.join(r.choice(password_characters) for _ in range(password_length))
            print("\n\t YOUR PASSWORD OF LENGTH",password_length,"IS :",password)
        else:
            print("\n\t INVALID LENGTH INPUT, TRY AGAIN !")
passwords()
