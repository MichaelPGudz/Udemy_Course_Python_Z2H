import csv
import PyPDF2
import re

data = open('./Exercise_Files/find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

# First approach
n = 0
link = ''
while n < len(data_lines[0]):
    for line in data_lines:
        link += line[n]
        n += 1

print(link)


#Second approach
link_str = ''
for row_number, letter in enumerate(data_lines):
    link_str += letter[row_number]

print(link_str)
num = str([1,2,3,4,5,6,7,8,9,0])
f = open('./Exercise_Files/Find_the_Phone_Number.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(f)

pattern = r'\d{3}'
pattern_updated = r'\d{3}.\d{3}.\d{4}'

all_text = ''
for i in range(pdf.numPages):
    page = pdf.getPage(i)
    page_text = page.extractText()
    all_text += page_text

print(re.findall(pattern, all_text))

for match in re.finditer(pattern, all_text):
    print(match)

print(all_text[41794:41807])

print(re.findall(pattern_updated, all_text))