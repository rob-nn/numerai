import csv

def main():
    with open ('original_data/numerai_training_data.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print ', '.join(row)

if __name__ == '__main__':
    main()
