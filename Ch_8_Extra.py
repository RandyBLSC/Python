import random
def get_Menu_Input(my_rainfall):  
    usrInput='w'  
    while usrInput !='q':
        print()
        print('      Main Menu')
        print('1  Rainfall Stats')
        print('2  List Functions')
        print('3  Encryption')       
        print('4  Dictionary Methods')
        print('q  Quit')
        print()
        usrInput=input('Enter the problem you want to solve:')
        if usrInput.upper()=='Q':
            break
        elif usrInput=="1":
            my_rainfall=rainfall_menu(my_rainfall)           
        elif usrInput=="2":
            my_list_functions_menu()            
        elif usrInput=="3":
            my_encryption_menu()            
        elif usrInput=="4":
            my_dictionary_menu()
    return

def my_dictionary_menu():
    my_dictionary=my_dictionary_initialize()
    usrInput='w'  
    while usrInput !='q':
        print()
        print('      Dictionary Methods Menu')
        print('1  dictionary.clear')
        print('2  dictionary.get')
        print('3  dictionary.update') 
        print('4  dictionary.pop')
        print('5  Reinitialize the dictionary')
        print('q  Quit')
        print('Here is the current dictionary:')
        print('****************')
        print(my_dictionary)
        print('****************')        
        usrInput=input('Enter the problem you want to solve:')
        if usrInput.upper()=='Q':
            break
        elif usrInput=="1":
            my_dictionary_clear(my_dictionary)           
        elif usrInput=="2":
            my_dictionary_get(my_dictionary)           
        elif usrInput=="3":
            my_dictionary_update(my_dictionary)
        elif usrInput=="4":
            my_dictionary=my_dictionary_pop(my_dictionary)
        elif usrInput=="5":
            my_dictionary=my_dictionary_initialize() 
    return
def my_second_dictionary_initialize():
    my_second_dictionary={
        'A':111,'X':2,'L':3,
        'P':4,'E':55,'S':6       
    }
    return my_second_dictionary
def my_dictionary_initialize():
    my_dictionary={
        'A':1,'B':2,'C':3,
        'D':4,'E':5,'F':6       
    }
    return my_dictionary
def my_dictionary_clear(my_dictionary):
    print('*** Clear ***')
    print('Removes all items from the dictionary.') 
    print('Code: my_dictionary.clear()')        
    my_dictionary.clear()
    return 
def my_dictionary_get(my_dictionary):
    print('*** Get ***')
    print('Reads the value of the key entry from the dictionary. If the key does not exist in the dictionary, then returns default.')
    my_item=input('Key: ') 
    my_default=input('Default value:')       
    print('Code: my_dictionary.get(\'%s\',\'%s\')'%(my_item,my_default))
    print('The returned value is:',my_dictionary.get(my_item,my_default))    
    return
def my_dictionary_update(my_dictionary):
    my_second_dictionary=my_second_dictionary_initialize()
    print('*** Update ***')
    print('Merges two dictionaries . Existing entries in first dictionary are overwritten if the same keys exist in the second dictionary.')      
    print('Code: my_first_dictionary.update(my_second_dictionary)')
    print(my_dictionary)
    print(my_second_dictionary)
    my_dictionary.update(my_second_dictionary)   
    print('Updated: \n',my_dictionary)
    return my_dictionary    
def my_dictionary_pop(my_dictionary):
    print('*** Pop ***')
    print('Removes and returns the key value from the dictionary. If key does not exist, then default is returned')   
    my_key=input('Enter key item:')
    my_default=input('Default value:')       
    print('Code: my_dictionary.pop(\'%s\',\'%s\')'%(my_key,my_default))
    my_poped=my_dictionary.pop(my_key,my_default)
    print('Item popped:',my_poped)
    return my_dictionary

def my_encryption_dictionary_initialize():
    my_encryprion_dictionary=dict()
    my_encryption_list=list()
    for x in range(32,126):
        my_encryprion_dictionary[chr(x)]=chr(x)
        my_encryption_list.append(chr(x))
    #print (my_encryption_list)
    random.shuffle(my_encryption_list)
    x=0
    for key in my_encryprion_dictionary.keys():
        my_encryprion_dictionary[key]=my_encryption_list[x]
        x=x+1
    return my_encryprion_dictionary
def my_encryption_menu():
    my_encryption_dictionary=my_encryption_dictionary_initialize()
    print(my_encryption_dictionary)
    usrInput='w'  
    while usrInput !='q':
        print()
        print('      Encryption  Menu')
        print('1  Encrypt text')
        print('2  Decrypt text')
        print('3  Change encryption dictionary') 
        print('q  Quit')        
        usrInput=input('Enter the problem you want to solve:')
        if usrInput.upper()=='Q':
            break
        elif usrInput=="1":
            my_encryption_encode(my_encryption_dictionary)           
        elif usrInput=="2":
            my_encryption_decode(my_encryption_dictionary)                           
        elif usrInput=="3":
            my_encryption_dictionary=my_encryption_dictionary_initialize() 
    return
def my_encryption_encode(my_encryption_dictionary):
    my_text=input('Enter text you want encryped:\n')
    my_encoded=""
    for x in my_text:
        my_encoded+=my_encryption_dictionary[x]
    print('Encrypted:',my_encoded)
    return
def my_encryption_decode(my_encryption_dictionary):
    my_text=input('Enter text you want decryped:\n')
    my_decoded=""
    for x in my_text:
        #my_decoded+=my_encryption_dictionary.get(x)
        my_decoded+=list(my_encryption_dictionary.keys())[list(my_encryption_dictionary.values()).index(x)]
    print('Decrypted:',my_decoded)
    return

def my_list_functions_menu():
    my_list=my_list_initialize()
    usrInput='w'  
    while usrInput !='q':
        print()
        print('      List Functions Menu')
        print('1  list.append')
        print('2  list.extend')
        print('3  list.insert')       
        print('4  list.remove')
        print('5  list.pop Last item')
        print('6  list.pop Specified item')
        print('7  list.sort')
        print('8  list.reverse')
        print('9  list.index')
        print('0  list.count')
        
        print('q  Quit')
        print('Here is the current list:')
        print('****************')
        print(my_list)
        print('****************')
        usrInput=input('Enter the problem you want to solve:')
        if usrInput.upper()=='Q':
            break
        elif usrInput=="1":
            my_list=my_list_append(my_list)           
        elif usrInput=="2":
           my_list=my_list_extend(my_list)            
        elif usrInput=="3":
            my_list=my_list_insert(my_list)            
        elif usrInput=="4":
            my_list=my_list_remove(my_list)
        elif usrInput=="5":
            my_list=my_list_pop(my_list)
        elif usrInput=="6":
            my_list=my_list_pop_item(my_list)    
        elif usrInput=="7":
            my_list=my_list_sort(my_list)
        elif usrInput=="8":
            my_list=my_list_reverse(my_list)
        elif usrInput=="9":
            my_list_index(my_list)
        elif usrInput=="0":
            my_list_count(my_list)
def my_list_count(my_list):
    print('*** Count ***')
    print('Count the number of times specified value is in list.')  
    my_item=input('Enter item to be counted: ')
    print('Code: my_list.count(\'%s\')'%my_item)    
    my_count=my_list.count(my_item)
    print('Count of %s is %d'%(my_item,my_count))
    return 
def my_list_index(my_list):
    print('*** Index ***')
    print('Return index of first item in list with specified value.')  
    print('* Note: remember that 0 is the first position')
    my_item=input('Enter item to be indexed: ')
    print('Code: my_list.index(\'%s\')'%my_item)    
    my_index=my_list.index(my_item)
    print('Index of %s is %d'%(my_item,my_index))
    return 
def my_list_reverse(my_list):
    print('*** Reverse ***')
    print('Reverse the elements of list in-place.')  
    print('Code: my_list.reverse()')
    print('Start:',my_list)
    my_list.reverse()    
    print('End  :',my_list)
    return my_list
def my_list_sort(my_list):
    print('*** Sort ***')
    print('Sort the items of list in-place.')  
    print('Code: my_list.sort()')
    print('Start:',my_list)
    my_list.sort()    
    print('End  :',my_list)
    return my_list
def my_list_pop_item(my_list):
    print('*** Pop ***')
    print('Remove and return item at specified position in list.')  
    print('* Note: remember that 0 is the first position')
    my_position=int(input('Enter position of item to be popped: ')  )
    print('Code: my_list.pop(%d)'%my_position)
    print('Start:',my_list)
    my_item=my_list.pop(my_position)
    print('Item popped:',my_item)
    print('End  :',my_list)
    return my_list
def my_list_pop(my_list):
    print('*** Pop ***')
    print('Remove and return last item in list.')    
    print('Code: my_list.pop()')
    print('Start:',my_list)
    my_item=my_list.pop()
    print('Item popped:',my_item)
    print('End  :',my_list)
    return my_list
def my_list_remove(my_list):
    print('*** Remove ***')
    print('Remove first item from list with specified value.')
    my_item=input('Enter item: ')    
    print('Code: my_list.insert(\'%s\')'%my_item)
    print('Start:',my_list)
    my_list.remove(my_item)
    print('End  :',my_list)
    return my_list
def my_list_insert(my_list):
    print('*** Insert ***')
    print('* Note: remember that 0 is the first position')
    print('Insert item into list before specified position.')
    my_item=input('Enter item: ')
    my_position=int(input('Enter item before position: '))
    print('Code: my_list.insert(%i,\'%s\')'%(my_position,my_item))
    print('Start:',my_list)
    my_list.insert(my_position,my_item)
    print('End  :',my_list)
    return my_list
def my_list_extend(my_list):
    print('*** Extend ***')
    print('* Note: This example only the string datatype.')
    print('Add all items in [x] to list.')
    my_item=input('Enter items seperated by a coma \',\'').split(',')
    print('Code: my_list.extend([%s])'%my_item)
    print('Start:',my_list)
    my_list.extend(my_item)
    print('End  :',my_list)
    return my_list
def my_list_append(my_list):
    print('*** Append ***')
    print('The append function will add an item to the end of list.')
    my_item=input('Enter an item to add to the list:')
    print('Code: my_list.append(\'%s\')'%my_item)
    print('Start:',my_list)
    my_list.append(my_item)
    print('End  :',my_list)
    return my_list
def my_list_initialize():
    my_list=['a','b','c','d']
    return my_list

def rainfall_menu(my_rainfall):
    usrInput='w'
    while usrInput !='q':
        print()
        print('      Rainfall Menu')
        print('1  Enter data')
        print('2  Total Rainfall')
        print('3  Average Rainfall')       
        print('4  Highest and Lowest Rainfall')
        print('5  Reset Rainfall amounts')
        print('q  Quit')
        print()
        usrInput=input('Enter the problem you want to solve:')
        if usrInput.upper()=='Q':
            break
        elif usrInput=="1":
            my_rainfall=rainfall_enter_data(my_rainfall) 
        elif usrInput=="2":
            rainfall_total(my_rainfall)            
        elif usrInput=="3":
            rainfall_average(my_rainfall)            
        elif usrInput=="4":
            rainfall_high_low(my_rainfall)
        elif usrInput=="5":
            my_rainfall=rainfall_initialize()    
        return my_rainfall
def rainfall_high_low(my_rainfall):
    month=max(my_rainfall, key=my_rainfall.get)
    mx=my_rainfall[month]
    print('%s had the highest total with %d inches'%(month,mx))
    month=min(my_rainfall, key=my_rainfall.get)
    mx=my_rainfall[month]
    print('%s had the lowest total with %d inches'%(month,mx))
    return
def rainfall_average(my_rainfall):
    avg=sum(my_rainfall.values())/len(my_rainfall)
    print("The average rainfall for the year is:",avg)
    return
def rainfall_total(my_rainfall):
    #print(my_rainfall)
    total=sum(my_rainfall.values())
    print("The total rainfall for the year is:",total)
    return
def rainfall_enter_data(my_rainfall):
    #print('rainfall_enterData',my_rainfall)
    print('  Enter Rainfall Data')
    for month in my_rainfall:
        amt=int(input('Enter the total ranfall for %s:'%month))
        my_rainfall[month]=amt
    print('Data entry complete\n')
    return my_rainfall
def rainfall_initialize():
    my_rainfall={'January':0,
                 'February':0,
                 'March':0,
                 'April':0,
                 'May':0,
                 'June':0,
                 'July':0,
                 'August':0,
                 'September':0,
                 'October':0,
                 'November':0,
                 'December':0
                 }
    return my_rainfall           

if __name__ == '__main__':
    # Complete main section of code
    my_rainfall=rainfall_initialize()
    #print(my_rainfall)
    get_Menu_Input(my_rainfall)