from django.shortcuts import render,get_object_or_404,redirect
from .models import Question

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'Polls_app/question_list.html', {
        'questions': questions
    })

# def question_detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'Polls_app/question_detail.html', {'question': question})
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        # Get selected choice ID from the form
        choice_id = request.POST.get('choice')
        if choice_id:
            selected_choice = question.choices.get(id=choice_id)
            selected_choice.votes += 1
            selected_choice.save()
            # Redirect to results page after voting
            return redirect('question_results', question_id=question.id)
        else:
            # If no choice selected, reload page with error
            return render(request, 'Polls_app/question_detail.html', {
                'question': question,
                'error_message': 'Please select a choice!'
            })

    # GET request → just show page
    return render(request, 'Polls_app/question_detail.html', {'question': question})

def question_results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'Polls_app/question_results.html', {'question': question})
    
    # # Calculate total votes for the question
    # total_votes = sum(choice.votes for choice in choices)
    
    # # Add a 'percentage' attribute to each choice
    # for choice in choices:
    #     if total_votes > 0:
    #         choice.percentage = (choice.votes / total_votes) * 100
    #     else:
    #         choice.percentage = 0  # Avoid division by zero
    
    # return render(request, 'Polls_app/question_results.html', {'question': question, 'choices': choices})



