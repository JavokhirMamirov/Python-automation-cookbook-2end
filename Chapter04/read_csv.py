import csv

############ Read csv file

# with open('documents/top_films.csv') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)

###############  use DictReader

with open('documents/top_films.csv') as file:
    data = csv.DictReader(file)
    structured_data = [row for row in data]
    print(structured_data[0]['Rank'])