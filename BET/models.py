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
from django.contrib import admin
from django.db import models
from django.utils.html import escape
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin import SimpleListFilter
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from datetime import date

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'
        app_label = 'BET'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        app_label = 'BET'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'
        app_label = 'BET'

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
        app_label = 'BET'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        app_label = 'BET'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        app_label = 'BET'

class BetItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    created = models.DateTimeField()
    priority = models.IntegerField()
    difficulty = models.IntegerField()
    done = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'bet_item'
        app_label = 'BET'

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
        app_label = 'BET'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'
        app_label = 'BET'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'
        app_label = 'BET'


class Filter_by_pins(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Pins')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'pins'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('<100', _('<100')),
            ('100--1000', _('100--1000')),
            ('1000--10000', _('1000--10000')),
            ('>10000', _('>10000')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or 'other')
        # to decide how to filter the queryset.
        if self.value() == '<100':
            return queryset.filter(pins__gte=0,
                                    pins__lte=100)
        if self.value() == '100--1000':
            return queryset.filter(pins__gte=101,
                                    pins__lte=1000)
        if self.value() == '1000--10000':
            return queryset.filter(pins__gte=1001,
                                    pins__lte=10000)
        if self.value() == '>10000':
            return queryset.filter(pins__gte=10001)

class Filter_by_total_days(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Total_days')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'Total_days'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('<10', _('<10')),
            ('10--100', _('10--100')),
            ('>100', _('>100')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or 'other')
        # to decide how to filter the queryset.
        if self.value() == '<10':
            return queryset.filter(total_days__gte=0,
                                    total_days__lte=10)
        if self.value() == '10--100':
            return queryset.filter(total_days__gte=11,
                                    total_days__lte=100)
        if self.value() == '>100':
            return queryset.filter(total_days__gte=101)


class Combine(models.Model):
    part_number = models.CharField(db_column='Part_number', max_length=80, primary_key=True) # Field name made lowercase.
    part_name = models.CharField(db_column='Part Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_name = models.CharField(db_column='Project Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.CharField(db_column='Category', max_length=45) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_days = models.FloatField(db_column='Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_total_days = models.FloatField(db_column='Estimated Total Days', blank=True, null=True) # Field name made lowercase.
    adjusted_total_days = models.FloatField(db_column='Adjusted Days', blank=True, null=True) # Field name made lowercase.
    board_width = models.FloatField(db_column='Board Width', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_height = models.FloatField(db_column='Board Height', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    metal_to_metal_thickness = models.FloatField(db_column='Metal to Metal Thickness', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    sequential_lam = models.CharField(db_column='Sequential Lam', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_buried = models.CharField(db_column='Via Type:Buried', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_blind = models.CharField(db_column='Via Type:Blind', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
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
    #     managed = False
    #     db_table = 'combine'
         app_label = 'BET'


class Combine2(models.Model):
    part_number = models.CharField(db_column='Part_number', max_length=80, primary_key=True) # Field name made lowercase.
    part_name = models.CharField(db_column='Part Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    project_name = models.CharField(db_column='Project Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.CharField(db_column='Category', max_length=45) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_days = models.FloatField(db_column='Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_total_days = models.FloatField(db_column='Estimated Total Days', blank=True, null=True) # Field name made lowercase.
    adjusted_total_days = models.FloatField(db_column='Adjusted Days', blank=True, null=True) # Field name made lowercase.
    board_width = models.FloatField(db_column='Board Width', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_height = models.FloatField(db_column='Board Height', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    metal_to_metal_thickness = models.FloatField(db_column='Metal to Metal Thickness', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    sequential_lam = models.CharField(db_column='Sequential Lam', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_buried = models.CharField(db_column='Via Type:Buried', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_blind = models.CharField(db_column='Via Type:Blind', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_layers = models.IntegerField(db_column='Total Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_layers = models.IntegerField(db_column='Plane Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    pins = models.IntegerField(db_column='Pins', blank=True, null=True) # Field name made lowercase.
    connections = models.IntegerField(db_column='Connections', blank=True, null=True) # Field name made lowercase.
    components = models.IntegerField(db_column='Components', blank=True, null=True) # Field name made lowercase.
    nets = models.IntegerField(db_column='Nets', blank=True, null=True) # Field name made lowercase.
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
    #     managed = False
    #     db_table = 'combine'
         app_label = 'BET'

class CombineAdmin(admin.ModelAdmin):
    # list_display = ["part_number", "part_name", "board_width","board_height","keepinx","keepiny","total_layers","metal_to_metal_thickness",\
    #                 "total_days","pins","connections","pin_density","component_density",'buses','constraintsets','diffpairs','matchgroups','netclasses','netc','pinpairs','xnets']
    list_display = ["part_number", "part_name",\
                "total_days","board_width","board_height","pins",'buses','constraintsets','diffpairs','matchgroups','netclasses','net_with_constraints','pinpairs','xnets']
    search_fields = ["part_number","total_days","pins"]
    list_filter = (Filter_by_pins,Filter_by_total_days)
admin.site.register(Combine, CombineAdmin)

class PartInfo(models.Model):
    partnumber = models.CharField(db_column='partNumber', max_length=16, blank=True) # Field name made lowercase.
    partname = models.CharField(db_column='partName', max_length=50, blank=True) # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50, blank=True) # Field name made lowercase.
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dimensionsuom = models.CharField(db_column='dimensionsUOM', max_length=6, blank=True) # Field name made lowercase.
    thickness = models.FloatField(blank=True, null=True)
    thicknesstolerance = models.FloatField(db_column='thicknessTolerance', blank=True, null=True) # Field name made lowercase.
    thicknessuom = models.CharField(db_column='thicknessUOM', max_length=6, blank=True) # Field name made lowercase.
    estimatedtotallayers = models.IntegerField(db_column='estimatedTotalLayers', blank=True, null=True) # Field name made lowercase.
    boarddensity = models.CharField(db_column='boardDensity', max_length=6, blank=True) # Field name made lowercase.
    boarddensitycomment = models.CharField(db_column='boardDensityComment', max_length=80, blank=True) # Field name made lowercase.
    activecomponents = models.CharField(db_column='activeComponents', max_length=11, blank=True) # Field name made lowercase.
    telcordiarequired = models.CharField(db_column='telcordiaRequired', max_length=3, blank=True) # Field name made lowercase.
    telcordiarequiredcomment = models.CharField(db_column='telcordiaRequiredComment', max_length=80, blank=True) # Field name made lowercase.
    oldassemblymethod = models.CharField(db_column='oldAssemblyMethod', max_length=19, blank=True) # Field name made lowercase.
    intendedassemblymethodcomment = models.CharField(db_column='intendedAssemblyMethodComment', max_length=80, blank=True) # Field name made lowercase.
    contactfingers = models.CharField(db_column='contactFingers', max_length=40, blank=True) # Field name made lowercase.
    contactfingerscomment = models.CharField(db_column='contactFingersComment', max_length=80, blank=True) # Field name made lowercase.
    regularfeaturescomment = models.CharField(db_column='regularFeaturesComment', max_length=80, blank=True) # Field name made lowercase.
    viatypescomment = models.CharField(db_column='viaTypesComment', max_length=80, blank=True) # Field name made lowercase.
    totalholes = models.IntegerField(db_column='totalHoles', blank=True, null=True) # Field name made lowercase.
    unfilledthruholesize = models.FloatField(db_column='unfilledThruHoleSize', blank=True, null=True) # Field name made lowercase.
    dielectricmaterials = models.CharField(db_column='dielectricMaterials', max_length=30, blank=True) # Field name made lowercase.
    dielectricmaterialscomment = models.CharField(db_column='dielectricMaterialsComment', max_length=80, blank=True) # Field name made lowercase.
    primaryfinish = models.CharField(db_column='primaryFinish', max_length=40, blank=True) # Field name made lowercase.
    primaryfinishcomment = models.CharField(db_column='primaryFinishComment', max_length=80, blank=True) # Field name made lowercase.
    assemblyreflowalloy = models.CharField(db_column='assemblyReflowAlloy', max_length=40, blank=True) # Field name made lowercase.
    intendedassemblymethod = models.CharField(db_column='intendedAssemblyMethod', max_length=40, blank=True) # Field name made lowercase.
    unfilledthruholequantity = models.IntegerField(db_column='unfilledThruHoleQuantity', blank=True, null=True) # Field name made lowercase.
    filledthruholesize = models.FloatField(db_column='filledThruHoleSize', blank=True, null=True) # Field name made lowercase.
    filledthruholequantity = models.IntegerField(db_column='filledThruHoleQuantity', blank=True, null=True) # Field name made lowercase.
    blindtop2viasize = models.FloatField(db_column='blindTop2ViaSize', blank=True, null=True) # Field name made lowercase.
    blindtop2viaquantity = models.IntegerField(db_column='blindTop2ViaQuantity', blank=True, null=True) # Field name made lowercase.
    blindtop3viasize = models.FloatField(db_column='blindTop3ViaSize', blank=True, null=True) # Field name made lowercase.
    blindtop3viaquantity = models.IntegerField(db_column='blindTop3ViaQuantity', blank=True, null=True) # Field name made lowercase.
    blindbottom2viasize = models.FloatField(db_column='blindBottom2ViaSize', blank=True, null=True) # Field name made lowercase.
    blindbottom2viaquantity = models.IntegerField(db_column='blindBottom2ViaQuantity', blank=True, null=True) # Field name made lowercase.
    blindbottom3viasize = models.FloatField(db_column='blindBottom3ViaSize', blank=True, null=True) # Field name made lowercase.
    blindbottom3viaquantity = models.IntegerField(db_column='blindBottom3ViaQuantity', blank=True, null=True) # Field name made lowercase.
    buriedviasize = models.FloatField(db_column='buriedViaSize', blank=True, null=True) # Field name made lowercase.
    buriedviaquantity = models.IntegerField(db_column='buriedViaQuantity', blank=True, null=True) # Field name made lowercase.
    buriedviacorequantity = models.IntegerField(db_column='buriedViaCoreQuantity', blank=True, null=True) # Field name made lowercase.
    dimmquantity = models.IntegerField(db_column='dimmQuantity', blank=True, null=True) # Field name made lowercase.
    tiebarspermitted = models.CharField(db_column='tieBarsPermitted', max_length=4, blank=True) # Field name made lowercase.
    maxdf = models.FloatField(db_column='maxDf', blank=True, null=True) # Field name made lowercase.
    subpanelsize = models.CharField(db_column='subpanelSize', max_length=30, blank=True) # Field name made lowercase.
    subpanelimages = models.IntegerField(db_column='subpanelImages', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = 'false'
        db_table = 'bet_PartInfo'
        app_label = 'BET'

class Physicalboard(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=80) # Field name made lowercase.
    part_name = models.CharField(db_column='Part Name', max_length=300, blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
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
    estimated_total_days = models.FloatField(db_column='Estimated Total Days', blank=True, null=True)
    def __str__(self):
        return self.part_number
    # created = models.ForeignKey(Task)
    # class Meta:
    #
    #     managed = False
    #     db_table = 'physicalboard'

class PhysicalAdmin(admin.ModelAdmin):
    list_display = ["part_number", "part_name", "job_start_date", "engineer_sign_off_date", "board_width","board_height","total_layers","metal_to_metal_thickness","total_days"]
    search_fields = ["part_number"]

admin.site.register(Physicalboard, PhysicalAdmin)

class Schematic(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=80) # Field name made lowercase.
    pins = models.IntegerField(db_column='Pins', blank=True, null=True) # Field name made lowercase.
    connections = models.IntegerField(db_column='Connections', blank=True, null=True) # Field name made lowercase.
    components = models.IntegerField(db_column='Components', blank=True, null=True) # Field name made lowercase.
    nets = models.IntegerField(db_column='Nets', blank=True, null=True) # Field name made lowercase.
    layoutarea = models.IntegerField(db_column='Layoutarea', blank=True, null=True) # Field name made lowercase.
    bga_lgas = models.IntegerField(db_column='BGA/LGAs', blank=True, null=True,verbose_name='BGA/LGAs') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dimms = models.IntegerField(db_column='DIMMs', blank=True, null=True,verbose_name='DIMMs') # Field name made lowercase.
    members = models.IntegerField(db_column='Members', blank=True, null=True,verbose_name='Members')
    buses = models.IntegerField(db_column='Buses', blank=True, null=True)
    constraintsets = models.IntegerField(db_column='Constraintsets', blank=True, null=True)
    diffpairs = models.IntegerField(db_column='Diffpairs', blank=True, null=True)
    matchgroups = models.IntegerField(db_column='Matchgroups', blank=True, null=True)
    netclasses = models.IntegerField(db_column='Netclasses', blank=True, null=True)
    netc = models.IntegerField(db_column='NetC', blank=True, null=True)
    pinpairs = models.IntegerField(db_column='Pinpairs', blank=True, null=True)
    xnets = models.IntegerField(db_column='Xnets', blank=True, null=True)
    keepinx = models.FloatField(db_column='Keepinx', blank=True, null=True,verbose_name='KeepinX')
    keepiny = models.FloatField(db_column='Keepiny', blank=True, null=True,verbose_name='KeepinY')
    def __str__(self):
        return self.part_number
    # created = models.ForeignKey(Task)
    class Meta:
        app_label = 'BET'
    #     managed = False
    #     db_table = 'schematic'

class SchematicAdmin(admin.ModelAdmin):
    list_display = ["part_number", "pins", "connections", "components", "nets","layoutarea","dimms","bga_lgas","members"]
    search_fields = ["part_number"]
    list_filter =["pins"]
admin.site.register(Schematic, SchematicAdmin)

#------------------------------------------the todolist example-------------------------------------------------------
# class Summaryreport(models.Model):
#     part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=80) # Field name made lowercase.
#     pins = models.IntegerField(db_column='Pins', blank=True, null=True) # Field name made lowercase.
#     connections = models.IntegerField(db_column='Connections', blank=True, null=True) # Field name made lowercase.
#     components = models.IntegerField(db_column='Components', blank=True, null=True) # Field name made lowercase.
#     nets = models.IntegerField(db_column='Nets', blank=True, null=True) # Field name made lowercase.
#     layoutarea = models.IntegerField(db_column='Layoutarea', blank=True, null=True) # Field name made lowercase.
#     bga_lgas = models.IntegerField(db_column='BGA/LGAs', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
#     dimms = models.IntegerField(db_column='DIMMs', blank=True, null=True) # Field name made lowercase.
#     created = models.ForeignKey(DateTime)
#
    # class Meta:
    #
    #     managed = False
    #     db_table = 'summaryreport'
#
# class SummaryAdmin(admin.ModelAdmin):
#     list_display = ["part_number", "pins", "connections", "components", "nets","layoutarea"]
#     search_fields = ["part_number"]
# admin.site.register(Summaryreport, SummaryAdmin)

# class Item(models.Model):
#     name = models.CharField(max_length=60)
#     created = models.ForeignKey(DateTime)
#     priority = models.IntegerField(default=0)
#     difficulty = models.IntegerField(default=0)
#     done = models.BooleanField(default=False)
#
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ["name", "priority", "difficulty", "created", "done"]
#     search_fields = ["name"]

# class ReportInline(admin.TabularInline):
#     model = Schematic
#     model2 = Physicalboard

# class Task(models.Model):
#     physicalboard=models.ForeignKey(Physicalboard)
#     schematic=models.ManyToManyField(Schematic)
#     def __unicode__(self):
#         return unicode(self.physicalboard.part_number)

#defining a class associating Part_number and location of a specific board
class Brdmapdat(models.Model):
    part_number = models.CharField(db_column='Part_number', primary_key=True, max_length=100) # Field name made lowercase.
    dat_file_location = models.CharField(db_column='Dat_file_location', max_length=500, blank=True) # Field name made lowercase.
    brd_file_location = models.CharField(db_column='Brd_file_location', max_length=500, blank=True) # Field name made lowercase.

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ["physicalboard"]
# admin.site.register(Task, TaskAdmin)


