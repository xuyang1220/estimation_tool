# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Combine'
        db.create_table(u'BET_combine', (
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_column=u'Part_number')),
            ('part_name', self.gf('django.db.models.fields.CharField')(max_length=300, db_column=u'Part Name')),
            ('total_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Total Days', blank=True)),
            ('board_width', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Board Width', blank=True)),
            ('board_height', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Board Height', blank=True)),
            ('metal_to_metal_thickness', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Metal to Metal Thickness', blank=True)),
            ('sequential_lam', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_column=u'Sequential Lam')),
            ('via_type_buried', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_column=u'Via Type:Buried')),
            ('via_type_blind', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_column=u'Via Type:Blind')),
            ('total_layers', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Total Layers', blank=True)),
            ('plane_layers', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Plane Layers', blank=True)),
            ('pins', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pins', blank=True)),
            ('connections', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Connections', blank=True)),
            ('components', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Components', blank=True)),
            ('total_nets', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Total Nets', blank=True)),
            ('bga_lgas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'BGA/LGAs', blank=True)),
            ('dimms', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DIMMs', blank=True)),
            ('pin_density', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('component_density', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('buses', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Buses', blank=True)),
            ('constraintsets', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Constraintsets', blank=True)),
            ('diffpairs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Diffpairs', blank=True)),
            ('matchgroups', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Matchgroups', blank=True)),
            ('netclasses', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Netclasses', blank=True)),
            ('net_with_constraints', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Net with Constraints', blank=True)),
            ('pinpairs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pinpairs', blank=True)),
            ('xnets', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Xnets', blank=True)),
            ('estimated_total_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Estimated Total Days', blank=True)),
        ))
        db.send_create_signal(u'BET', ['Combine'])

        # Adding model 'PartInfo'
        db.create_table(u'bet_PartInfo', (
            ('board_width', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'width', blank=True)),
            ('board_height', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'height', blank=True)),
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_column=u'partNumber')),
        ))
        db.send_create_signal(u'BET', ['PartInfo'])

        # Adding model 'Physicalboard'
        db.create_table(u'BET_physicalboard', (
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_column=u'Part_number')),
            ('part_name', self.gf('django.db.models.fields.CharField')(max_length=300, db_column=u'Part Name', blank=True)),
            ('job_start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'Job Start Date', blank=True)),
            ('engineer_sign_off_date', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'Engineer Sign-off Date', blank=True)),
            ('sequential_lam', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Sequential Lam', blank=True)),
            ('board_width', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Board Width', blank=True)),
            ('board_height', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Board Height', blank=True)),
            ('via_type_buried', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Via Type:Buried', blank=True)),
            ('via_type_blind', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Via Type:Blind', blank=True)),
            ('total_layers', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Total Layers', blank=True)),
            ('metal_to_metal_thickness', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Metal to Metal Thickness', blank=True)),
            ('plane_layers', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Plane Layers', blank=True)),
            ('whizz_time_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Whizz_time_days', blank=True)),
            ('overtime_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Overtime / days', blank=True)),
            ('qty_designers', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Qty designers', blank=True)),
            ('prime_designer_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Prime designer / days', blank=True)),
            ('second_designer_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Second designer / days', blank=True)),
            ('total_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Total days', blank=True)),
            ('estimated_total_days', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Estimated Total Days', blank=True)),
        ))
        db.send_create_signal(u'BET', ['Physicalboard'])

        # Adding model 'Schematic'
        db.create_table(u'BET_schematic', (
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_column=u'Part_number')),
            ('pins', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pins', blank=True)),
            ('connections', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Connections', blank=True)),
            ('components', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Components', blank=True)),
            ('nets', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nets', blank=True)),
            ('layoutarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Layoutarea', blank=True)),
            ('bga_lgas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'BGA/LGAs', blank=True)),
            ('dimms', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DIMMs', blank=True)),
            ('members', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Members', blank=True)),
            ('buses', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Buses', blank=True)),
            ('constraintsets', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Constraintsets', blank=True)),
            ('diffpairs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Diffpairs', blank=True)),
            ('matchgroups', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Matchgroups', blank=True)),
            ('netclasses', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Netclasses', blank=True)),
            ('netc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NetC', blank=True)),
            ('pinpairs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pinpairs', blank=True)),
            ('xnets', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Xnets', blank=True)),
            ('keepinx', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Keepinx', blank=True)),
            ('keepiny', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Keepiny', blank=True)),
        ))
        db.send_create_signal(u'BET', ['Schematic'])

        # Adding model 'Brdmapdat'
        db.create_table(u'BET_brdmapdat', (
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True, db_column=u'Part_number')),
            ('dat_file_location', self.gf('django.db.models.fields.CharField')(max_length=500, db_column=u'Dat_file_location', blank=True)),
            ('brd_file_location', self.gf('django.db.models.fields.CharField')(max_length=500, db_column=u'Brd_file_location', blank=True)),
        ))
        db.send_create_signal(u'BET', ['Brdmapdat'])


    def backwards(self, orm):
        # Deleting model 'Combine'
        db.delete_table(u'BET_combine')

        # Deleting model 'PartInfo'
        db.delete_table(u'bet_PartInfo')

        # Deleting model 'Physicalboard'
        db.delete_table(u'BET_physicalboard')

        # Deleting model 'Schematic'
        db.delete_table(u'BET_schematic')

        # Deleting model 'Brdmapdat'
        db.delete_table(u'BET_brdmapdat')


    models = {
        u'BET.authgroup': {
            'Meta': {'object_name': 'AuthGroup', 'db_table': "u'auth_group'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'BET.authgrouppermissions': {
            'Meta': {'object_name': 'AuthGroupPermissions', 'db_table': "u'auth_group_permissions'", 'managed': 'False'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.AuthPermission']"})
        },
        u'BET.authpermission': {
            'Meta': {'object_name': 'AuthPermission', 'db_table': "u'auth_permission'", 'managed': 'False'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.DjangoContentType']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'BET.authuser': {
            'Meta': {'object_name': 'AuthUser', 'db_table': "u'auth_user'", 'managed': 'False'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {}),
            'is_staff': ('django.db.models.fields.IntegerField', [], {}),
            'is_superuser': ('django.db.models.fields.IntegerField', [], {}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'BET.authusergroups': {
            'Meta': {'object_name': 'AuthUserGroups', 'db_table': "u'auth_user_groups'", 'managed': 'False'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.AuthUser']"})
        },
        u'BET.authuseruserpermissions': {
            'Meta': {'object_name': 'AuthUserUserPermissions', 'db_table': "u'auth_user_user_permissions'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.AuthPermission']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.AuthUser']"})
        },
        u'BET.betitem': {
            'Meta': {'object_name': 'BetItem', 'db_table': "u'bet_item'", 'managed': 'False'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {}),
            'done': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        u'BET.brdmapdat': {
            'Meta': {'object_name': 'Brdmapdat'},
            'brd_file_location': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "u'Brd_file_location'", 'blank': 'True'}),
            'dat_file_location': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "u'Dat_file_location'", 'blank': 'True'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True', 'db_column': "u'Part_number'"})
        },
        u'BET.combine': {
            'Meta': {'object_name': 'Combine'},
            'bga_lgas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'BGA/LGAs'", 'blank': 'True'}),
            'board_height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Board Height'", 'blank': 'True'}),
            'board_width': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Board Width'", 'blank': 'True'}),
            'buses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Buses'", 'blank': 'True'}),
            'component_density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'components': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Components'", 'blank': 'True'}),
            'connections': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Connections'", 'blank': 'True'}),
            'constraintsets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Constraintsets'", 'blank': 'True'}),
            'diffpairs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Diffpairs'", 'blank': 'True'}),
            'dimms': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DIMMs'", 'blank': 'True'}),
            'estimated_total_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Estimated Total Days'", 'blank': 'True'}),
            'matchgroups': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Matchgroups'", 'blank': 'True'}),
            'metal_to_metal_thickness': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Metal to Metal Thickness'", 'blank': 'True'}),
            'net_with_constraints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Net with Constraints'", 'blank': 'True'}),
            'netclasses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Netclasses'", 'blank': 'True'}),
            'part_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "u'Part Name'"}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_column': "u'Part_number'"}),
            'pin_density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pinpairs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pinpairs'", 'blank': 'True'}),
            'pins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pins'", 'blank': 'True'}),
            'plane_layers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Plane Layers'", 'blank': 'True'}),
            'sequential_lam': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'Sequential Lam'"}),
            'total_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Total Days'", 'blank': 'True'}),
            'total_layers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Total Layers'", 'blank': 'True'}),
            'total_nets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Total Nets'", 'blank': 'True'}),
            'via_type_blind': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'Via Type:Blind'"}),
            'via_type_buried': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'Via Type:Buried'"}),
            'xnets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Xnets'", 'blank': 'True'})
        },
        u'BET.djangoadminlog': {
            'Meta': {'object_name': 'DjangoAdminLog', 'db_table': "u'django_admin_log'", 'managed': 'False'},
            'action_flag': ('django.db.models.fields.IntegerField', [], {}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {}),
            'change_message': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.DjangoContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_repr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['BET.AuthUser']"})
        },
        u'BET.djangocontenttype': {
            'Meta': {'object_name': 'DjangoContentType', 'db_table': "u'django_content_type'", 'managed': 'False'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'BET.djangosession': {
            'Meta': {'object_name': 'DjangoSession', 'db_table': "u'django_session'", 'managed': 'False'},
            'expire_date': ('django.db.models.fields.DateTimeField', [], {}),
            'session_data': ('django.db.models.fields.TextField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        },
        u'BET.partinfo': {
            'Meta': {'object_name': 'PartInfo', 'db_table': "u'bet_PartInfo'"},
            'board_height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'height'", 'blank': 'True'}),
            'board_width': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'width'", 'blank': 'True'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_column': "u'partNumber'"})
        },
        u'BET.physicalboard': {
            'Meta': {'object_name': 'Physicalboard'},
            'board_height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Board Height'", 'blank': 'True'}),
            'board_width': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Board Width'", 'blank': 'True'}),
            'engineer_sign_off_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'Engineer Sign-off Date'", 'blank': 'True'}),
            'estimated_total_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Estimated Total Days'", 'blank': 'True'}),
            'job_start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'Job Start Date'", 'blank': 'True'}),
            'metal_to_metal_thickness': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Metal to Metal Thickness'", 'blank': 'True'}),
            'overtime_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Overtime / days'", 'blank': 'True'}),
            'part_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "u'Part Name'", 'blank': 'True'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_column': "u'Part_number'"}),
            'plane_layers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Plane Layers'", 'blank': 'True'}),
            'prime_designer_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Prime designer / days'", 'blank': 'True'}),
            'qty_designers': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Qty designers'", 'blank': 'True'}),
            'second_designer_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Second designer / days'", 'blank': 'True'}),
            'sequential_lam': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Sequential Lam'", 'blank': 'True'}),
            'total_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Total days'", 'blank': 'True'}),
            'total_layers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Total Layers'", 'blank': 'True'}),
            'via_type_blind': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Via Type:Blind'", 'blank': 'True'}),
            'via_type_buried': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Via Type:Buried'", 'blank': 'True'}),
            'whizz_time_days': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Whizz_time_days'", 'blank': 'True'})
        },
        u'BET.schematic': {
            'Meta': {'object_name': 'Schematic'},
            'bga_lgas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'BGA/LGAs'", 'blank': 'True'}),
            'buses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Buses'", 'blank': 'True'}),
            'components': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Components'", 'blank': 'True'}),
            'connections': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Connections'", 'blank': 'True'}),
            'constraintsets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Constraintsets'", 'blank': 'True'}),
            'diffpairs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Diffpairs'", 'blank': 'True'}),
            'dimms': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DIMMs'", 'blank': 'True'}),
            'keepinx': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Keepinx'", 'blank': 'True'}),
            'keepiny': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Keepiny'", 'blank': 'True'}),
            'layoutarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Layoutarea'", 'blank': 'True'}),
            'matchgroups': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Matchgroups'", 'blank': 'True'}),
            'members': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Members'", 'blank': 'True'}),
            'netc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NetC'", 'blank': 'True'}),
            'netclasses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Netclasses'", 'blank': 'True'}),
            'nets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nets'", 'blank': 'True'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_column': "u'Part_number'"}),
            'pinpairs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pinpairs'", 'blank': 'True'}),
            'pins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pins'", 'blank': 'True'}),
            'xnets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Xnets'", 'blank': 'True'})
        }
    }

    complete_apps = ['BET']