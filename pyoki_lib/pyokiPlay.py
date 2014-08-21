import DB

query = DB.DBConnect()

class Play:
  def song(self, id):
    sql = "SELECT * FROM songs WHERE id = ?"
    result = query.getOne(sql, id);
    return result
