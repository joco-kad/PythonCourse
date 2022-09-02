from sqlite3 import connect

conn = connect('mrrobot.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS mrrobot_user')
c.execute('''CREATE TABLE mrrobot_user
			 (username text, password text, mail text)''')

users = [
	('elliot', 'abcde', 'elliot@evilcorp.com'),
	('darlene', 'abcde', 'darlene@fsoc.com'),
	('angela', 'abcde', 'angela@heaven.com')
]

c.executemany("INSERT INTO mrrobot_user VALUES (?, ?, ?)", users)

conn.commit()
conn.close()
