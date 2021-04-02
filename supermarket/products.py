class Product:

    ''' Passing in list of products in the store as a python dictionary which is a temperory approach. 
        In real application, this data could be obtained from csv or json file; or from database.
    '''
    product_dict = {
        "A":{"price":50,"offer":True,"offer_quantity":3, "offer_price":20},
        "B":{"price":30,"offer":True,"offer_quantity":2, "offer_price":15},
        "C":{"price":20,"offer":True,"offer_quantity":5, "offer_price":20},
        "D":{"price":60,"offer":False,"offer_quantity":0, "offer_price":0},
        "E":{"price":70,"offer":False,"offer_quantity":0, "offer_price":0}
    }

    ''' Functions that give control over the list of products. Deletion, Addition and Updation of product list is made possible.
        add_new_product()
        delete_product()
        reset_product_list()
        view_product_list()
    '''

    def add_new_product(self):
        product_dict = self.product_dict
        product = input("Product Name: ").upper()
        product_dict[product]=dict()
        product_dict[product]["price"] = input("Price of product: ")
        product_dict[product]["offer"] = bool(int(input("Any offers?\nIf yes press 1, otherwise press 0: ")))
        if product_dict[product]["offer"]:
            product_dict[product]["offer_quantity"] = int(input("Discount eligible purchase quantity: "))
            product_dict[product]["offer_price"] = int(input("Discount amount: "))
        else:
            product_dict[product]["offer_quantity"] = 0
            product_dict[product]["offer_price"] = 0

        self.product_dict=product_dict
        return self.product_dict
        


    def delete_product(self):
        product_dict = self.product_dict
        key = input("Enter the product you want to delete: ").upper()
        if key in product_dict.keys():
            confirm = bool(int(input(f"Are you sure about deleting?\nIf yes press 1, otherwise press 0: ")))
            if confirm:
                del product_dict[key]
                print("Product deleted.")
        else:
            print("Product not found! check if you entered correct name.")
        self.product_dict=product_dict
        return self.product_dict


    def reset_product_list(self):
        return self.product_dict.clear()


    def view_product_list(self):
        for x,y in self.product_dict.items():
            print(x, end=" -- ")
            for i,j in y.items():
                print(i,j, end= " \t\t ")
            print()
                
