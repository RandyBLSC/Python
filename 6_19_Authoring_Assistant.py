import re
def print_menu(usrStr):
    menuOp = ' '
    while menuOp != 'q':
        print('\nMENU')
        print('c - Number of non-whitespace characters')
        print('w - Number of words')
        print('f - Fix capitalization')
        print('r - Replace punctuation')
        print('s - Shorten spaces')
        print('q - Quit')
        print()
        menuOp=input('Choose an option:')
        if menuOp=='q':
            print()         
            break
        elif menuOp=='c':            
            print('Number of non-whitespace characters:', get_num_of_non_WS_characters(usrStr))
        elif menuOp=="w":
             print('Number of words:', get_num_of_words(usrStr))
        elif menuOp=="f":
            count,temp= fix_capitalization(usrStr)
            print ('Number of letters capitalized:',count)
            print ('Edited text:',temp)
        elif menuOp=="r":
            NusrStr,eCount, sCount=replace_punctuation(usrStr,0,0)
            print('Punctuation replaced')
            print('exclamationCount:',eCount)
            print('semicolonCount:',sCount)
            print('Edited text:',NusrStr)
        elif menuOp=="s":
            print('Edited text:',shorten_space(usrStr))
        elif menuOp=="z":
            print(mycap(usrStr))
    return menuOp, usrStr
    
def get_num_of_non_WS_characters(usrStr):
    return len(usrStr.replace(" ", ""))    

def get_num_of_words(usrStr):
    return len(usrStr.split())
    
def fix_capitalization(usrStr):
    temp=""    
    count=0
    lp=0
    for index in range(len(usrStr)):
        ch=usrStr[index]
        ch=ch.lower()
        if index==0:
            ch=ch.upper()        
        if ch=="!" or ch=="?" or ch=="." :
            count =count + 1
            lp=lp+1        
        if lp>1 and ch != " ":
            ch=ch.upper() 
            lp=0   
        if lp>0:
            lp=lp + 1
        temp = temp + ch 
    temp=temp.replace(" i ", " I ")
    return count,temp

def mycap(usrStr):
    rtn = re.split('([.!?] *)', usrStr)
    print('')
    temp=(''.join([each.capitalize() for each in rtn]))
    return temp
    


def replace_exclamation(usrStr,exclamationCount, semicolonCount):
    exclamationCount=usrStr.count("!")
    semicolonCount=usrStr.count(";")
    temp=""
    for i in range(len(usrStr)):
        if usrStr[i]=="!":
            temp=temp+"."
        elif usrStr[i]==";":
            temp=temp+","
        else:
            temp=temp+usrStr[i]    
        temp = usrStr.replace(";",",")
        temp = temp.replace("!",".")
    return temp,exclamationCount,semicolonCount

def shorten_space(usrStr):
    temp=usrStr.split()
    temp2=" "
    temp3=temp2.join(temp)
    return temp3

def get_string():
    myStr = input('Enter a sample text:\n')
    return myStr
def replace_punctuation(usrStr):
    return count,temp

def replace_punctuation(usrStr,exclamationCount, semicolonCount):
    exclamationCount=usrStr.count("!")
    semicolonCount=usrStr.count(";")
    temp=""
    for i in range(len(usrStr)):
        if usrStr[i]=="!":
            temp=temp+"."
        elif usrStr[i]==";":
            temp=temp+","
        else:
            temp=temp+usrStr[i]   
        temp = usrStr.replace(";",",")
        temp = temp.replace("!",".") 
    return temp,exclamationCount,semicolonCount


if __name__ == '__main__':
    # Complete main section of code
    usrStr=get_string()
    #usrStr="we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!"
    print('\nYou entered:',usrStr)
    print_menu(usrStr)
    '''
(1) Prompt the user to enter a string of their choosing. Store the text in a string. 
Output the string. (1 pt) 

(2) Implement a print_menu() function, which has a string as a parameter, outputs
 a menu of user options for analyzing/editing the string, and returns the user's 
 entered menu option and the sample text string (which can be edited inside the 
 print_menu() function). Each option is represented by a single character. 
 If an invalid character is entered, continue to prompt for a valid choice. 
 Hint: Implement the Quit menu option before implementing other options. 
 Call print_menu() in the main section of your code. Continue to call print_menu() 
 until the user enters q to Quit. (3 pts) 

(3) Implement the get_num_of_non_WS_characters() function. 
get_num_of_non_WS_characters() has a string parameter and returns the number of 
characters in the string, excluding all whitespace. Call 
get_num_of_non_WS_characters() in the print_menu() function. (4 pts) 

(4) Implement the get_num_of_words() function. get_num_of_words() has a string 
parameter and returns the number of words in the string. Hint: Words end when a 
space is reached except for the last word in a sentence. Call get_num_of_words() 
in the print_menu() function. (3 pts) 

(5) Implement the fix_capilization() function. fix_capilization() has a string 
parameter and returns an updated string, where lowercase letters at the beginning 
of sentences are replaced with uppercase letters. fix_capilization() also returns 
the number of letters that have been capitalized. Call fix_capilization() in the
 print_menu() function, and then output the number of letters capitalized and the
  edited string. Hint 1: Look up and use Python functions .islower() and .upper() 
  to complete this task. Hint 2: Create an empty string and use string 
  concatenation to make edits to the string. (3 pts) 

(6) Implement the replace_punctuation() function. replace_punctuation() has a 
string parameter and two keyword argument parameters exclamationCount and 
semicolonCount. replace_punctuation() updates the string by replacing each 
exclamation point (!) character with a period (.) and each semicolon (;) 
character with a comma (,). replace_punctuation() also counts the number of 
times each character is replaced and outputs those counts. Lastly, 
replace_punctuation() returns the updated string. Call replace_exclamation() 
in the print_menu() function, and then output the edited string. (3 pts) 

(7) Implement the shorten_space() function. shorten_space() has a string parameter 
and updates the string by replacing all sequences of 2 or more spaces with a single 
space. shorten_space() returns the string. Call shorten_space() in the print_menu() 
function, and then output the edited string. Hint: Look up and use Python 
function .isspace(). (3 pt) 

'''