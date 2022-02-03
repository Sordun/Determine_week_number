from datetime import date, timedelta

from django.shortcuts import redirect, render

from .forms import DateForm


def week_number(request):
    """Вычисление номера недели переданной даты"""
    start_date = date(2019, 1, 1)

    if request.method == "POST":
        form = DateForm(request.POST)

        if form.is_valid():
            calculated_date = form.cleaned_data["input_date"]

            reference_point = start_date - timedelta(days=2)  # дата отчёта
            quantity_days = (
                calculated_date - reference_point
            ).days  # количество прошедших дней с даты отчёта
            week_num = quantity_days // 7 + 1  # номер недели

            request.session["answer_weeks"] = week_num
            return redirect("answer_weeks")
    else:
        form = DateForm()

    return render(request, "weeks/week_number.html", context={"form": form})


def answer_weeks(request):
    """Отвечает какая неделя"""
    weeks = request.session.get("answer_weeks")
    return render(request, "weeks/weeks.html", context={"answer_weeks": weeks})
