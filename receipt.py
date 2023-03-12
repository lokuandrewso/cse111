import csv
from datetime import datetime 

def main() :

    #the read request fxn
    request_list = read_requests("request.csv")

    item_no = 0
    product_name = 1
    price = 2

    products_dict = read_dictionary("products.csv", item_no)
    #print(products_dict)
    #print("Omar Catalogue")
    print()
    total_product = 0
    subtotal = 0
    for line in request_list:
        product_no_in_list = line[0]
        quntity = line[1]
    

        for items in products_dict.items():
            value = products_dict[item_no]
            product_no_dict = value[item_no]
            name_of_product = value[product_name]
            the_price = value[price]

        if product_no_in_list in product_no_dict:
            print(f'{product_no_dict}: {name_of_product} @ {the_price}')
            
            subtotal += float(the_price) * float(quntity)
            tax_rate = 0.06
            disc_rate = 0.10
            sales_tax = subtotal * tax_rate
            total = subtotal + sales_tax

        current_date_and_time = datetime.now()
            #call the weekday function
        weekday = current_date_and_time.weekday()
            #if today is Tuesday or Wednesday, compute the discount amount
        if weekday == 1 or weekday == 2:
            discount = round(subtotal * disc_rate, 2)
            print(f'Discount amount: {discount:.2f}')
            subtotal -= discount
    print()
    print(f'Number of Items: {quntity:.0f}')
    print(f'Subtotal: {subtotal:.2f}')
    print(f'Sales Tax: {sales_tax: .2f}')
    print(f'Total: {total}')
    print(f'Thank you for shopping with Omar Catalogue')
    print(f"{current_date_and_time:%A %I:%M %p}")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """ 
    dictionary = {}
    with open(filename, "rt") as products_file:
        reader = csv.reader(products_file)
        #skip the first line
        next(reader)

        for row in reader:
            item_no = row[key_column_index]
            dictionary[item_no] = row

        return dictionary
    
def read_requests(filename):
    #store data
    compound_list = []

    with open(filename, "rt") as request_file:
        file = csv.reader(request_file)
        #skip line
        for item in file:
            #name = item[key_column_index]
            #number = item[quantity]
            compound_list.append(item)
    return compound_list

# Call main to start this program.
if __name__ == "__main__":
    main()