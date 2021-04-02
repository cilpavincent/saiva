from products import Product

class Offer(Product):

    def remove_offer(self):
        global product_dict 
        product_dict = self.product_dict
        item = input("Enter the product you want to change: ").upper()
        if item in product_dict:
            confirm = bool(int(input("Are you sure about removing offer? If yes, press any number else press '0'")))
            if confirm:
                product_dict[item]["offer"] = False
                product_dict[item]["offer_quantity"] = 0
                product_dict[item]["offer_price"] = 0
                print("Offer deleted")
                return product_dict
            else:
                print("Removing offer cancelled..")
        else:
            print("Wrong entry")
        
    
    def new_offer(self):
        global product_dict 
        product_dict = self.product_dict
        item = input("Enter the product you want to change: ").upper()
        if item in product_dict:
            product_dict[item]["offer"] = True
            product_dict[item]["offer_quantity"] = int(input("Discount eligible purchase quantity: "))
            product_dict[item]["offer_price"] = int(input("Discount amount: "))
            return product_dict
        else:
            print("Wrong entry!")

        
    def view_offers(self):
        global product_dict 
        product_dict = self.product_dict
        for x,y in product_dict.items():
            if product_dict[x]["offer"]:
                offer_price = product_dict[x]["offer_price"]
                offer_quantity = product_dict[x]["offer_quantity"]
                print(f"{x} -- Offer Price:{offer_price}, Offer Quantity: {offer_quantity}")
        


