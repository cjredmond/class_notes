with open("data.csv") as open_file:
    contents = open_file.readlines()

# clean_data = []
# for row in contents:
#     row = row.replace("\n", "")
#     clean_data.append(row.split(","))

clean_data = [row.replace("\n", "").split(",") for row in contents]
#print(clean_data)
import csv
with open("data.csv") as open_file:
    contents = csv.reader(open_file)
#    print(list(contents))
#dictionary reader use more memory, you need to know column names

with open("data.csv") as open_file:
    contents = csv.DictReader(open_file)
    print(list(contents)[4])
