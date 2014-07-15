# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class BetBrdmapdat(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=100) # Field name made lowercase.
    dat_file_location = models.CharField(db_column='Dat_file_location', max_length=500) # Field name made lowercase.
    brd_file_location = models.CharField(db_column='Brd_file_location', max_length=500) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'BET_brdmapdat'

class BetCombine(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=80) # Field name made lowercase.
    project_name = models.CharField(db_column='Project Name', max_length=300, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_name = models.CharField(db_column='Part Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.CharField(db_column='Category', max_length=45, blank=True) # Field name made lowercase.
    total_days = models.FloatField(db_column='Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_total_days = models.FloatField(db_column='Estimated Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    adjusted_days = models.FloatField(db_column='Adjusted Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_width = models.FloatField(db_column='Board Width', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_height = models.FloatField(db_column='Board Height', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    metal_to_metal_thickness = models.FloatField(db_column='Metal to Metal Thickness', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    sequential_lam = models.CharField(db_column='Sequential Lam', max_length=3, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_buried = models.CharField(db_column='Via Type:Buried', max_length=3, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_blind = models.CharField(db_column='Via Type:Blind', max_length=3, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_layers = models.IntegerField(db_column='Total Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_layers = models.IntegerField(db_column='Plane Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    pins = models.IntegerField(db_column='Pins', blank=True, null=True) # Field name made lowercase.
    connections = models.IntegerField(db_column='Connections', blank=True, null=True) # Field name made lowercase.
    components = models.IntegerField(db_column='Components', blank=True, null=True) # Field name made lowercase.
    total_nets = models.IntegerField(db_column='Total Nets', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    bga_lgas = models.IntegerField(db_column='BGA/LGAs', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    dimms = models.IntegerField(db_column='DIMMs', blank=True, null=True) # Field name made lowercase.
    pin_density = models.FloatField(blank=True, null=True)
    component_density = models.FloatField(blank=True, null=True)
    buses = models.IntegerField(db_column='Buses', blank=True, null=True) # Field name made lowercase.
    constraintsets = models.IntegerField(db_column='Constraintsets', blank=True, null=True) # Field name made lowercase.
    diffpairs = models.IntegerField(db_column='Diffpairs', blank=True, null=True) # Field name made lowercase.
    matchgroups = models.IntegerField(db_column='Matchgroups', blank=True, null=True) # Field name made lowercase.
    netclasses = models.IntegerField(db_column='Netclasses', blank=True, null=True) # Field name made lowercase.
    net_with_constraints = models.IntegerField(db_column='Net with Constraints', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    pinpairs = models.IntegerField(db_column='Pinpairs', blank=True, null=True) # Field name made lowercase.
    xnets = models.IntegerField(db_column='Xnets', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'BET_combine'

class BetCombine2(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=80) # Field name made lowercase.
    part_name = models.CharField(db_column='Part Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_name = models.CharField(db_column='Project Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.CharField(db_column='Category', max_length=45) # Field name made lowercase.
    total_days = models.FloatField(db_column='Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_total_days = models.FloatField(db_column='Estimated Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    adjusted_days = models.FloatField(db_column='Adjusted Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_width = models.FloatField(db_column='Board Width', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_height = models.FloatField(db_column='Board Height', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    metal_to_metal_thickness = models.FloatField(db_column='Metal to Metal Thickness', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    sequential_lam = models.CharField(db_column='Sequential Lam', max_length=3, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_buried = models.CharField(db_column='Via Type:Buried', max_length=3, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_blind = models.CharField(db_column='Via Type:Blind', max_length=3, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_layers = models.IntegerField(db_column='Total Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_layers = models.IntegerField(db_column='Plane Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    pins = models.IntegerField(db_column='Pins', blank=True, null=True) # Field name made lowercase.
    connections = models.IntegerField(db_column='Connections', blank=True, null=True) # Field name made lowercase.
    components = models.IntegerField(db_column='Components', blank=True, null=True) # Field name made lowercase.
    total_nets = models.IntegerField(db_column='Total Nets', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    bga_lgas = models.IntegerField(db_column='BGA/LGAs', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    dimms = models.IntegerField(db_column='DIMMs', blank=True, null=True) # Field name made lowercase.
    pin_density = models.FloatField(blank=True, null=True)
    component_density = models.FloatField(blank=True, null=True)
    buses = models.IntegerField(db_column='Buses', blank=True, null=True) # Field name made lowercase.
    constraintsets = models.IntegerField(db_column='Constraintsets', blank=True, null=True) # Field name made lowercase.
    diffpairs = models.IntegerField(db_column='Diffpairs', blank=True, null=True) # Field name made lowercase.
    matchgroups = models.IntegerField(db_column='Matchgroups', blank=True, null=True) # Field name made lowercase.
    netclasses = models.IntegerField(db_column='Netclasses', blank=True, null=True) # Field name made lowercase.
    net_with_constraints = models.IntegerField(db_column='Net with Constraints', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    pinpairs = models.IntegerField(db_column='Pinpairs', blank=True, null=True) # Field name made lowercase.
    xnets = models.IntegerField(db_column='Xnets', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'BET_combine2'

class BetPhysicalboard(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=80) # Field name made lowercase.
    part_name = models.CharField(db_column='Part Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    job_start_date = models.DateTimeField(db_column='Job Start Date', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    engineer_sign_off_date = models.DateTimeField(db_column='Engineer Sign-off Date', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    sequential_lam = models.IntegerField(db_column='Sequential Lam', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_width = models.FloatField(db_column='Board Width', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_height = models.FloatField(db_column='Board Height', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_buried = models.IntegerField(db_column='Via Type:Buried', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_blind = models.IntegerField(db_column='Via Type:Blind', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_layers = models.IntegerField(db_column='Total Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    metal_to_metal_thickness = models.FloatField(db_column='Metal to Metal Thickness', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_layers = models.IntegerField(db_column='Plane Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    whizz_time_days = models.FloatField(db_column='Whizz_time_days', blank=True, null=True) # Field name made lowercase.
    overtime_days = models.FloatField(db_column='Overtime / days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    qty_designers = models.FloatField(db_column='Qty designers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    prime_designer_days = models.FloatField(db_column='Prime designer / days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    second_designer_days = models.FloatField(db_column='Second designer / days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_days = models.FloatField(db_column='Total days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_total_days = models.FloatField(db_column='Estimated Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    class Meta:
        managed = False
        db_table = 'BET_physicalboard'

class BetSchematic(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=80) # Field name made lowercase.
    pins = models.IntegerField(db_column='Pins', blank=True, null=True) # Field name made lowercase.
    connections = models.IntegerField(db_column='Connections', blank=True, null=True) # Field name made lowercase.
    components = models.IntegerField(db_column='Components', blank=True, null=True) # Field name made lowercase.
    nets = models.IntegerField(db_column='Nets', blank=True, null=True) # Field name made lowercase.
    layoutarea = models.IntegerField(db_column='Layoutarea', blank=True, null=True) # Field name made lowercase.
    bga_lgas = models.IntegerField(db_column='BGA/LGAs', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    dimms = models.IntegerField(db_column='DIMMs', blank=True, null=True) # Field name made lowercase.
    members = models.IntegerField(db_column='Members', blank=True, null=True) # Field name made lowercase.
    buses = models.IntegerField(db_column='Buses', blank=True, null=True) # Field name made lowercase.
    constraintsets = models.IntegerField(db_column='Constraintsets', blank=True, null=True) # Field name made lowercase.
    diffpairs = models.IntegerField(db_column='Diffpairs', blank=True, null=True) # Field name made lowercase.
    matchgroups = models.IntegerField(db_column='Matchgroups', blank=True, null=True) # Field name made lowercase.
    netclasses = models.IntegerField(db_column='Netclasses', blank=True, null=True) # Field name made lowercase.
    netc = models.IntegerField(db_column='NetC', blank=True, null=True) # Field name made lowercase.
    pinpairs = models.IntegerField(db_column='Pinpairs', blank=True, null=True) # Field name made lowercase.
    xnets = models.IntegerField(db_column='Xnets', blank=True, null=True) # Field name made lowercase.
    keepinx = models.FloatField(db_column='Keepinx', blank=True, null=True) # Field name made lowercase.
    keepiny = models.FloatField(db_column='Keepiny', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'BET_schematic'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'

