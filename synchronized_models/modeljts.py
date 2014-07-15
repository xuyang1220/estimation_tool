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

class Atepackage(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    typeofoutput = models.CharField(db_column='typeOfOutput', max_length=5, blank=True) # Field name made lowercase.
    typeofoutputcomment = models.CharField(db_column='typeOfOutputComment', max_length=80, blank=True) # Field name made lowercase.
    numberofcopies = models.IntegerField(db_column='numberOfCopies', blank=True, null=True) # Field name made lowercase.
    numberofcopiescomment = models.CharField(db_column='numberOfCopiesComment', max_length=80, blank=True) # Field name made lowercase.
    filmaccount = models.CharField(db_column='filmAccount', max_length=20, blank=True) # Field name made lowercase.
    filmaccountcomment = models.CharField(db_column='filmAccountComment', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ATEPackage'

class Advanced(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    secondaryfinish = models.CharField(db_column='secondaryFinish', max_length=40, blank=True) # Field name made lowercase.
    secondaryfinishcomment = models.CharField(db_column='secondaryFinishComment', max_length=80, blank=True) # Field name made lowercase.
    specialpackagesusedcomment = models.CharField(db_column='specialPackagesUsedComment', max_length=80, blank=True) # Field name made lowercase.
    constructioncomment = models.CharField(db_column='constructionComment', max_length=80, blank=True) # Field name made lowercase.
    stackupcomment = models.TextField(db_column='stackupComment', blank=True) # Field name made lowercase.
    scoring = models.CharField(max_length=3, blank=True)
    scoringcomment = models.CharField(db_column='scoringComment', max_length=80, blank=True) # Field name made lowercase.
    fabdrawingrequired = models.CharField(db_column='fabDrawingRequired', max_length=3, blank=True) # Field name made lowercase.
    fabdrawingrequiredcomment = models.CharField(db_column='fabDrawingRequiredComment', max_length=80, blank=True) # Field name made lowercase.
    costadders = models.TextField(db_column='costAdders', blank=True) # Field name made lowercase.
    pressfitcompliantvhdm = models.CharField(db_column='pressFitCompliantVHDM', max_length=3, blank=True) # Field name made lowercase.
    insertionvhdm = models.CharField(db_column='insertionVHDM', max_length=6, blank=True) # Field name made lowercase.
    probepoints = models.CharField(db_column='probePoints', max_length=3, blank=True) # Field name made lowercase.
    cubalancing = models.CharField(db_column='cuBalancing', max_length=15, blank=True) # Field name made lowercase.
    lga1mmsocketquantity = models.IntegerField(db_column='lga1MMSocketQuantity', blank=True, null=True) # Field name made lowercase.
    lgaothersocketquantity = models.IntegerField(db_column='lgaOtherSocketQuantity', blank=True, null=True) # Field name made lowercase.
    stackupfrozen = models.CharField(db_column='stackupFrozen', max_length=4, blank=True) # Field name made lowercase.
    prepregrestrictions = models.CharField(db_column='prepregRestrictions', max_length=12, blank=True) # Field name made lowercase.
    forcefabnotes = models.TextField(db_column='forceFabNotes', blank=True) # Field name made lowercase.
    blockfabnotes = models.TextField(db_column='blockFabNotes', blank=True) # Field name made lowercase.
    uniquenotetext = models.TextField(db_column='uniqueNoteText', blank=True) # Field name made lowercase.
    designercomment = models.TextField(db_column='designerComment', blank=True) # Field name made lowercase.
    checkercomment = models.TextField(db_column='checkerComment', blank=True) # Field name made lowercase.
    vendorcomment = models.TextField(db_column='vendorComment', blank=True) # Field name made lowercase.
    longtermcomment = models.TextField(db_column='longTermComment', blank=True) # Field name made lowercase.
    brdsignature = models.CharField(db_column='brdSignature', max_length=30, blank=True) # Field name made lowercase.
    brdstatus = models.CharField(db_column='brdStatus', max_length=20, blank=True) # Field name made lowercase.
    teardropping = models.CharField(max_length=4, blank=True)
    cuthieving = models.CharField(db_column='cuThieving', max_length=4, blank=True) # Field name made lowercase.
    designertodesignercomment = models.TextField(db_column='designerToDesignerComment', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Advanced'

class Appcorebiblio(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    describeddocument = models.CharField(db_column='describedDocument', max_length=40, blank=True) # Field name made lowercase.
    title = models.CharField(max_length=160, blank=True)
    comments = models.TextField(blank=True)
    importance = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'AppCoreBiblio'

class Approval(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    owningjob = models.CharField(db_column='owningJob', max_length=40, blank=True) # Field name made lowercase.
    enteringuser = models.CharField(db_column='enteringUser', max_length=40, blank=True) # Field name made lowercase.
    stagetag = models.CharField(db_column='stageTag', max_length=35, blank=True) # Field name made lowercase.
    steptag = models.CharField(db_column='stepTag', max_length=35, blank=True) # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True)
    entered = models.DateTimeField(blank=True, null=True)
    shortcomment = models.CharField(db_column='shortComment', max_length=160, blank=True) # Field name made lowercase.
    longcomment = models.TextField(db_column='longComment', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Approval'

class Assemblycopy(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    targetassembly = models.CharField(db_column='targetAssembly', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AssemblyCopy'

class Assemblydoc(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    typeofoutput = models.CharField(db_column='typeOfOutput', max_length=20, blank=True) # Field name made lowercase.
    typeofoutputcomments = models.CharField(db_column='typeOfOutputComments', max_length=80, blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AssemblyDoc'

class Assemblyjob(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    assemblynumber = models.CharField(db_column='assemblyNumber', max_length=16, blank=True) # Field name made lowercase.
    assemblyname = models.CharField(db_column='assemblyName', max_length=50, blank=True) # Field name made lowercase.
    assemblytype = models.CharField(db_column='assemblyType', max_length=20, blank=True) # Field name made lowercase.
    parentassemblynumber = models.CharField(db_column='parentAssemblyNumber', max_length=16, blank=True) # Field name made lowercase.
    designnumber = models.CharField(db_column='designNumber', max_length=16, blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True) # Field name made lowercase.
    econumber = models.CharField(db_column='ecoNumber', max_length=30, blank=True) # Field name made lowercase.
    nostufflocations = models.CharField(db_column='noStuffLocations', max_length=4, blank=True) # Field name made lowercase.
    socketlocations = models.CharField(db_column='socketLocations', max_length=4, blank=True) # Field name made lowercase.
    shuntlocations = models.CharField(db_column='shuntLocations', max_length=4, blank=True) # Field name made lowercase.
    typeofoutput = models.CharField(db_column='typeOfOutput', max_length=20, blank=True) # Field name made lowercase.
    typeofoutputcomment = models.CharField(db_column='typeOfOutputComment', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AssemblyJob'

class Assemblyrsvp(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    numberofecr = models.CharField(db_column='numberOfECR', max_length=14, blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AssemblyRSVP'

class Attachment(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=20, blank=True)
    datavalue = models.CharField(db_column='dataValue', max_length=100, blank=True) # Field name made lowercase.
    comments = models.CharField(max_length=160, blank=True)
    entered = models.DateTimeField(blank=True, null=True)
    attachinguser = models.CharField(db_column='attachingUser', max_length=40, blank=True) # Field name made lowercase.
    targetpersistent = models.CharField(db_column='targetPersistent', max_length=40, blank=True) # Field name made lowercase.
    attachedpersistent = models.CharField(db_column='attachedPersistent', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Attachment'

class Bibliorelationship(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    biblio = models.CharField(max_length=40, blank=True)
    entity = models.CharField(max_length=40, blank=True)
    relationship = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'BiblioRelationship'

class Boardcharacteristics(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dimensionsuom = models.CharField(db_column='dimensionsUOM', max_length=6, blank=True) # Field name made lowercase.
    breakawaytabs = models.CharField(db_column='breakAwayTabs', max_length=3, blank=True) # Field name made lowercase.
    breakawaytabscomment = models.CharField(db_column='breakAwayTabsComment', max_length=80, blank=True) # Field name made lowercase.
    thickness = models.FloatField(blank=True, null=True)
    thicknesstolerance = models.FloatField(db_column='thicknessTolerance', blank=True, null=True) # Field name made lowercase.
    thicknessuom = models.CharField(db_column='thicknessUOM', max_length=6, blank=True) # Field name made lowercase.
    estimatedtotallayers = models.IntegerField(db_column='estimatedTotalLayers', blank=True, null=True) # Field name made lowercase.
    boarddensity = models.CharField(db_column='boardDensity', max_length=6, blank=True) # Field name made lowercase.
    boarddensitycomment = models.CharField(db_column='boardDensityComment', max_length=80, blank=True) # Field name made lowercase.
    activecomponents = models.CharField(db_column='activeComponents', max_length=11, blank=True) # Field name made lowercase.
    activecomponentscomment = models.CharField(db_column='activeComponentsComment', max_length=80, blank=True) # Field name made lowercase.
    telcordiarequired = models.CharField(db_column='telcordiaRequired', max_length=3, blank=True) # Field name made lowercase.
    telcordiarequiredcomment = models.CharField(db_column='telcordiaRequiredComment', max_length=80, blank=True) # Field name made lowercase.
    oldassemblymethod = models.CharField(db_column='oldAssemblyMethod', max_length=19, blank=True) # Field name made lowercase.
    intendedassemblymethodcomment = models.CharField(db_column='intendedAssemblyMethodComment', max_length=80, blank=True) # Field name made lowercase.
    onboardcomment = models.CharField(db_column='onboardComment', max_length=80, blank=True) # Field name made lowercase.
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
        managed = False
        db_table = 'BoardCharacteristics'

class Bookmark(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    auserentity = models.CharField(db_column='aUserEntity', max_length=40, blank=True) # Field name made lowercase.
    rememberedpersistent = models.CharField(db_column='rememberedPersistent', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Bookmark'

class Brdcopy(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'BrdCopy'

class Checktask(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    taskdesignjob = models.CharField(db_column='taskDesignJob', max_length=40, blank=True) # Field name made lowercase.
    updated = models.DateTimeField(blank=True, null=True)
    tasktag = models.CharField(db_column='taskTag', max_length=80, blank=True) # Field name made lowercase.
    designerstatus = models.CharField(db_column='designerStatus', max_length=10, blank=True) # Field name made lowercase.
    checkerstatus = models.CharField(db_column='checkerStatus', max_length=10, blank=True) # Field name made lowercase.
    needsstatus = models.CharField(db_column='needsStatus', max_length=10, blank=True) # Field name made lowercase.
    hasstatus = models.CharField(db_column='hasStatus', max_length=10, blank=True) # Field name made lowercase.
    designinfo = models.TextField(db_column='designInfo', blank=True) # Field name made lowercase.
    designinfohistory = models.TextField(db_column='designInfoHistory', blank=True) # Field name made lowercase.
    comment = models.TextField(blank=True)
    commenthistory = models.TextField(db_column='commentHistory', blank=True) # Field name made lowercase.
    commentmarkup = models.TextField(db_column='commentMarkup', blank=True) # Field name made lowercase.
    resultdetails = models.TextField(db_column='resultDetails', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CheckTask'

class Checktaskold(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    taskdesignjob = models.CharField(db_column='taskDesignJob', max_length=40, blank=True) # Field name made lowercase.
    updated = models.DateTimeField(blank=True, null=True)
    tasktag = models.CharField(db_column='taskTag', max_length=80, blank=True) # Field name made lowercase.
    designerstatus = models.CharField(db_column='designerStatus', max_length=10, blank=True) # Field name made lowercase.
    checkerstatus = models.CharField(db_column='checkerStatus', max_length=10, blank=True) # Field name made lowercase.
    needsstatus = models.CharField(db_column='needsStatus', max_length=10, blank=True) # Field name made lowercase.
    hasstatus = models.CharField(db_column='hasStatus', max_length=10, blank=True) # Field name made lowercase.
    designinfo = models.TextField(db_column='designInfo', blank=True) # Field name made lowercase.
    designinfohistory = models.TextField(db_column='designInfoHistory', blank=True) # Field name made lowercase.
    comment = models.TextField(blank=True)
    commenthistory = models.TextField(db_column='commentHistory', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CheckTaskOld'

class Compelectric(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    receivingvendorscomment = models.CharField(db_column='receivingVendorsComment', max_length=80, blank=True) # Field name made lowercase.
    vendorcontact = models.CharField(db_column='vendorContact', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CompElectric'

class Compositevalue(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    category = models.CharField(max_length=20, blank=True)
    valuekey = models.CharField(db_column='valueKey', max_length=20, blank=True) # Field name made lowercase.
    optionaldatavalue = models.CharField(db_column='optionalDataValue', max_length=20, blank=True) # Field name made lowercase.
    maindatavalue = models.CharField(db_column='mainDataValue', max_length=20, blank=True) # Field name made lowercase.
    targetpersistent = models.CharField(db_column='targetPersistent', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CompositeValue'

class Core(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    coretype = models.CharField(db_column='coreType', max_length=50, blank=True) # Field name made lowercase.
    dielectricthickness = models.CharField(db_column='dielectricThickness', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Core'

class Coredata(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    coretype = models.CharField(db_column='coreType', max_length=50, blank=True) # Field name made lowercase.
    dielectricthickness = models.FloatField(db_column='dielectricThickness', blank=True, null=True) # Field name made lowercase.
    materialtype = models.CharField(db_column='materialType', max_length=30, blank=True) # Field name made lowercase.
    materialcomment = models.CharField(db_column='materialComment', max_length=80, blank=True) # Field name made lowercase.
    thicknesscontrol = models.CharField(db_column='thicknessControl', max_length=40, blank=True) # Field name made lowercase.
    dk = models.FloatField(blank=True, null=True)
    fdk = models.FloatField(db_column='fDk', blank=True, null=True) # Field name made lowercase.
    df = models.FloatField(blank=True, null=True)
    fdf = models.FloatField(db_column='fDf', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CoreData'

class Designcopy(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    targetdesign = models.CharField(db_column='targetDesign', max_length=40, blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DesignCopy'

class Designjob(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    partnumber = models.CharField(db_column='partNumber', max_length=16, blank=True) # Field name made lowercase.
    partname = models.CharField(db_column='partName', max_length=50, blank=True) # Field name made lowercase.
    designtype = models.CharField(db_column='designType', max_length=20, blank=True) # Field name made lowercase.
    lifecyclephase = models.CharField(db_column='lifeCyclePhase', max_length=40, blank=True) # Field name made lowercase.
    intendedboardusage = models.CharField(db_column='intendedBoardUsage', max_length=16, blank=True) # Field name made lowercase.
    intendedboardusagecomment = models.CharField(db_column='intendedBoardUsageComment', max_length=80, blank=True) # Field name made lowercase.
    parentpartnumber = models.CharField(db_column='parentPartNumber', max_length=16, blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True) # Field name made lowercase.
    requesteddesigner = models.CharField(db_column='requestedDesigner', max_length=50, blank=True) # Field name made lowercase.
    requestedstart = models.DateTimeField(db_column='requestedStart', blank=True, null=True) # Field name made lowercase.
    actualstart = models.DateTimeField(db_column='actualStart', blank=True, null=True) # Field name made lowercase.
    estimatedlayouttimevalue = models.IntegerField(db_column='estimatedLayoutTimeValue', blank=True, null=True) # Field name made lowercase.
    estimatedlayouttimeunits = models.CharField(db_column='estimatedLayoutTimeUnits', max_length=6, blank=True) # Field name made lowercase.
    econumber = models.CharField(db_column='ecoNumber', max_length=30, blank=True) # Field name made lowercase.
    workgroupsvectorcomment = models.CharField(db_column='workGroupsVectorComment', max_length=80, blank=True) # Field name made lowercase.
    customerbu = models.CharField(db_column='customerBU', max_length=40, blank=True) # Field name made lowercase.
    customerbucomment = models.CharField(db_column='customerBUComment', max_length=80, blank=True) # Field name made lowercase.
    spmemail = models.CharField(db_column='spmEMail', max_length=40, blank=True) # Field name made lowercase.
    assemblyvendor = models.CharField(db_column='assemblyVendor', max_length=40, blank=True) # Field name made lowercase.
    assemblyvendorcomment = models.CharField(db_column='assemblyVendorComment', max_length=80, blank=True) # Field name made lowercase.
    leadfree = models.CharField(db_column='leadFree', max_length=3, blank=True) # Field name made lowercase.
    leadfreecomment = models.CharField(db_column='leadFreeComment', max_length=80, blank=True) # Field name made lowercase.
    certification = models.CharField(max_length=60, blank=True)
    chargeto = models.CharField(db_column='chargeTo', max_length=12, blank=True) # Field name made lowercase.
    queuerank = models.IntegerField(db_column='queueRank', blank=True, null=True) # Field name made lowercase.
    marker1 = models.CharField(max_length=40, blank=True)
    marker2 = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'DesignJob'

class Designpackage(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    targetdesign = models.CharField(db_column='targetDesign', max_length=40, blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True) # Field name made lowercase.
    optionalemail = models.CharField(db_column='optionalEMail', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DesignPackage'

class Designrsvp(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    ecrnumber = models.CharField(db_column='ecrNumber', max_length=50, blank=True) # Field name made lowercase.
    ecrnumbercomments = models.CharField(db_column='ecrNumberComments', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DesignRSVP'

class Eventlogentry(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    target = models.CharField(max_length=40, blank=True)
    eventtag = models.CharField(db_column='eventTag', max_length=30, blank=True) # Field name made lowercase.
    eventtime = models.DateTimeField(db_column='eventTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'EventLogEntry'

class Fabcopy(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    typeofoutput = models.CharField(db_column='typeOfOutput', max_length=20, blank=True) # Field name made lowercase.
    typeofoutputcomments = models.CharField(db_column='typeOfOutputComments', max_length=80, blank=True) # Field name made lowercase.
    numberofcopies = models.IntegerField(db_column='numberOfCopies', blank=True, null=True) # Field name made lowercase.
    numberofcopiescomments = models.CharField(db_column='numberOfCopiesComments', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FabCopy'

class Fabpackage(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    receivingvendorscomment = models.CharField(db_column='receivingVendorsComment', max_length=80, blank=True) # Field name made lowercase.
    typeofoutput = models.CharField(db_column='typeOfOutput', max_length=14, blank=True) # Field name made lowercase.
    typeofoutputcomment = models.CharField(db_column='typeOfOutputComment', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FabPackage'

class Faxattachment(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    faxjob = models.CharField(db_column='faxJob', max_length=40, blank=True) # Field name made lowercase.
    faxitem = models.CharField(db_column='faxItem', max_length=40, blank=True) # Field name made lowercase.
    title = models.CharField(max_length=80, blank=True)
    basereference = models.CharField(db_column='baseReference', max_length=255, blank=True) # Field name made lowercase.
    directorymode = models.IntegerField(db_column='directoryMode', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FaxAttachment'

class Faxitem(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    parentfax = models.CharField(db_column='parentFax', max_length=40, blank=True) # Field name made lowercase.
    subject = models.CharField(max_length=80, blank=True)
    itemnumber = models.IntegerField(db_column='itemNumber', blank=True, null=True) # Field name made lowercase.
    ownershipee = models.CharField(db_column='ownershipEE', max_length=4, blank=True) # Field name made lowercase.
    issue = models.TextField(blank=True)
    suggestion = models.TextField(blank=True)
    suggestionlog = models.TextField(db_column='suggestionLog', blank=True) # Field name made lowercase.
    discussion = models.TextField(blank=True)
    discussionlog = models.TextField(db_column='discussionLog', blank=True) # Field name made lowercase.
    clarifyissue = models.CharField(db_column='clarifyIssue', max_length=4, blank=True) # Field name made lowercase.
    clarifysuggestion = models.CharField(db_column='clarifySuggestion', max_length=4, blank=True) # Field name made lowercase.
    vendoraction = models.CharField(db_column='vendorAction', max_length=4, blank=True) # Field name made lowercase.
    vendorspecific = models.CharField(db_column='vendorSpecific', max_length=4, blank=True) # Field name made lowercase.
    fixitdecision = models.CharField(db_column='fixitDecision', max_length=4, blank=True) # Field name made lowercase.
    classification = models.CharField(max_length=60, blank=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated', blank=True, null=True) # Field name made lowercase.
    lastchanges = models.CharField(db_column='lastChanges', max_length=255, blank=True) # Field name made lowercase.
    ownershipfab = models.CharField(db_column='ownershipFab', max_length=4, blank=True) # Field name made lowercase.
    originalsuggestion = models.TextField(db_column='originalSuggestion', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FaxItem'

class Faxjob(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    targetpartnumber = models.CharField(db_column='targetPartNumber', max_length=20, blank=True) # Field name made lowercase.
    faxnumber = models.IntegerField(db_column='faxNumber', blank=True, null=True) # Field name made lowercase.
    vendor = models.CharField(max_length=40, blank=True)
    vendorcomment = models.CharField(db_column='vendorComment', max_length=80, blank=True) # Field name made lowercase.
    clockstart = models.DateTimeField(db_column='clockStart', blank=True, null=True) # Field name made lowercase.
    buildstatus = models.CharField(db_column='buildStatus', max_length=20, blank=True) # Field name made lowercase.
    datasource = models.CharField(db_column='dataSource', max_length=30, blank=True) # Field name made lowercase.
    otheremails = models.CharField(db_column='otherEMails', max_length=200, blank=True) # Field name made lowercase.
    simpleurltext = models.TextField(db_column='simpleURLText', blank=True) # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True) # Field name made lowercase.
    directorymode = models.IntegerField(db_column='directoryMode', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FaxJob'

class Filmcopy(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    filmaccount = models.CharField(db_column='filmAccount', max_length=20, blank=True) # Field name made lowercase.
    filmaccountcomment = models.CharField(db_column='filmAccountComment', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'FilmCopy'

class Fixittask(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    faxitem = models.CharField(db_column='faxItem', max_length=40, blank=True) # Field name made lowercase.
    taskdesignjob = models.CharField(db_column='taskDesignJob', max_length=40, blank=True) # Field name made lowercase.
    taskstatus = models.CharField(db_column='taskStatus', max_length=20, blank=True) # Field name made lowercase.
    tasklog = models.CharField(db_column='taskLog', max_length=255, blank=True) # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'FixitTask'

class Hpcopy(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'HPCopy'

class Highestoid(models.Model):
    highest = models.IntegerField(unique=True, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'HighestOID'

class Job(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    businessprocess = models.CharField(db_column='businessProcess', max_length=60, blank=True) # Field name made lowercase.
    mainstatus = models.CharField(db_column='mainStatus', max_length=1, blank=True) # Field name made lowercase.
    substatus = models.CharField(db_column='subStatus', max_length=40, blank=True) # Field name made lowercase.
    requestreceived = models.DateTimeField(db_column='requestReceived', blank=True, null=True) # Field name made lowercase.
    requestedcompletion = models.DateTimeField(db_column='requestedCompletion', blank=True, null=True) # Field name made lowercase.
    actualcompletion = models.DateTimeField(db_column='actualCompletion', blank=True, null=True) # Field name made lowercase.
    legacyjobid = models.IntegerField(db_column='legacyJobID', blank=True, null=True) # Field name made lowercase.
    manualholdflag = models.CharField(db_column='manualHoldFlag', max_length=3, blank=True) # Field name made lowercase.
    oldmanualholdcomment = models.CharField(db_column='oldManualHoldComment', max_length=80, blank=True) # Field name made lowercase.
    manualholdcomment = models.TextField(db_column='manualHoldComment', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Job'

class Layertextdata(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    layertext = models.CharField(db_column='layerText', max_length=80, blank=True) # Field name made lowercase.
    representation = models.CharField(max_length=8, blank=True)
    class Meta:
        managed = False
        db_table = 'LayerTextData'

class Maillog(models.Model):
    eventoid = models.CharField(db_column='eventOID', max_length=40, blank=True) # Field name made lowercase.
    maintargetoid = models.CharField(db_column='mainTargetOID', max_length=40, blank=True) # Field name made lowercase.
    logtime = models.DateTimeField(db_column='logTime', blank=True, null=True) # Field name made lowercase.
    subject = models.CharField(max_length=255, blank=True)
    recipients = models.CharField(max_length=255, blank=True)
    messagedata = models.TextField(db_column='messageData', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'MailLog'

class Oidlist(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'OidList'

class Optionalapproval(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    owningjob = models.CharField(db_column='owningJob', max_length=40, blank=True) # Field name made lowercase.
    areatag = models.CharField(db_column='areaTag', max_length=40, blank=True) # Field name made lowercase.
    title = models.CharField(max_length=40, blank=True)
    status = models.CharField(max_length=40, blank=True)
    emails = models.CharField(max_length=120, blank=True)
    comments = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'OptionalApproval'

class Personentity(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    companyid = models.CharField(db_column='companyID', max_length=40, blank=True) # Field name made lowercase.
    givenname = models.CharField(db_column='givenName', max_length=60, blank=True) # Field name made lowercase.
    familyname = models.CharField(db_column='familyName', max_length=60, blank=True) # Field name made lowercase.
    email = models.CharField(db_column='eMail', max_length=80, blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=60, blank=True)
    usagedescription = models.TextField(db_column='usageDescription', blank=True) # Field name made lowercase.
    loginstatus = models.CharField(db_column='loginStatus', max_length=10, blank=True) # Field name made lowercase.
    departmentcode = models.CharField(db_column='departmentCode', max_length=20, blank=True) # Field name made lowercase.
    location = models.CharField(max_length=60, blank=True)
    automaticupdate = models.CharField(db_column='automaticUpdate', max_length=3, blank=True) # Field name made lowercase.
    manager = models.CharField(max_length=80, blank=True)
    usagetag = models.CharField(db_column='usageTag', max_length=80, blank=True) # Field name made lowercase.
    manageremail = models.CharField(db_column='managerEMail', max_length=50, blank=True) # Field name made lowercase.
    oracleid = models.CharField(db_column='oracleID', max_length=60, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PersonEntity'

class Planedata(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True)
    weight = models.FloatField(blank=True, null=True)
    foiltype = models.CharField(db_column='foilType', max_length=14, blank=True) # Field name made lowercase.
    conductivity = models.FloatField(blank=True, null=True)
    metalthickness = models.FloatField(db_column='metalThickness', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PlaneData'

class Planelayer(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    layername = models.CharField(db_column='layerName', max_length=50, blank=True) # Field name made lowercase.
    weight = models.CharField(max_length=50, blank=True)
    tolerance = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'PlaneLayer'

class Prepregdata(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    ply = models.CharField(max_length=50, blank=True)
    dielectricthickness = models.FloatField(db_column='dielectricThickness', blank=True, null=True) # Field name made lowercase.
    materialtype = models.CharField(db_column='materialType', max_length=30, blank=True) # Field name made lowercase.
    materialcomment = models.CharField(db_column='materialComment', max_length=80, blank=True) # Field name made lowercase.
    thicknesscontrol = models.CharField(db_column='thicknessControl', max_length=40, blank=True) # Field name made lowercase.
    dk = models.FloatField(blank=True, null=True)
    fdk = models.FloatField(db_column='fDk', blank=True, null=True) # Field name made lowercase.
    df = models.FloatField(blank=True, null=True)
    fdf = models.FloatField(db_column='fDf', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'PrepregData'

class Project(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    name = models.CharField(max_length=50, blank=True)
    primarydesigngroup = models.CharField(db_column='primaryDesignGroup', max_length=40, blank=True) # Field name made lowercase.
    requestingworkgroupscomment = models.CharField(db_column='requestingWorkGroupsComment', max_length=80, blank=True) # Field name made lowercase.
    primarydesigngroupcomment = models.CharField(db_column='primaryDesignGroupComment', max_length=80, blank=True) # Field name made lowercase.
    updated = models.DateTimeField(blank=True, null=True)
    observeremails = models.CharField(db_column='observerEMails', max_length=240, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Project'

class Projectgroup(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    aproject = models.CharField(db_column='aProject', max_length=40, blank=True) # Field name made lowercase.
    aworkgroup = models.CharField(db_column='aWorkGroup', max_length=40, blank=True) # Field name made lowercase.
    relationship = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'ProjectGroup'

class Projectjobassociation(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    aproject = models.CharField(db_column='aProject', max_length=40, blank=True) # Field name made lowercase.
    ajob = models.CharField(db_column='aJob', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ProjectJobAssociation'

class Reviewcopy(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    xlevel = models.IntegerField(db_column='xLevel', blank=True, null=True) # Field name made lowercase.
    receivingvendorscomment = models.CharField(db_column='receivingVendorsComment', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ReviewCopy'

class Roleassignment(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    auserentity = models.CharField(db_column='aUserEntity', max_length=40, blank=True) # Field name made lowercase.
    arole = models.CharField(db_column='aRole', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'RoleAssignment'

class Signaldata(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True)
    signaltype = models.CharField(db_column='signalType', max_length=10, blank=True) # Field name made lowercase.
    weight = models.FloatField(blank=True, null=True)
    foiltype = models.CharField(db_column='foilType', max_length=14, blank=True) # Field name made lowercase.
    conductivity = models.FloatField(blank=True, null=True)
    metalthickness = models.FloatField(db_column='metalThickness', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SignalData'

class Signallayer(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    adesignjob = models.CharField(db_column='aDesignJob', max_length=40, blank=True) # Field name made lowercase.
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    layername = models.CharField(db_column='layerName', max_length=50, blank=True) # Field name made lowercase.
    surfaceflag = models.CharField(db_column='surfaceFlag', max_length=3, blank=True) # Field name made lowercase.
    width = models.CharField(max_length=50, blank=True)
    space = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    impedance = models.CharField(max_length=50, blank=True)
    tolerance = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'SignalLayer'

class Signalparam(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    layer = models.CharField(max_length=40, blank=True)
    sequencenumber = models.FloatField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    width = models.FloatField(blank=True, null=True)
    space = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    oldparamtype = models.CharField(db_column='oldParamType', max_length=7, blank=True) # Field name made lowercase.
    impedance = models.FloatField(blank=True, null=True)
    tolerance = models.FloatField(blank=True, null=True)
    paramtype = models.CharField(db_column='paramType', max_length=12, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SignalParam'

class Staticvalue(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    grouping = models.CharField(max_length=30, blank=True)
    oldtag = models.CharField(max_length=20, blank=True)
    valuetitle = models.CharField(db_column='valueTitle', max_length=80, blank=True) # Field name made lowercase.
    sequencenumber = models.IntegerField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    reviewlevel = models.CharField(db_column='reviewLevel', max_length=20, blank=True) # Field name made lowercase.
    reviewsubject = models.CharField(db_column='reviewSubject', max_length=80, blank=True) # Field name made lowercase.
    reviewcomments = models.TextField(db_column='reviewComments', blank=True) # Field name made lowercase.
    helptext = models.TextField(db_column='helpText', blank=True) # Field name made lowercase.
    usagestatus = models.CharField(db_column='usageStatus', max_length=40, blank=True) # Field name made lowercase.
    valuetag = models.CharField(db_column='valueTag', max_length=50, blank=True) # Field name made lowercase.
    email = models.CharField(max_length=80, blank=True)
    class Meta:
        managed = False
        db_table = 'StaticValue'

class Staticvaluerelationship(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    primaryinstance = models.CharField(db_column='primaryInstance', max_length=40, blank=True) # Field name made lowercase.
    dependentvalue = models.CharField(db_column='dependentValue', max_length=40, blank=True) # Field name made lowercase.
    relationshiptype = models.CharField(db_column='relationshipType', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'StaticValueRelationship'

class Statusdependency(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    parent = models.CharField(max_length=40, blank=True)
    child = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'StatusDependency'

class Stencilpackage(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    receivingvendorscomment = models.CharField(db_column='receivingVendorsComment', max_length=80, blank=True) # Field name made lowercase.
    typeofoutput = models.CharField(db_column='typeOfOutput', max_length=14, blank=True) # Field name made lowercase.
    typeofoutputcomment = models.CharField(db_column='typeOfOutputComment', max_length=80, blank=True) # Field name made lowercase.
    numberofcopies = models.IntegerField(db_column='numberOfCopies', blank=True, null=True) # Field name made lowercase.
    numberofcopiescomment = models.CharField(db_column='numberOfCopiesComment', max_length=80, blank=True) # Field name made lowercase.
    filmaccount = models.CharField(db_column='filmAccount', max_length=20, blank=True) # Field name made lowercase.
    filmaccountcomment = models.CharField(db_column='filmAccountComment', max_length=80, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'StencilPackage'

class Storage(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    majorformat = models.CharField(db_column='majorFormat', max_length=25, blank=True) # Field name made lowercase.
    storagetype = models.CharField(db_column='storageType', max_length=10, blank=True) # Field name made lowercase.
    storageurl = models.CharField(db_column='storageURL', max_length=160, blank=True) # Field name made lowercase.
    localpath = models.CharField(db_column='localPath', max_length=160, blank=True) # Field name made lowercase.
    content = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'Storage'

class Storedquery(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    enteringuser = models.CharField(db_column='enteringUser', max_length=40, blank=True) # Field name made lowercase.
    title = models.CharField(max_length=80, blank=True)
    usagemode = models.CharField(max_length=80, blank=True)
    querytext = models.TextField(db_column='queryText', blank=True) # Field name made lowercase.
    entered = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'StoredQuery'

class Userentityassignment(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    auserentity = models.CharField(db_column='aUserEntity', max_length=40, blank=True) # Field name made lowercase.
    assignedwork = models.CharField(db_column='assignedWork', max_length=40, blank=True) # Field name made lowercase.
    assignmentnature = models.CharField(db_column='assignmentNature', max_length=30, blank=True) # Field name made lowercase.
    assignmentdate = models.DateTimeField(db_column='assignmentDate', blank=True, null=True) # Field name made lowercase.
    assignedby = models.CharField(db_column='assignedBy', max_length=40, blank=True) # Field name made lowercase.
    assignmentcomment = models.TextField(db_column='assignmentComment', blank=True) # Field name made lowercase.
    involvement = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'UserEntityAssignment'

class Userentityrole(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    rolename = models.CharField(db_column='roleName', max_length=60, blank=True) # Field name made lowercase.
    roletag = models.CharField(db_column='roleTag', max_length=60, blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'UserEntityRole'

class Usermessage(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    messagetag = models.CharField(db_column='messageTag', max_length=60, blank=True) # Field name made lowercase.
    messagetitle = models.CharField(db_column='messageTitle', max_length=100, blank=True) # Field name made lowercase.
    targetcase = models.CharField(db_column='targetCase', max_length=200, blank=True) # Field name made lowercase.
    simpleusecases = models.TextField(db_column='simpleUseCases', blank=True) # Field name made lowercase.
    simpleblockcases = models.TextField(db_column='simpleBlockCases', blank=True) # Field name made lowercase.
    sequencenumber = models.IntegerField(db_column='sequenceNumber', blank=True, null=True) # Field name made lowercase.
    reviewlevel = models.CharField(db_column='reviewLevel', max_length=20, blank=True) # Field name made lowercase.
    messagetext = models.TextField(db_column='messageText', blank=True) # Field name made lowercase.
    usagestatus = models.CharField(db_column='usageStatus', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'UserMessage'

class Workgroup(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    name = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'WorkGroup'

class Workgroupassignment(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    ajob = models.CharField(db_column='aJob', max_length=40, blank=True) # Field name made lowercase.
    aworkgroup = models.CharField(db_column='aWorkGroup', max_length=40, blank=True) # Field name made lowercase.
    grouprole = models.CharField(db_column='groupRole', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'WorkGroupAssignment'

class Workgroupmembership(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    auserentity = models.CharField(db_column='aUserEntity', max_length=40, blank=True) # Field name made lowercase.
    aworkgroup = models.CharField(db_column='aWorkGroup', max_length=40, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'WorkGroupMembership'

class BetPartinfo(models.Model):
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
        managed = False
        db_table = 'bet_PartInfo'

class Butable(models.Model):
    job_id = models.IntegerField(blank=True, null=True)
    business_unit = models.CharField(max_length=40, blank=True)
    organization = models.CharField(max_length=60, blank=True)
    class Meta:
        managed = False
        db_table = 'buTable'

class HdBetparts(models.Model):
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
    hd_f1 = models.CharField(max_length=45, blank=True)
    hd_f2 = models.CharField(max_length=45, blank=True)
    hd_f3 = models.CharField(max_length=45, blank=True)
    hd_f4 = models.CharField(max_length=45, blank=True)
    hd_f5 = models.CharField(max_length=45, blank=True)
    hd_n1 = models.FloatField(blank=True, null=True)
    hd_n2 = models.FloatField(blank=True, null=True)
    hd_n3 = models.FloatField(blank=True, null=True)
    hd_n4 = models.FloatField(blank=True, null=True)
    hd_n5 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hd_BETParts'

class HdInter(models.Model):
    partnumber = models.CharField(db_column='partNumber', max_length=16, blank=True) # Field name made lowercase.
    partname = models.CharField(db_column='partName', max_length=50, blank=True) # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50, blank=True) # Field name made lowercase.
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dimensionsuom = models.CharField(db_column='dimensionsUOM', max_length=6, blank=True) # Field name made lowercase.
    hd_f1 = models.CharField(max_length=45, blank=True)
    hd_f2 = models.CharField(max_length=45, blank=True)
    hd_f3 = models.CharField(max_length=45, blank=True)
    hd_f4 = models.CharField(max_length=45, blank=True)
    hd_f5 = models.CharField(max_length=45, blank=True)
    hd_n1 = models.FloatField(blank=True, null=True)
    hd_n2 = models.FloatField(blank=True, null=True)
    hd_n3 = models.FloatField(blank=True, null=True)
    hd_n4 = models.FloatField(blank=True, null=True)
    hd_n5 = models.FloatField(blank=True, null=True)
    newwidth = models.CharField(max_length=63, blank=True)
    newheight = models.CharField(max_length=63, blank=True)
    class Meta:
        managed = False
        db_table = 'hd_inter'

class HdTest(models.Model):
    hd_partnumber = models.CharField(db_column='hd_PartNumber', unique=True, max_length=100) # Field name made lowercase.
    hd_f1 = models.CharField(max_length=45, blank=True)
    hd_f2 = models.CharField(max_length=45, blank=True)
    hd_f3 = models.CharField(max_length=45, blank=True)
    hd_f4 = models.CharField(max_length=45, blank=True)
    hd_f5 = models.CharField(max_length=45, blank=True)
    hd_n1 = models.FloatField(blank=True, null=True)
    hd_n2 = models.FloatField(blank=True, null=True)
    hd_n3 = models.FloatField(blank=True, null=True)
    hd_n4 = models.FloatField(blank=True, null=True)
    hd_n5 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hd_test'

class Test(models.Model):
    oid = models.CharField(max_length=40, blank=True)
    intvar = models.IntegerField(db_column='intVar', blank=True, null=True) # Field name made lowercase.
    stringvar = models.CharField(db_column='stringVar', max_length=40, blank=True) # Field name made lowercase.
    anenumvar = models.CharField(db_column='anEnumVar', max_length=5, blank=True) # Field name made lowercase.
    areference = models.CharField(db_column='aReference', max_length=40, blank=True) # Field name made lowercase.
    acalendar = models.DateTimeField(db_column='aCalendar', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'test'

