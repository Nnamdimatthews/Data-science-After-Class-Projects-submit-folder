import matplotlib.pyplot as maplt

students_names = ["Nnamdi", "Matti", "Ben", "Ekene", "Jay", "Leroy", "Robert", "James"]
students_marks = [28, 12, 20, 15, 19, 25, 26, 11]

marks_perc = []
for x in students_marks:
    res = (x / 50) * 100
    marks_perc.append(res)

print(marks_perc)

def line_chart_of_students_marks():
   maplt.plot(students_names, students_marks)
   maplt.title("Students Marks Graph")
   maplt.xlabel("Students Names")
   maplt.ylabel("Students Marks")
   maplt.show()

line_chart_of_students_marks()

def percentage_bar_chart():
   maplt.bar(students_names, marks_perc)
   maplt.title("Students' Percentage Graph")
   maplt.xlabel("Students Names")
   maplt.ylabel("Students Percentage")
   maplt.show()
             
percentage_bar_chart()    