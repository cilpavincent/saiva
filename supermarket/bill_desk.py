from checkout import CheckOut
from offers import Offer

''' 
Checkout is a child class of Product.

    **** methods of Checkout class ****
            add_to_cart(), calculate_total_price()

    **** properties of Checkout class ****
            cart, bill_amount

    **** methods inherited by Checkout class from Product ****
            add_new_product(), delete_product(), reset_product_list(), view_product_list()

    **** properties inherited by Checkout class from Product ****
            product_dict

Offer is an imported class of offers module

        ** methods imported from Offer class **
                remove_offer()
                view_offers()
                new_offer()

'''

co = CheckOut()
co.view_product_list()
# input items purchased
co.add_to_cart()
co.add_to_cart()
co.add_to_cart()
co.add_to_cart()
# calculate the amount to be paid
co.calculate_total_price()


obj = Offer()
# obj.view_offers()
# obj.remove_offer()
# obj.new_offer()


# updating product list
# co.view_product_list()
# co.add_new_product()
# co.delete_product()
# co.reset_product_list()

