class Institute:
    def __init__(self,course,semester):
        self.course = course
        self.semester = semester
	
def display(self):
		print("Course: ",self.course)
		print("Semester: ",self.semester)
		
class Branch(Institute):
	def __init__(self,course,semester,name,en_no):
		Institute.__init__(self,course,semester)
		self.name = name
		self.en_no = en_no
	
	def display(self):
		print("Name: ",self.name)
		print("Enrollment: ",self.en_no)
		super().display()

Z=Branch("B.Tech IT", "4", "safu master", "202103103510083")
Z.display()

	



