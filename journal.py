from peewee import *
import datetime

db = SqliteDatabase('diary.db')

class Entry(Model):
	#content
	content = TextField()
	timestamp = DateTimeField(default=datetime.datetime.now)
	#timestamp

	class Meta:
		database = db

def initialize():
	"""Create the databasse and the table if they dont exist"""
	db.connect()
	db.create_tables([Entry], safe=True)

def menu_loop():
	"""show menu"""

def add_entry():
	"""add an entry"""

def view_entry():
	"""view preivous entries"""

def delete_entry():
	"""delete an entry"""

if __name__ == '__main__':
	initialize
	menu_loop()