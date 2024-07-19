def convert_to_indian_currency(number):
    num_str = str(number)
    result = ""
    length = len(num_str)
    result = num_str[-3:]
    num_str = num_str[:-3]

    while len(num_str) > 0:
        result = num_str[-2:] + ',' + result
        num_str = num_str[:-2]

    return result

number = int(input("Enter the number : "))
formatted_number = convert_to_indian_currency(number)
print(formatted_number)  

