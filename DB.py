import sqlite3 as sql
con = sql.connect('Pyoki.db')

class DBConnect:
  def getOne(self, query, id):
    with con:
      con.row_factory = sql.Row
      cur = con.cursor()    
      cur.execute(query, (id,))
      row = cur.fetchone()
      return row
  def getAll(self, query):
    with con:
      con.row_factory = sql.Row
      cur = con.cursor()    
      cur.execute(query)
      rows = cur.fetchall()
      return rows
