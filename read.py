import csv
import numpy as np

def get_data_set():
    data_set = [] 
    categories = {}
    next_cat_index = 1
    first_line = True
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
                    next_cat_index += 1
                    cat_index = categories[category]
                data_set_item = np.append(data_set_item, np.array([cat_index]))
                data_set_item = np.append(data_set_item, np.array(row[15:]).astype(np.int))
                data_set.append(data_set_item)
            else:
                first_line = False 
    data_set = np.array(data_set)
    return (data_set, categories)

if __name__ == '__main__':
    main()
