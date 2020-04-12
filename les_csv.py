import csv

phone = [['brand', 'model', 'capaciti'],['Xiaomi','Note 10 Pro','5260']]

with open('lesson.csv', 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(phone)
print('Writing complete!')


with open('lesson.csv') as f:
    reader = csv.reader(f, delimiter =';')
    for row in reader:
        print(row)