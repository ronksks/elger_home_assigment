# 1. Price Check

# string products[n]: each products[i] is the name of an item for sale
# string product_prices[n]: each product_prices[i] is the price of products[i]
# string product_sold[m]: each product_sold[j] is the name of a product sold
# float sold_price[m]: each sold_price[j] contains the sale price recorded for product_sold[j].


def price_check(products, product_prices, product_sold, sold_price):
    # first we check if the list are not empty
    def are_lists_empty():
        my_lists = [products, product_prices, product_sold, sold_price]
        for lst in my_lists:
            if not lst:
                return 1
        return 0

    # we check if the input is follows the constrains
    def check_constrains():
        if not (len(products) >= 1 and len(product_sold) >= 1) or not (len(products) <= 99 and len(product_sold) <= 99):
            return 0
        if not (sorted(product_prices)[0] >= 1.00) or not (sorted(sold_price)[0] >= 1.00) or not (
                sorted(product_prices)[-1] <= 100000.00) or not (sorted(sold_price)[-1] <= 100000.00):
            return 0
        return 1

    # if all checks out we can start checking the prices
    if not are_lists_empty() and check_constrains():
        products_and_prices_origin = {}
        products_and_prices_sold = {}
        error = 0
        for i in range(0, len(products)):
            # create a dictionary for the products and the prices
            # then we compare each price of the sold products to the original product and product price
            products_and_prices_origin.update({products[i]: product_prices[i]})
        for j in range(0, len(product_sold)):
            products_and_prices_sold.update({product_sold[j]: sold_price[j]})
            if (float(products_and_prices_sold.get(product_sold[j])) != products_and_prices_origin.get(
                    product_sold[j])):
                error += 1
        return (error)
    return 0


print(price_check(['eggs', 'milk', 'cheese'],
                  [2.89, 3.29, 5.79],
                  ['eggs', 'eggs', 'cheese', 'milk'],
                  [2.89, 2.99, 5.97, 3.29]))
print(price_check(['rice', 'sugar', 'wheat', 'cheese'],
                  [16.89, 56.92, 20.89, 345.99],
                  ['rice', 'cheese'],
                  [18.99, 400.89]))
