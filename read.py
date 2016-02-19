import csv
import numpy as np


def main():
    data_set = [] 
    categories = {}
    next_cat_index = 1
    first_line = True
    count = 0
    with open ('original_data/numerai_training_data.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if not first_line: #Skip first line
                data_set_item = np.array(row[0:14]).astype(np.int)
                category = row[14]
                try:
                    #if KeyError add a new category
                    cat_index = categories[category] 
                except KeyError as e:
                    categories[category] = next_cat_index
                    cat_index = categories[category]
                    next_cat_index += 1
                data_set_item = np.append(data_set_item, np.array([cat_index]))
                data_set_item = np.append(data_set_item, np.array(row[15:]).astype(np.int))
                data_set.append(data_set_item)
            else:
                first_line = False 
            count += 1

        data_set = np.array(data_set)
        print 'Data set shape', data_set.shape

if __name__ == '__main__':
    main()
