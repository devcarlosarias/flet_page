import peewee as pw

bd_posgrado = pw.SqliteDatabase("https://github.com/vjcarlosedit/flet_page/raw/main/posgrado.sqlite3")

class Division(pw.Model):
    id_division = pw.TextField(primary_key=True)
    nombre      = pw.TextField()
    ubicacion   = pw.TextField(null=True)
    class Meta:
        database = bd_posgrado

class Responsable(pw.Model):
    id_responsable = pw.TextField(primary_key=True)
    nombre         = pw.TextField()
    grado          = pw.TextField()
    correo         = pw.TextField()
    id_division    = pw.ForeignKeyField(column_name="id_division", field="id_division", model=Division)
    class Meta:
        database = bd_posgrado

class Posgrado(pw.Model):
    id_posgrado = pw.IntegerField(primary_key=True)
    nombre         = pw.TextField()
    tipo           = pw.TextField()
    activo         = pw.TextField()
    snp            = pw.TextField()
    orientacion    = pw.TextField()
    modalidad      = pw.TextField()
    id_division    = pw.ForeignKeyField(column_name="id_division", field="id_division", model=Division)
    id_respondable = pw.ForeignKeyField(column_name="id_responsable", field="id_responsable", model=Responsable)
    class Meta:
        database = bd_posgrado
