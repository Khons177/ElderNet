import MySQLdb
<<<<<<< HEAD
import re
import string
def remove_tag(s):
  s = s.strip(" ")
  return re.sub('\<[^>]+\>', '', s)
class t_database:	
	db=0
	cur=0
=======

class t_database:	
	db = MySQLdb.connect(host="", # your host, usually localhost
                     user="", # your username
                      passwd="", # your password
                      db="") # name of the data base
	cur = db.cursor() 
>>>>>>> 45089bb17c525039b232cd2cb97d9e34b26720a6
	def __init__(self, hostname, username, password, database):
		self.db = MySQLdb.connect(host=hostname, # your host, usually localhost
                     	user=username, # your username
                     	passwd=password, # your password
                     	db=database) # name of the data base
<<<<<<< HEAD
		self.cur = self.db.cursor()
	
	def add_tag(self, tag):
		query = "select id from tags where tag = %s";
		self.cur.execute(query, (tag,))
=======
		self.cur = db.cursor()
	
	def add_tag(self, tag):
		query = "select id from tag where tag = %s";
		self.cur.execute(query, tag)
>>>>>>> 45089bb17c525039b232cd2cb97d9e34b26720a6
		q = -1
		for row in self.cur.fetchall():
			q = row
		if q == -1:
<<<<<<< HEAD
			que = "insert into tags (tag) values (%s)"
<<<<<<< HEAD
			self.cur.execute(que, (tag,))
			q = self.cur.lastrowid
=======
=======
			que = "insert into tag (tag) values (%s)"
>>>>>>> 21b2bce20c1131c7d512f427084b876d7f04d978
			self.cur.execute(que, tag)
			q = self.cur.insert_id()
>>>>>>> 45089bb17c525039b232cd2cb97d9e34b26720a6
			
		return q # should return tag id and add it.
				 # if the tag does exist, just retu
				 # rn tag id!
	
<<<<<<< HEAD


	def add_article(self, name, url, desc, date, tags):
		query = "insert ignore into articles (name, url, simplified, date_p) values (%s, %s, %s, %s)"
		curs = (remove_tag(name), remove_tag(url), remove_tag(desc), date, )
		print (query, curs)
		self.cur.execute(query, curs)
		itemid = self.cur.lastrowid
		#for p in tags:
		#	l = self.add_tag(p)
		#	query = "insert into t_connections (uid_, tid, orig) values (%s, %s, 1)"
		#	curs = (itemid, l, )
		#	self.cur.execute(query, curs)
		
=======
	def add_article(self, name, url, desc, date, tags):
		query = "insert into articles (name, url, simplified, date_p) values (%s, %s, %s, %s)"
		curs = (name, url, desc, date, )
		self.cur.execute(query, curs)
		itemid = self.cur.insert_id()
		for p in tags:
			l = self.add_tag(p)
			query = "insert into t_connections (uid_, tid, orig) values (%s, %s, 1)"
			curs = (itemid, l, )
			self.cur.execute(query, curs)
>>>>>>> 45089bb17c525039b232cd2cb97d9e34b26720a6
		return 1

	def add_user(self, username, password):
		# pass sha256 passwords here!
		query = "insert into users (name, password) values (%s, %s)"
		curs = (username, password, )
		self.cur.execute(query, curs)
	
	def check_user(self, username, password):
		query = "select id from users where name = %s and password = %s"
		curs = (username, password,)
		self.cur.execute(query, curs)
		q = -1
		for row in self.cur.fetchall():
			q = row
		return q
		
	def get_relevant_articles(self, uid):
		query = "select tags.tag from tags, t_connections, users where users.uid_ = t_connection.uid_ and tags.id = t_connections.tid and t_connections.orig = 0 and users.uid_ = %s"
		self.cur.execute(query, uid)
		l = []
		p = []
		for row in self.cur.fetchall():
			# row is tags
			p.append(row)
		for i in p: # To make sure we do not end up modifying cur while doing this
			query = "select articles.name articles.url articles.simplified articles.date_ from articles, users, tags, t_connections where tags.tag = %s and tags.id = t_connections.tid and t_connections.orig = 1 and articles.tid = t_connections.uid_ order by articles.date_p desc limit 15;"
			self.cur.execute(query, i)
			for row in self.cur.fetchall():
				l.append(row)
		return l
		# And we have the articles in l!
	def add_application(version, name, url, pub, desc):
		query = "insert into apps (version, name, url, pub, desc) values ('%s', '%s', '%s', '%s', '%s')"
		dat = (version, name, url, pub, desc,)
		self.cur.execute(query, dat)
	def update_app_url(aid, url):
		query = "update apps set url = '%s' where id = '%s'"
		dat = (url, aid,)
		self.cur.execute(query, dat)

	def update_app_ver(aid, ver):
		query = "update apps set version = '%s' where id = '%s'"
		dat = (ver, aid, )
		self.cur.execute(query, dat)
<<<<<<< HEAD
	def commit_data():
		self.db.commit()


           
=======


>>>>>>> 45089bb17c525039b232cd2cb97d9e34b26720a6
