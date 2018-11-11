# Type code for classes here
class ItemToPurchase:
    def __init__(self):
        self.item_name ="none"
        self.item_price=0.00
        self.item_quantity=0
    def __str__(self):
        return ('%s %d @ $%.0f = $%.0f'%(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))
    def __add__(self,other):
        return (self.item_price*self.item_quantity)+(other.item_price*other.item_quantity)


if __name__ == "__main__":
    # Type main section of code here
    item1=ItemToPurchase()
    print('Item 1')
    item1.item_name=input('Enter the item name:')
    item1.item_price=float(input('\nEnter the item price:'))
    item1.item_quantity=int(input('\nEnter the item quantity:'))
    print()
    item2=ItemToPurchase()
    print('\nItem 2')
    item2.item_name=input('Enter the item name:')
    item2.item_price=float(input('\nEnter the item price:'))
    item2.item_quantity=int(input('\nEnter the item quantity:'))
    print()
    print()
    print('TOTAL COST')
    print(item1)
    print(item2)
    print()
    print('Total: $%.0f'%(item1+item2))