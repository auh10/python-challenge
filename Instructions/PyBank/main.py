#read data from file named "budget_data.csv" in folder named "Resources"
import os, csv
csv_path = os.path.join("../Resources/budget_data.csv")
with open(csv_path, newline='', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row)

print(len(csv_path))




#write cleaned data into CSV file
# import os, csv
# output_path = os.path.join("..", "output", "budget_data.csv")
# with open(output_path, "w", newline='', encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     csv_writer.writerow([
#         [" "]
# ])