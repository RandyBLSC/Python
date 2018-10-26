def get_title():
    return input('Enter a title for the data:')

def get_col():
    col1=input('\nEnter the column 1 header:')
    print('\nYou entered:',col1)
    col2=input('\nEnter the column 2 header:')
    print('\nYou entered:',col2)
    return col1,col2
def get_data_point():
    sp_s=[]
    error=1
    while error==1:        
        my_data=input ('\nEnter a data point (-1 to stop input):')
        if my_data =="-1":
            print('\n')
            sp_s=[-1,-1]
            return sp_s
            break
        sp_s=my_data.split(',')
    
        if my_data.count(',')==0:
            print ('\nError: No comma in string.')
            continue
        if my_data.count(',')>1:
            print('\nError: Too many commas in input.')
            continue

        try: 
            int(sp_s[1])
            sp_s[1]=int(sp_s[1]) # cannot do this earlier due to single "," error checking        
        except ValueError:                 
            print('\nError: Comma not followed by an integer.')
            continue
        error=0

    print('\nData string:',sp_s[0])
    print('Data integer:',sp_s[1])
    return sp_s


my_title=get_title()
print('\nYou entered:', my_title)
my_col1,my_col2=get_col()
my_dp1,my_dp2=get_data_point()
dp1=[]
dp2=[]
while my_dp2 !=-1:
    dp1.append(my_dp1)
    dp2.append(my_dp2)    
    my_dp1,my_dp2=get_data_point()
#print('\n')

print(f'{my_title:>33}')

print(f'{my_col1:20}|{my_col2:>23}')
print('--------------------------------------------')
#print('%20s|%23s'%(my_col1,my_col2))
for x in range(len(dp1)):
     print(f'{dp1[x]:20}|{dp2[x]:23}')  
print('')
for x in range(len(dp1)):
    v="*" * dp2[x]
    print(f'{dp1[x]:>20} {v}')      