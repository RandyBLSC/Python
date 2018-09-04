total=0
# dictionary of services and prices
svc_dict={    
    'Oil change':35,
    'Tire rotation':19,
    'Car wash':7,
    'Car wax':12
} 
# print header
print('Davy\'s auto shop services')
# rather than "if" every item in the dictionary, we will use the "for" loop
for item in svc_dict:
    print(item + ' -- $'+ str(svc_dict[item]))
# get input
print()
request1 = input('Select first service:\n')
request2 = input('Select second service:\n')
# print invoice
print('\nDavy\'s auto shop invoice\n')
if request1 != "-":
    print('Service 1: %s, $%d' % (request1,svc_dict[request1]))
    total = svc_dict[request1]
else:
    print('Service 1: No service')
if request2 !='-':
    print('Service 2: %s, $%d' % (request2,svc_dict[request2]))
    total = total + svc_dict[request2]
else:
    print('Service 2: No service')
# print total charges
print()
print ('Total: $%d'%(total))



''' how the output should look
Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12

Select first service:
Tire rotation
Select second service:
-

Davy's auto shop invoice

Service 1: Tire rotation, $19
Service 2: No service

Total: $19
'''