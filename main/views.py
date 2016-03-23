from django.shortcuts import render, render_to_response 
from django.template import RequestContext
#from django.http import HttpResponse
from main.models import State, City
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

#forms
from main.forms import CitySearchFrom, CreateCityForm, CityEditForm

# Create your views here.
@login_required
def city_delete(request, pk):

	City.objects.get(pk=pk).delete()

	return redirect('/city_search/')

@login_required
def city_edit(request, pk):

	print 'REQUEST TYPE -- %s' % request.method

	request_context = RequestContext(request)
	context = {}

	form = CityEditForm(request.POST or None)

	city = City.objects.get(pk=pk)

	form = CityEditForm(request.POST or None, instance=city)

	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/city_search/')

	return render_to_response('city_edit.html', context, context_instance=request_context)





def city_create(request):
	request_context = RequestContext(request)
	context = {}

	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()

			return render_to_response('city_create.html', context, context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response('city_create.html', context, context_instance=request_context)
	else:
		form = CreateCityForm()
		context['form'] = form		
		return render_to_response('city_create.html', context, context_instance=request_context)




def city_search(request):
	request_context = RequestContext(request)

	context = {}

	if request.method == 'POST':
		form = CitySearchFrom(request.POST)
		context['form'] = form

		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state = form.cleaned_data['state']
# , means and [this is to allow us to search for the name of the city and state]
			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

			return render_to_response('city_search.html', context, context_instance=request_context)

		else:
			context['valid'] = forms.errors

	else:
		form = CitySearchFrom()
		context['form'] = form
		return render_to_response('city_search.html', context, context_instance=request_context)


def state_list(request):
	context = {}
	states = State.objects.all()
	context['states'] = states
	return render(request, 'state_list.html', context)


class StateListView(ListView):
	model = State
	template_name = 'state_list.html'
	context_objects_name = 'states'

def state_detail(request, pk):
	context = {}
	state = State.objects.get(pk=pk)
	context['state'] = state
	return render(request, 'state_detail.html', context)

class StateDetailView(DetailView):
	model = State
	template_name = "state_detail.html"
	context_objects_name = "state"

	# state_list = []

	# for state in states:
	# 	try:
	# 		state_list.append("<a href= '/state_detail/%s'> %s -- %s</a><br>" % ( state.name, state.name, state.StateCapital.name))
	# 	except Exception, e:
	# 		print e

	# return HttpResponse(state_list)

# def template_view(request):

# 	context = {}

# 	states = State.objects.all()

# 	context['states'] = states

# 	return render(request,'state_list.html', context)


c
# @csrf_exempt
# def get_search(request):

# 	print request.method

# 	if request.method == 'GET':

# 		text_string = ''

# 		text_string += """
# 		<form action="/get_search/" method="POST">

# 		Search Cities:
# 		<input type='text' name='city_name'>
# 		<br>

# 		<input type='submit' value="Submit">

# 		</form>

# 		"""
# 		return HttpResponse(text_string)

# 	if request.method == 'POST':

# 		city_name = request.POST.get('city_name', None)

# 		print 'GET: %s' % request.GET
# 		print 'POST: %s' % request.POST

# 		text_string = ''
# 		text_string += 'Search Term: %s <br>' % city_name

# 		text_string += """
# 		<form action="/get_search/" method="POST">

# 		Search Cities:
# 		<input type='text' name='city_name'>
# 		<br>

# 		<input type='submit' value="Submit">

# 		</form>

# 		"""



# 	if city_name != None:
# 		cities = City.objects.filter(name__icontains=city_name)
# 		for city in cities:
# 			text_string += '%s <br>' % city.name
# 	return HttpResponse(text_string)


# class GetPost(View):
	
# 	def get(self, request, *args, **kwargs):
# 		text_string = ''

# 		text_string += """
# 		<form action="/GetPost/" method="POST">

# 		Search Cities:
# 		<input type='text' name='city_name'>
# 		<br>

# 		<input type='submit' value="Submit">

# 		</form>

# 		"""
# 		return HttpResponse(text_string)


# 	def post(self, request, *args, **kwargs):
# 		city_name = request.POST.get('city_name', None)

# 		print 'GET: %s' % request.GET
# 		print 'POST: %s' % request.POST

# 		text_string = ''
# 		text_string += 'Search Term: %s <br>' % city_name

# 		text_string += """
# 		<form action="/GetPost/" method="POST">

# 		Search Cities:
# 		<input type='text' name='city_name'>
# 		<br>

# 		<input type='submit' value="Submit">

# 		</form>
# 		"""
# 		return HttpResponse(text_string)




# @csrf_exempt
# def get_post(View):

# 	city_name = request.GET.get('q', None)

# 	post_var = request.POST.get('q', None)

# 	print request.GET
# 	print request.POST

# 	text_string = ''

# 	text_string += 'Get Var: %s <br>' % city_name

# 	text_string += 'Post Var: %s <br>' % post_var

# 	text_string += """
# 	<form action="/get_post/" method="POST">

# 	Enter Var:
# 	<input type='text' name='q'>
# 	<br>

# 	<input type='submit' value="Submit">
# 	</form>
# 	"""
# 	return HttpResponse(text_string)