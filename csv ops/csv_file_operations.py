"""
    Working with csv files
"""
import csv
# working with csv files using python

# with open('new_names.csv', 'r') as file:
#     # need to specify delimeter is its not a comma
#     CSV_READER = csv.reader(file, delimiter = '\t')

#     for line in CSV_READER:
#         print(line)

# ----------------------------------------------------------------------------------

# reading and writing to another file

# with open('names.csv', 'r') as file:
#     CSV_READER = csv.reader(file)

#     with open('new_names.csv', 'w', newline='') as new_file:
#         CSV_WRITER = csv.writer(new_file, delimiter = '\t')

#         for line in CSV_READER:
#             CSV_WRITER.writerow(line)


# -----------------------------------------------------------------------------------

# using dictionary reader

# with open('names.csv', 'r') as file:
#     # need to specify delimeter is its not a comma
#     CSV_READER = csv.DictReader(file)
#         # for line in CSV_READER:
#         #   print(line)

#     with open('dict_file.csv', 'w') as new_file:
#         fieldnames = ['first_name','last_name','email']
#         CSV_WRITER = csv.DictWriter(new_file, fieldnames, delimiter = '\t')
#         # to write fieldnames on firstline
#         CSV_WRITER.writeheader()

#         for line in CSV_READER:
#         #    del line['email']
#             CSV_WRITER.writerow(line)

# ---------------------------------------------------------------------------------------

# getting first and last name from csv file and entering as a sentence in text file

# This is also called as context manager

# with open('names.csv', 'r') as names:
#     namesReader = csv.reader(names)

#     with open('file.txt', 'w') as textFile:
#         for entry in namesReader:
#             string = 'Name : {} Last Name : {} has mail address : {}'.format(entry[0],entry[1],entry[2])
#             print(string,file=textFile,end='\n')
                
# ---------------------------------------------------------------------------------------

# writing firstname and lastname from csv file to html file:

# read csv file
name = []
with open('names.csv', 'r') as names:
    namesReader = csv.DictReader(names)

    for line in namesReader:
        name.append('{} {}'.format(line['first_name'],line['last_name']))
    
print(name)

html = ''
html += '<html>\n\t<ul>'
for name in name:
    html += '\t\t<li> {} </li>'.format(name)

html += '</ul>\n\t</html>'

print(html)

with open('names.html', mode='w') as file:
    file.write(html)

