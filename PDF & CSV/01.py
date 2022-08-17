import csv

#Open the file
data = open('example.csv', encoding='utf-8')

#CSV reader
csv_data = csv.reader(data)

#Reformat it into python object list of lists
data_lines = list(csv_data)

print(data_lines)
all_emails = []
full_names = []

for line in data_lines[1:]:
    # print(line)
    all_emails.append(line[3])

for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])

print(all_emails)
print((full_names))

file_to_output = open('first_exercise_saved.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])

file_to_output.close()

f = open('first_exercise_saved.csv', mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1', '2', '3'])
f.close()
