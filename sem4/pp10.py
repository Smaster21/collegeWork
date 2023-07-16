import sqlite3

conn = sqlite3.connect('pp10.db')
c = conn.cursor()
c.execute('''CREATE TABLE Result(Student_Name text, Enrolment_No text, Semester int,Branch text, Subject text, Grade text)''')

data = [('Xavier', 'E001', 2, 'IT', 'DBMS', 'B'),
        ('ABC', 'E004', 2, 'IT', 'Java', 'A'),
        ('XYZ', 'E104', 6, 'IT', 'Python', 'O'),
        ('PQR', 'E204', 4, 'IT', 'Html', 'A+'),
        ('MNO', 'E304', 8, 'IT', 'OOPj', 'C')]
c.executemany("INSERT INTO Result VALUES (?, ?, ?, ?, ?, ?)", data)
conn.commit()

c.execute("UPDATE Result SET Subject='WT' WHERE Semester=5 AND Subject='WTP'")
conn.commit()

c.execute("DELETE FROM Result WHERE Grade='FF'")
conn.commit()

print("Student_Name, Enrolment_No, Semester, Branch, Subject, Grade")
for row in c.execute("SELECT * FROM Result"):
    print(row)
conn.close()
