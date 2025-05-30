import csv

def read_and_write():
    with open('ds.csv','r') as f :
        reader = csv.reader(f)
        with open('ds.tsv', 'w') as tf:
            writer = csv.writer(tf, delimiter='\t')
            for row in reader:
                writer.writerow(row)

if __name__ == '__main__':
    read_and_write()
