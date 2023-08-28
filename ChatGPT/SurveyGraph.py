# Import the matplotlib and csv package
import matplotlib.pyplot as plt
import csv

# Initialize the data
csv_data = []

# Reads through the spreadsheet in csv file
with open("responsefinalcopy.csv", 'r') as response:
    # Setting up all the data while removing the commas with the delimiter
    data = csv.reader(response, delimiter=',')
    # For each row in the spreadsheet, add the row to the csv_data list
    for row in data:
        csv_data.append(row)
    
# Setting up the data of the age groups
age_group = ['18-19', '20-29', '30-39', '40-49', '50+']
age_stats = [0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    age_stats[age_group.index(row[3])] += 1
    
# Creates a bar graph to show the data of the age groups
plt.bar(age_group, age_stats)
plt.title('Age')
plt.ylabel('# of People')
plt.xlabel('Age Groups')

plt.show()

# Setting up the data for the genders (For some responses, I had to change their response to 'Other,' to not show too many labels)
genders = ['Male', 'Female', 'Non-binary', 'Rather not say', 'Other']
gender_stats = [0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    gender_stats[genders.index(row[2])] += 1
# Creates a bar graph to display the data of the genders
plt.bar(genders, gender_stats)
plt.title('Gender')
plt.ylabel('# of People')
plt.xlabel('Genders')

plt.show()

# Setting up the data of the University Year
year = ['1st Year', '2nd Year', '3rd Year', '4th year', '5th Year or above']
year_stats = [0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    year_stats[year.index(row[-2])] += 1
# Creates a bar graph to display the data of the University Year Students
plt.bar(year, year_stats)
plt.title('Year of Study')
plt.ylabel('# of People')
plt.xlabel('Study Years')

plt.show()

# Setting up the data of the Universities (Again, had to change some responses to 'Other' to not show too many responses as labels)
university = ['TMU', 'Other']
university_stats = [0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    # Checks if that specific row in column -4 is not empty
    if row[-4] != '':
        university_stats[university.index(row[-4])] += 1
# Creates a bar graph to show the data of the universities
plt.bar(university, university_stats)
plt.title('University Students')
plt.ylabel('# of People')
plt.xlabel('Universities/Colleges')

plt.show()

# Setting up the data of the faculty (Again, had to change some responses to 'Other' to not show too many responses as labels)
faculty = ['Arts', 'Communication Design', 'Community Services', 'Engineering', 'Science', 'Law', 'Business', 'Other']
faculty_stats = [0, 0, 0, 0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    faculty_stats[faculty.index(row[5])] += 1
# Creates a pie graph to show the data of faculties
plt.pie(faculty_stats, labels = faculty, autopct='%1.1f%%')
plt.title('Faculty')
plt.legend()
plt.show()

# Setting up the data to show the university roles (Again, had to change some responses to 'Other' to not show too many responses as labels)
role = ['Pursuing a diploma', 'Pursuing a Bachelor', 'Pursuing a Master', 'Pursuing a PhD', 'Teaching Assistant', 'Other']
role_stats = [0, 0, 0, 0, 0, 0]
# Setting up a filter to add all the data by one based on their answer
for row in csv_data[1:]:
    # Setting up the current row in column 7 (indexing)
    uni_role = row[7]
    # Splitting each response by comma, in case for multiple answers separated by commas
    string_list = uni_role.split(',')
    # Loops through each response
    for string in string_list:
        # Strips the first whitespace
        string = string.strip()
        # Adds the corresponding data by 1 based on response
        if string == 'Pursuing a diploma':
            role_stats[0] += 1
        if string == 'Pursuing a Bachelor':
            role_stats[1] += 1
        if string == 'Pursuing a Master':
            role_stats[2] += 1
        if string == 'Pursuing a PhD':
            role_stats[3] += 1
        if string == 'Teaching Assistant':
            role_stats[4] += 1
        if string == 'Other':
            role_stats[5] += 1
# Displays the data of the university roles
plt.pie(role_stats, labels = role, autopct='%1.1f%%')
plt.title('Roles')

plt.show()

# Setting up the data of the ChatGPT frequency
chatgpt_spending = ['Every day', 'Few times a week', 'Once a week', 'Very rarely', 'I know of it, but I have never tested it out myself', 'I am not familiar with it']
spending_stats = [0, 0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    spending_stats[chatgpt_spending.index(row[4])] += 1
# Creates a pie graph to show the data of ChatGPT frequency
plt.pie(spending_stats, labels = chatgpt_spending, autopct='%1.1f%%')
plt.title('How often you use ChatGPT?')
plt.show()

# Setting up the data to whether using ChatGPT is cheating (Again, had to change some responses to 'Other' to not show too many responses as labels)
cheating_or_no = ['This line does not exist', 'When you cut the working process in order to reach completion, but you do not actually grasp the content', 'When your assignment lacks your soul (so if ChatGPT would not produce the same result as you in creative disciplines)', 'It depends on the assignment', 'It is difficult to say', 'Other']
cheating_stats = [0, 0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    cheating_stats[cheating_or_no.index(row[8])] += 1
# Creates a pie graph to show the data of when ChatGPT is cheating
plt.pie(cheating_stats, labels = cheating_or_no, autopct='%1.1f%%')
plt.title('When do you think using ChatGPT for an assignment draws the line between working smart and simply not working at all?')
plt.show()

# Setting up the data to explain why people cheat (Again, had to change some responses to 'Other' to not show too many responses as labels)
why_cheating = ['Sheer laziness due to disconnect from learning material', 'Low expectations for success', 'All of the above', 'Other']
why_cheating_stats = [0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    why_cheating_stats[why_cheating.index(row[10])] += 1
# Creates a pie graph to show the data of why using ChatGPT is cheating
plt.pie(why_cheating_stats, labels = why_cheating, autopct='%1.1f%%')
plt.title('Why do students cheat?')
plt.show()

# Setting up the data to explain the problems of using ChatGPT (Again, had to change some responses to 'Other' to not show too many responses as labels)
problems = ['ChatGPT is the main problem', 'Students are the main problem', 'The education system is the main problem', 'Both students and the education system are part of the problem', 'All 3 are part of the problem', 'Other']
problems_stats = [0, 0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    problems_stats[problems.index(row[11])] += 1
# Creates a pie graph to show the data of the problems
plt.pie(problems_stats, labels = problems, autopct='%1.1f%%')
plt.title('Main problem: ChatGPT, students, or education?')
plt.show()

# Setting up the data to explain if ChatGPT is just a tool, or a cheating tool
tool_or_cheat = ['Useful tool', 'Cheating engine']
tool_or_cheat_stats = [0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    tool_or_cheat_stats[tool_or_cheat.index(row[9])] += 1
# Creates a bar graph to show the data of tool or cheat 
plt.bar(tool_or_cheat, tool_or_cheat_stats)
plt.title('Is it a tool, or is it something you can use to cheat with?')
plt.ylabel('# of People')
plt.xlabel('Useful Tool or Cheating Engine?')

plt.show()

# Setting up the data to the use of ChatGPT (Again, had to change some responses to 'Other' to not show too many responses as labels)
uses = ['A research tool', 'A digital tutor providing personalized asynchronous learning', 'Marking assessments', 'It should not be used', 'Other']
uses_stats = [0, 0, 0, 0, 0]
# Setting up a filter to add the data by one based on their answer
for row in csv_data[1:]:
    # Setting up the current row in column -5 (indexing)
    tool = row[-5]
    # Splitting each response by comma, in case for multiple answers separated by commas
    string_list = tool.split(',')
    # Loops through each response
    for string in string_list:
        # Strips the first whitespace
        string = string.strip()
        # Adds the corresponding data by 1 based on response
        if string == 'A research tool':
            uses_stats[0] += 1
        if string == 'A digital tutor providing personalized asynchronous learning':
            uses_stats[1] += 1
        if string == 'Marking assessments':
            uses_stats[2] += 1
        if string == 'It should not be used':
            uses_stats[3] += 1
        if string == 'Other':
            uses_stats[4] += 1
# Displays a pie graph of the ChatGPT uses
plt.pie(uses_stats, labels = uses, autopct='%1.1f%%')
plt.title('Use of ChatGPT')
plt.show()

# Setting up the data to explain what regulations should be implemented (Again, had to change some responses to 'Other' to not show too many responses as labels)
regulations = ['Nothing needs to be done', 'Educating students on the (current) limitations of AI as well as the consequences of plagiarism', 'Surveilling the working process for assignments', 'Holding in person tests as much as possible', 'Changing the grading system', 'It should be banned outright', 'Other']
regulations_stats = [0, 0, 0, 0, 0, 0, 0]
# Setting up a filter to add all the data by one based on their answer
for row in csv_data[1:]:
    # Setting up the current row in column -6 (indexing)
    reg = row[-6]
    # Splitting each response by comma, in case for multiple answers separated by commas
    string_list = reg.split(',')
    # Loops through each response
    for string in string_list:
        # Strips the first whitespace
        string = string.strip()
        # Adds the corresponding data by 1 based on response
        if string == 'Nothing needs to be done':
            regulations_stats[0] += 1
        if string == 'Educating students on the (current) limitations of AI as well as the consequences of plagiarism':
            regulations_stats[1] += 1
        if string == 'Holding in person tests as much as possible':
            regulations_stats[3] += 1
        if string == 'It should be banned outright':
            regulations_stats[5] += 1
        if string == 'Surveilling the working process for assignments':
            regulations_stats[2] += 1
        if string == 'Changing the grading system':
            regulations_stats[4] += 1
        if string == 'Other':
            regulations_stats[6] += 1
# Displays a pie chart of the ChatGPT regulations
plt.pie(regulations_stats, labels = regulations, autopct='%1.1f%%')
plt.title('ChatGPT Regulations')
plt.show()

