from checkout import CheckOut

''' Checkout is a child class of Product.

    **** methods of Checkout class ****
            add_to_cart(), calculate_total_price()

    **** properties of Checkout class ****
            cart, bill_amount

    **** methods inherited by Checkout class from Product ****
            add_new_product(), delete_product(), reset_product_list(), view_product_list()

    **** properties inherited by Checkout class from Product ****
            product_dict

'''

co = CheckOut()
co.view_product_list()

co.add_to_cart()
co.add_to_cart()
co.add_to_cart()
co.add_to_cart()
co.calculate_total_price()