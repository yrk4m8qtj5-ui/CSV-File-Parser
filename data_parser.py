def read_n_group_file(filename):                          #define function
  students = []                                           #store students as a list

  with open(filename, 'r') as file:                       #open file
          #read and process column names
          header_line = file.readline().strip()           #remove leading and trailing whitespace characters from a string
          header = header_line.split(',')

          #print(f"Columns: {header}")                     #print each header

          #read data
          for line in file:                               #iterate through item in file
            line = line.strip()                           #.spilt spilts string 'line' into list of substrings using commas as delimiter (cleans code)
            fields = line.split(',')
            if len(fields) == 6:
              try:
                  cgpa = float(fields[5])                 # Try to convert to float
              except ValueError:
                  print(f"Skipping line with bad CGPA: {fields}")
                  continue                                # Skip this line and go to the next
            
             
              student = {                                 #dict of headers
                  'Tutorial Group': fields[0],
                  'Student ID': fields[1],
                  'School': fields[2],
                  'Name': fields[3],
                  'Gender': fields[4],
                  'CGPA': cgpa                            # Use the converted 'cgpa' variable
              }
              students.append(student)
  return students

def create_tutgrps(students):

    tutgroups = {}                              #create empty dict that will store final grouped students
    for student in students:                    #iterate through each student in students
      group = student['Tutorial Group']         #extracts the tut grp key from student dict

      if group not in tutgroups:                #check if tut grp already exisits as a key in groups dict
        tutgroups[group] = []                   #initialize empty list for new group
      tutgroups[group].append(student)          #add student to the group
    return tutgroups

# Update the file path to access the file in the Colab environment
students = read_n_group_file("records.csv")
tutgroups = create_tutgrps(students)

# remove the tutgroup name in each values
for eachGrp in tutgroups.keys():
    for student in tutgroups[eachGrp]:
        student.pop('Tutorial Group',None)

# Print result to check if it works
import json
print(json.dumps(tutgroups, indent=2))