from bs4 import UnicodeDammit
####################### read text file

# with open('documents\zen_of_python.txt', 'rt') as file:
#     for line in file:
#         if 'should' in line.lower():
#             print(line)

#################### read utf8 text file

with open('documents/example_utf8.txt', encoding='utf8') as file:
    print(file.read())


##################### read ISO text file

with open('documents/example_iso.txt', encoding='iso-8859-1') as file:
    print(file.read())