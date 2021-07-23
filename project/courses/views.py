from django.shortcuts import render, redirect

from courses.forms import CourseCreationForm


def create_course(request, id):
    form = CourseCreationForm()
    if request.method == 'POST':
        form = CourseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.mentor_id = id
            f.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'course/create_course.html', context)
