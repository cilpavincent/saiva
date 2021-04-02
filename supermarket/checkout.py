from products import Product

class CheckOut(Product):
    cart = []
    bill_amount = 0

    def add_to_cart(self):
        item = input("Enter an item: ").upper()
        if item not in Product.product_dict:
            print("Sorry, You seem to enter wrong item")
        else:
            self.cart.append(item)
            print(self.cart)


    def calculate_total_price(self):
        for x in set(self.cart):
            purchased_quantity = self.cart.count(x)
            if  Product.product_dict[x]["offer"]:
                n = purchased_quantity // Product.product_dict[x]["offer_quantity"]
            else:
                n=0
            discount_amount = n * Product.product_dict[x]["offer_price"]
            total_price = purchased_quantity * Product.product_dict[x]["price"]
            self.bill_amount += total_price - discount_amount
        print(f"Bill Amount: {self.bill_amount}")

        


# p = Product()

# p.view_product_list()
