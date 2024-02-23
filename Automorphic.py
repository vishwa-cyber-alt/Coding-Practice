# input=9
# convert_to_string=str(input)
# square=pow(6,2)
# convert_square_to_string=str(square)
# if convert_square_to_string.endswith(convert_to_string):
#     print("yes")
# else:
#     print("no")

def find(input):
    convert_to_string=str(input)
    square=pow(input,2)
    convert_square_to_string=str(square)
    if convert_square_to_string.endswith(convert_to_string):
        print(input," = yes")
    else:
        print(input," = no")
find(2)
find(6)
find(5)
find(76)
find(376)
