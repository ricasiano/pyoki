import DB

query = DB.DBConnect()

class List:
  def artists(self):
    sql = "SELECT id, name FROM artists ORDER BY name"
    result = query.getAll(sql);
    return self._jsonConvert(result)
  def artistSongs(self, id):
    sql = "SELECT * FROM songs where artist_id = " + str(id)
    result = query.getAll(sql);
    return self._jsonConvert(result)
  def artisAlbums(self, id):
    sql = "SELECT * FROM songs where artist_id = " + str(id)
    result = query.getAll(sql);
    return self._jsonConvert(result)
  def albumSongs(self, id):
    sql = "SELECT * FROM songs where artist_id = " + str(id)
    result = query.getAll(sql);
    return self._jsonConvert(result)
  def _jsonConvert(self, mylist):
    data = [dict(ix) for ix in mylist]
    return data
