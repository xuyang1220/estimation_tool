from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from models import *
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
import datetime
#from haystack.views import SearchView
from forms import RangeForm, NewTaskForm, SingleSearchForm
from django.template import RequestContext
#from regression import est_time, model
from forms import *
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def hello(request):
    return HttpResponse("Hello world")

def search(request):
    return render_to_response('search/search.html',{'Combine':Combine}, context_instance=RequestContext(request))

def AdvancedSearch(request):
    form=AdvancedSearchForm()
    if request.method == 'POST':
        print "-----------POST----------------"
        form=AdvancedSearchForm(request.POST)
        #request.session['_old_post'] = request.POST
        if form.is_valid():
            print '---is valid----'
            queryset = form.search()
            return render_to_response('search/advancedsearch.html', {'form': form, 'queryset':queryset}, context_instance=RequestContext(request))
        else:
            return render_to_response('search/advancedsearch.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RangeForm()
        return render_to_response('search/advancedsearch.html', {'form': form}, context_instance=RequestContext(request))

def show_detail(request, part_number=''):
    combine = Combine.objects.get(part_number=part_number)
    #estimation = est_time(part_number)
    pins2 = combine.pins
    components2 = combine.components
    pin_density2 = combine.pin_density
    global pin_upper,pin_lower,component_upper,component_lower,pin_density_upper,pin_density_lower
    pin_lower=-100000
    pin_upper=100000
    component_lower=-1000000
    component_upper=1000000
    pin_density_lower=-1000000
    pin_density_upper=1000000
    if request.method == 'POST':
        print "-----------POST----------------"
        form = RangeForm(request.POST)
        #request.session['_old_post'] = request.POST
        if form.is_valid():
            print "-----------valid----------------"
            pin_diff = form.cleaned_data['pin_diff']
            component_diff = form.cleaned_data['component_diff']
            pin_density_diff = form.cleaned_data['pin_density_diff']
            adjusted_time = form.cleaned_data['adjusteddays']
            actual_time = form.cleaned_data['actualdays']
            # pin_lower=100
            # pin_upper=150
            if 'search1' in request.POST:
                if type(pin_diff) is int:
                    print "---------------------------"
                    pin_upper = pins2+pin_diff
                    pin_lower = pins2-pin_diff
                if type(component_diff) is int:
                    print "---------------------------"
                    component_upper = components2 + component_diff
                    component_lower = components2 - component_diff
                if type(pin_density_diff) is float:
                    print "---------------------------"
                    pin_density_upper = pin_density2 + pin_density_diff
                    pin_density_lower = pin_density2 - pin_density_diff
                #return render_to_response('search/show_similar.html',{ 'Combine': combine,'Combines': combines, 'part_number': part_number}, context_instance=RequestContext(request))
                return HttpResponseRedirect('/showdetail/%s/showsimilar/' % part_number)
            elif 'up1' in request.POST:
                combine.adjusted_total_days=adjusted_time
                combine.save()
                return HttpResponseRedirect('/showdetail/%s/' % part_number)
            elif 'up2' in request.POST:
                combine.total_days=actual_time
                combine.save()
                return HttpResponseRedirect('/showdetail/%s/' % part_number)
        else:
            return render_to_response('search/criteria_error.html', {'form': form, "Combine": combine}, context_instance=RequestContext(request))
    else:
        form = RangeForm()
        return render_to_response('search/show_detail.html', {'form': form, "Combine": combine}, context_instance=RequestContext(request))

def show_similar(request, part_number=''):
    combine=Combine.objects.get(part_number=part_number)
    combines = Combine.objects.filter(pins__gte=pin_lower, pins__lte=pin_upper)
    combines = combines.filter(components__gte=component_lower, components__lte=component_upper)
    combines = combines.filter(pin_density__gte=pin_density_lower, pin_density__lte=pin_density_upper)
    combines = combines.exclude(part_number=part_number)
    return render_to_response('search/show_similar.html',{'Combine': combine,'Combines': combines, 'part_number': part_number}, context_instance=RequestContext(request))
        #return HttpResponse('/thanks/')

def show_est_formula(request, part_num=''):
    formula = 'clopen set'
    #formula = model([1,1,1,1,1],1,1,1,1,1,1,1,1,1,1,1,1)
    return render(request, 'search/show_estimation_formula.html',{'formula' : formula})

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('search/login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/search/')
            else:
                return render_to_response('search/login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('search/login.html', RequestContext(request, {'form': form,}))

def index(request):
    form = NewTaskForm()
    if request.method == 'POST':
        print "------------POST IT!!!!!!!!!!!!!------"
        form = NewTaskForm(request.POST)
        if form.is_valid():
            (err, newtask) = form.get_statistics()
            partnumber = form.cleaned_data['part_number2']
            if err == 'Success!':
                newtask.save()
                return HttpResponseRedirect( "/showdetail/%s" % partnumber)
            # elif err == 'Warning! overwriting existing data in databases! Part number %s already exists in our database, not updated!' %(partnumber):
            #     return HttpResponseRedirect( "/showdetail/%s" % partnumber)
            else:
                return render_to_response('search/index.html', {'form': form, 'errormessage':err}, RequestContext(request))
        else:
            print "------------Not Valid!!!!!---------------"
            err='Please specify correct input for estimation'
            return render_to_response('search/index.html', {'form': form, 'errormessage':err}, RequestContext(request))
    else:
        return render_to_response('search/index.html', {'form': form}, RequestContext(request))

def index2(request):
    form = NewTaskForm()
    form2 = SingleSearchForm()
    if request.method == 'POST':
        print "---------------POST IT!!!!!!!!!!!!!--------------"
        form2 = SingleSearchForm(request.POST)
        if form2.is_valid():
            print "---------------Is valid--------------"
            partnumber = form2.cleaned_data['part_number']
            try:
                combine = Combine.objects.get(part_number=partnumber)
                return HttpResponseRedirect( "/showdetail/%s" % partnumber)
            except ObjectDoesNotExist:
                return HttpResponse('No result found')
        else:
            print "-------------------Not Valid!!!!!------------------------------"
            return render_to_response('search/search.html', RequestContext(request, {'form': form2}))
    else:
        return render_to_response('search/search.html', RequestContext(request, {'form': form2}))


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
