# remember to fork this and push to github

# f = open('test.txt', "r")
# print(f.readlines())
# f.close()

# with open('test.txt', 'r') as f: 
#   f_contents = f.readlines()
#   print(f_contents, end='')

# employee_file = open("employees.txt", "r")
# print(employee_file.readlines())
# employee_file.close()

# employee_file = open("employees.txt", "r")
# print(employee_file.readlines()[1])
# employee_file.close()

# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()

with open('readme.txt', 'w') as f:
  f.write('readme')

  # this overwrites the original content
with open('readme.txt', 'w') as f:
  f.write('I dont care')

  # this appends to the oroginal content 
with open('readme.txt', 'a') as f:
  f.write('I dont care 3xxxxxx')

# create a file through python code
# get it to accept user input
# to append to the content

with open('user.txt', 'a') as f:
  input = input("Enter whatever you want: ")
  f.write(input)
