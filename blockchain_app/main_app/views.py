from django.shortcuts import render, get_object_or_404, redirect
from .models import LessonModel, StepModel
# Create your views here.

def mainpage_view(request):
    return redirect('/lessons/')

def lessons_list_view(request):
    lessons = LessonModel.objects.all()
    return render(request, 'lessonslist.html', {'lessons':lessons})

def step_detail_view(request, lesson_slug, step_slug):
    lesson = get_object_or_404(LessonModel, slug=lesson_slug)
    step = get_object_or_404(StepModel, lesson=lesson, slug = step_slug)
    steps_list = StepModel.objects.filter(lesson=lesson)
    steps_order = {}
    for i in steps_list:
        steps_order[i.index] = i.slug
    has_previous = has_next = True
    if step.index == 1:
        has_previous = pr_step = False
        next_step = steps_order.get(2, '')
    elif step.index == max([i for i in steps_order.keys()]):
        has_next = next_step = False
        pr_step = steps_order.get(step.index-1, '')
    else:
        pr_step = steps_order.get(step.index-1, '')
        next_step = steps_order.get(step.index+1, '')
        
    return render(request, 'step.html', {'lesson':lesson, 'step':step, 'has_previous':has_previous, 'has_next':has_next, 'pr_step':pr_step, 'next_step':next_step })