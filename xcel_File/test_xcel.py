import csv

with open('/Users/aiperizh/Desktop/pythonProject/xcel_File/email.csv') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        if row['manager_id'] < 200:
            print(row['manager_id'])
 
   
# # open the file in the write mode
# f = open('xcel_File/csv_file', 'w')

# # create the csv writer
# writer = csv.writer(f)

# # write a row to the csv file
# writer.writerow("lolo")

# # close the file
# f.close()