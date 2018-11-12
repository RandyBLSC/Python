class CellPhone:
    def __init__(self, manufact="unknown",model="unknown",retail_price=0):
        self.manufact=manufact
        self.model=model
        self.retail_price=retail_price
        return 
    def get_manufacture(self):
        return self.manufact    
    def set_manufact(self,manufact):
        self.manufact=manufact
        return    
    def get_model(self):
        return self
    def set_model(self,model):
        self.model=model
        return    
    def get_retail_price(self):
        return self.retail.price
    def set_retail_price(self,retail_price):
        self.retail.price=retail_price
        return    
def get_cell_info():
    manuf=input('Enter the manufacturer: ')
    model=input('Enter the model number: ')
    price=float(input('Enter the price: '))
    my_cell=CellPhone(manuf,model,price)    
    return my_cell
def print_cell_info(my_cell):
    print('Here is the data that you entered:')
    print('Manufacturer:',my_cell.manufact)
    print('Model Number:',my_cell.model)
    print('Retail Price: $%.2f'%my_cell.retail_price)
if __name__ == "__main__":
       my_cell=get_cell_info()
       print_cell_info(my_cell)