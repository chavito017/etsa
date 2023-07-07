# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agendamiento(models.Model):
    hora = models.TimeField(blank=True, null=True)
    lugar = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda la ubicacion de la cita ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre de quien cita ')
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    servicio = models.ForeignKey('Servicio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agendamiento'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoriaservicio(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoriaservicio'


class Categoriataller(models.Model):
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoriataller'


class Contrato(models.Model):
    descripcion = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda los terminos y condiciones de cada contrato ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre del contrato ')
    persona_idpersona = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contrato'


class Cuerpofacrura(models.Model):
    cantidad = models.CharField(max_length=45, blank=True, null=True)
    valorunitariol = models.IntegerField(blank=True, null=True)
    valortotal = models.IntegerField(blank=True, null=True)
    scripcion_idscripcion = models.IntegerField()
    faccabeza = models.ForeignKey('Faccabeza', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cuerpofacrura'


class Departamento(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre de la empresa ')
    direccion = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda la direccion de la empresa ')
    telefono = models.IntegerField(blank=True, null=True, db_comment='guarda el contacto de la empresa ')
    correo = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el correo de la empresa ')
    razonsocial = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre juridico de la empresa')
    catgtall_id = models.IntegerField()
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING)
    categoriataller = models.ForeignKey(Categoriataller, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'empresa'


class Faccabeza(models.Model):
    cliente = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    valor_unitario = models.IntegerField(db_column='valor unitario', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    valortotal = models.IntegerField(blank=True, null=True)
    pagos_tarjetacredito = models.IntegerField()
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'faccabeza'


class Municipio(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ciudad_idciudad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'municipio'


class Pagos(models.Model):
    precio = models.FloatField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    agendamiento = models.ForeignKey(Agendamiento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pagos'


class Servicio(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    categoriaservicio = models.ForeignKey(Categoriaservicio, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servicio'


class Tdocumento(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    abreviatura = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tdocumento'


class Tpempresario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpempresario'


class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    contraseña = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    municipio = models.ForeignKey(Municipio, models.DO_NOTHING)
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)
    tdocumento = models.ForeignKey(Tdocumento, models.DO_NOTHING)
    tpempresario = models.ForeignKey(Tpempresario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'
