from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
	username = CharField(max_length=255, unique=True)
	points = IntegerField(default=0)

	class Meta:
		database = db 

students =[
	{'username' : 'Ali Raza',
	'points' : 9000},
	{'username' : 'Kenneth',
	'points':0},
	{'username' : 'Alina',
	'points' : 500},
]

def add_students():
	for student in students:
		try:
			Student.create(username = student['username'],
				points = student['points'])
		except IntegrityError:
			student_record = Student.get(username = student['username'])
			student_record.points = student['points']
			student_record.save()

def top_student():
	student = Student.select().order_by(Student.points.desc()).get()
	print("Our top student right now is {} and they have {} points".format(student.username, student.points))
	return student

if __name__ == '__main__':
	db.connect()
	db.create_tables([Student], safe=True)
	add_students()
	top_student()