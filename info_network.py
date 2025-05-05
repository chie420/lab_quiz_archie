import datetime
name = "Archie Villaceran"
student_id = "211-0970"
date_time = datetime.datetime.now()

print("Name: ", name)
print("Student ID: ", student_id)
print("Date and Time: ", date_time)

issue = input("Slow network")

with open ("networking_issue.txt", "w") as file:
	file.write(issue)
