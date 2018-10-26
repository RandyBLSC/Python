def get_Menu_Input(usrInput):    
    while usrInput !='q':
        print()
        print('      Main Menu')
        print('1  Initials')
        print('5  Phone Alpha/Number Translator')
        print('9  Vowels and Constants')       
        print('12 Pig Latin')
        print('q  Quit')
        print()
        usrInput=input('Enter the problem you want to solve:')
        if usrInput.upper()=='Q':
            break
        elif usrInput=="1":
            initials()           
        elif usrInput=="5":
            alpha_phone()            
        elif usrInput=="9":
            vowel()            
        elif usrInput=="12":
             igpay_aitenlay()
        elif usrInput=="16":
             print('Future')

def igpay_aitenlay():
    my_new_sentence=""
    my_input=input('Enter a sentence and I will translate it into Pig Latin: ')
    my_input=my_input.lower()
    my_split=my_input.rstrip().split(' ')
    
    for my_word in my_split:
        #print('myword:%s**'% my_word)
        my_new_sentence+=my_word[1:]+my_word[0]+'ay '       
        
        #print(my_new_sentence.capitalize())
    print('Pig Latin:\n',my_new_sentence.capitalize())


def vowel():
    v,c,o=process_vowel()
    print('Vowels:',v)
    print('Consonents:',c)
    print('Non alphabet:',o)

def process_vowel():    
    my_vowels="AEIOUaeiou"
    my_input=input('Enter a string and I will count the vowels and consonants: ')
    v_counter=0
    c_counter=0
    o_counter=0
    for x in my_input:
        if my_vowels.count(x)>0:
            v_counter+=1
        elif x.isalpha():
            c_counter+=1
        else:
            o_counter+=1
    return v_counter,c_counter,o_counter



def initials():
    my_name=input('Enter your full name:')
    my_split=my_name.split(' ')    
    my_first=my_split[0]
    my_middle=my_split[1]
    my_last=my_split[2]
    my_initials=my_first[0]+'.' + my_middle[0] + '.'+my_last[0] + '.'
    print('Your initials are :',my_initials.upper())




def alpha_phone():
    ph_dictionary={
        'A':2,'B':2,'C':2,
        'D':3,'E':3,'F':3,
        'G':4,'H':4,'I':4,
        'J':5,'K':5,'L':5,
        'M':6,'N':6,'O':6,
        'P':7,'Q':7,'R':7,'S':7,
        'T':8,'U':8,'V':8,
        'W':9,'X':9,'Y':9,'Z':9
    }

    
    my_phone_number=input('Enter your 10 digit phone number:')
    my_new_phone_number=''
    for x in my_phone_number.upper():
        if x.isalpha():
            #print('%s is alpha' % (x))
            #print('Service 1: %s, $%d' % (x,ph_dictionary[x]))
           
            my_new_phone_number += str(ph_dictionary[x])
        else:
            #print('%s is not alpha' % (x))
            my_new_phone_number += x
    print('Your number is:',my_new_phone_number)




if __name__ == '__main__':
    # Complete main section of code
    get_Menu_Input("")