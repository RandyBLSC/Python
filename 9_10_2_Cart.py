# Type code for classes here
import datetime
class ItemToPurchase:
    def __init__(self, item_name='none', item_description='none',item_price=0,item_quantity=0):
        self.item_name =item_name
        self.item_description=item_description
        self.item_price=item_price
        self.item_quantity=item_quantity
    def __str__(self):
        return ('%s %d @ $%.0f = $%.0f'%(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))
    def __add__(self,other):
        return (self.item_price*self.item_quantity)+(other.item_price*other.item_quantity)
    def print_item_description(self):
        print('%s: %s '%(self.item_name,self.item_decription))
class ShoppingCart:
    def __init__(self,customer_name='none',current_date='January 1, 2016',cart_items=list()):
        self.customer_name=customer_name
        self.current_date=current_date
        self.cart_items=cart_items
    def add_item(self): 
        item=ItemToPurchase()
        print('ADD ITEM TO CART')
        item.item_name=input('Enter the item name:')
        item.item_description=input('Enter the item description:')
        item.item_price=float(input('Enter the item price:'))
        item.item_quantity=int(input('Enter the item quantity:'))      
        self.cart_items.append(item)
        return
    def remove_item(self, item):
        try:
            b=self.cart_items.index(item)
        except ValueError:
            print('Item not found in cart. Nothing removed.')
        else:
            self.cart_items.remove(item)    
    def modify_item(self,item):
        try:
            b=self.cart_items.index(item)
        except ValueError:
            print('Item not found in cart. Nothing removed.')
        else:
            self.cart_items.remove(item)
    def get_num_items_in_cart(self):
        total_items=0
        for x in self.cart_items:
            num_items=x.item_quantity
            total_items+=num_items
        return total_items
    def get_cost_of_cart(self):
        total_cost=0
        for x in self.cart_items:
            total_cost+=x.item_quantity*x.item_price
        return total_cost    
    def print_total(self):
        total_cost=0
        total_items=0
        print('OUTPUT SHOPPING CART')
        print('%s\'s Shopping Cart - %s'%(self.customer_name,self.current_date)) # why self here
        print('Number if items:',ShoppingCart.get_num_items_in_cart(self))       # why ShoppingCart here
        print()
        for x in self.cart_items:
            print(x)
        print()    
        print ('Total: $%.0d'%ShoppingCart.get_cost_of_cart(self))
        return
    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('%s\'s Shopping Cart - %s'%(self.customer_name,self.current_date))
        print()
        print('Item Descriptions:')
        for x in self.cart_items:
            print('%s: %s'%(x.item_name,x.item_description))
        return        
    
def shopping_menu(shopper):    
    usrInput='w'  
    while usrInput !='q':
        print()
        print('MENU')
        print('a  Add item to cart')
        print('r  Remove item from cart')
        print('c  Change item quantity')       
        print('i  Output item descriptions')
        print('o  Output shopping cart')
        print('q  Quit')
        print()
        usrInput=input('Choose an option:')
        print()
        if usrInput.upper()=='Q':
            break
        elif usrInput=="a":
            shopper.add_item()                     
        elif usrInput=="r":
            my_list_functions_menu()            
        elif usrInput=="c":
            my_encryption_menu()            
        elif usrInput=="i":
            shopper.print_descriptions()
        elif usrInput=="o":
            ShoppingCart.print_total(shopper)            

    return

def create_john_doe_cart():
    shopper=ShoppingCart()
    now=datetime.date.today()
    shopper.customer_name=input('Enter customer\'s name:')   
    print (now.strftime("%B %d, %Y"))    
    shopper.current_date=input('Enter today\'s date:') 
    print()
    print('Costomer\'s name:',shopper.customer_name)
    print('Today\'s date:',shopper.current_date)


    return shopper

if __name__ == "__main__":
    # Type main section of code here

    shopper=create_john_doe_cart()
    shopping_menu(shopper)