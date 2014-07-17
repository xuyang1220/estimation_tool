__author__ = 'yaxxu'
from django import forms
# from haystack.forms import SearchForm
# from haystack.query import *
from models import *
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from django.core.exceptions import ObjectDoesNotExist
import subprocess
import MySQLdb
from extract_statistics import *
from django.db import connections
#
# class SearchForm(forms.Form):
#     def no_query_found(self):
#         return EmptySearchQuerySet()

class AdvancedSearchForm(forms.Form):
    pin_lower_bound = forms.IntegerField(required=False, label='Pins Lower Bound')
    pin_upper_bound = forms.IntegerField(required=False, label='Pins Upper Bound')
    component_lower_bound = forms.IntegerField(required=False, label='Components Lower Bound')
    component_upper_bound = forms.IntegerField(required=False, label='Components Upper Bound')
    pin_density_lower = forms.IntegerField(required=False, label='Pin Density Lower Bound')
    pin_density_upper = forms.IntegerField(required=False, label='Pin Density Upper Bound')
    board_size_lower = forms.IntegerField(required=False, label='Board Size Lower Bound')
    board_size_upper = forms.IntegerField(required=False, label='Board Size Upper Bound')
    def search(self):
        # # First, store the SearchQuerySet received from other processing.
        sqs = Combine.objects.all()

        if not self.is_valid():
            return sqs

        sqs = sqs.order_by('pins')

        if self.cleaned_data['pin_lower_bound']:
            sqs = sqs.filter(pins__gte=self.cleaned_data['pin_lower_bound'])

        if self.cleaned_data['pin_upper_bound']:
            sqs = sqs.filter(pins__lte=self.cleaned_data['pin_upper_bound'])

        if self.cleaned_data['component_lower_bound']:
            sqs = sqs.filter(components__gte=self.cleaned_data['component_lower_bound'])

        if self.cleaned_data['component_upper_bound']:
            sqs = sqs.filter(components__lte=self.cleaned_data['component_upper_bound'])

        if self.cleaned_data['pin_density_lower']:
            sqs = sqs.filter(pin_density__gte=self.cleaned_data['pin_density_lower'])

        if self.cleaned_data['pin_density_upper']:
            sqs = sqs.filter(pin_density__lte=self.cleaned_data['pin_density_upper'])

        if self.cleaned_data['board_size_lower']:
            sqs = sqs.filter(board_width__gte=self.cleaned_data['board_size_lower'])

        if self.cleaned_data['board_size_upper']:
            sqs = sqs.filter(board_width__lte=self.cleaned_data['board_size_upper'])

        return sqs


# class SearchByPartNumber(SearchForm):
#     def search(self):
#         # # First, store the SearchQuerySet received from other processing.
#         sqs = super(SearchByPartNumber, self).search()
#
#         if not self.is_valid():
#             return sqs
#
#         return sqs

# class FacetedSearchView(SearchView):
#     def extra_context(self):
#         extra = super(FacetedSearchView, self).extra_context()
#
#         if self.results == []:
#             extra['facets'] = self.form.search().facet_counts()
#         else:
#             extra['facets'] = self.results.facet_counts()
#
#         return extra

class RangeForm(forms.Form):
    pin_diff = forms.IntegerField(required=False)
    component_diff = forms.IntegerField(required=False)
    pin_density_diff = forms.FloatField(required=False)
    adjusteddays = forms.FloatField(required=False)
    actualdays = forms.FloatField(required=False)

class NewTaskForm(forms.Form):
    category = forms.CharField(required=False, label=u"Category")
    part_number2 = forms.CharField(required=True, label=u"Part Number",widget=forms.TextInput(attrs={'size': '20'}))
    dat_file_location = forms.CharField(required=True, label=u"Dat Files",widget=forms.TextInput(attrs={'size': '150'}))
    def get_statistics(self):
        partnumber = self.cleaned_data['part_number2']
        directory =self.cleaned_data['dat_file_location']
        print directory
        try:
            #connect to JTS get the information
            query = PartInfo.objects.using('JTS').get(part_number=partnumber)
            # create the board file and the reports. Skill programming script called
            # subprocess.call(['O:\usr2\engcheck\Estimation_tool\scripts\bet.bat', directory, str(query.board_height), str(query.board_width)], shell=True)
        except:
            err="Cannot find records for %s in JTS or the directory given is invalid" %(partnumber)
            return err
        # extract information from reports.
        try:
            check = Combine.objects.get(part_number=partnumber)
            err = 'Warning! overwriting existing data in databases! Part number %s already exists in our database' %(partnumber)
        except:
            err = 'Success!'
        finally:
            newtask = getstatistics(directory)
            newtask = getbigcomponents(directory,newtask)
            newtask = getconstraints(directory,newtask)
            newtask.part_name = query.part_name
            newtask.project_name = query.projectname
            newtask.board_width = query.width
            newtask.board_height = query.height
            print newtask.pins, newtask.constraintsets
            # except:
            #     err='Part Number not Found in JTS or No Such Directory'
            #     return err
            #add this new board to our data base
            #newtask.save(using='BET_NEW')
            return (err,newtask)


class SingleSearchForm(forms.Form):
    part_number = forms.CharField(required=True, label=u"Part Number",widget=forms.TextInput(attrs={'size': '30'}))

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"Username",
        error_messages={'required': 'Please input username'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"Username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"Password",
        error_messages={'required': u'Please input password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"password",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"Username and password required")
        else:
            cleaned_data = super(LoginForm, self).clean()




