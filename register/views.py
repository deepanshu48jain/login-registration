from django.shortcuts import render, get_object_or_404, redirect
from .models import UserDetails
from .forms import UserForm


def sign_up(request):
	if request.method == "POST":
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect('detail', pk=user.pk)
	else:
	    form = UserForm()
	return render(request, 'register/sign_up.html', {'form': form})


def detail(request, pk):
	user = get_object_or_404(UserDetails, pk=pk)
	return render(request, 'register/detail.html', {'user': user})
