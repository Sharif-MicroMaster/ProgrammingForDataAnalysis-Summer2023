import csv

def process(address):
    with open(address, 'r') as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            yield (row + [' ' + str(sum(map(int, row)))])   

row = process('a.csv')
with open('ans.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        new_row = ''
        while new_row != 'empty':
            new_row = next(row, 'empty')
            if new_row == 'empty':
                break
            writer.writerow(new_row)