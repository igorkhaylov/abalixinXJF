from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import FirstBlock, Management, Departament, Professors, Students, Practice, Science, Conference, Gallery, \
    Answers, Questions
import requests
# Create your views here.


def send_message(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        print(name, email, phone)
        print("this method is POST")
        link = request.path.split('/')[1]
        print(link)
        mes = "Имя: <b> " + name + \
              "\n</b>E-mail: <b> " + email + \
              "\n</b>Номер: <b> " + phone + "</b>"
              # "</b>\n\nСообщение: \n" + text
        url = f"https://api.telegram.org/bot1954029166:AAFTnvaHu5zaVd19_qY45WueeO9ch5SGEBE/sendMessage?chat_id=432499122&parse_mode=HTML&text={str(mes)}"
        response = requests.get(url)
        response.json()
        print(mes)


    return HttpResponseRedirect('/' + link)


def main(request):
    firstblock = FirstBlock.objects.first()
    management = Management.objects.all()
    departament = Departament.objects.all()
    professors = Professors.objects.all()
    students = Students.objects.all()
    practice = Practice.objects.first()
    science = Science.objects.first()
    conference = Conference.objects.first()
    gallery = Gallery.objects.first()
    answers = Answers.objects.all()
    questions = Questions.objects.all()
    return render(request, "index.html", {"firstblock": firstblock,
                                          "management": management,
                                          "departament": departament,
                                          "professors": professors,
                                          "students": students,
                                          "practice": practice,
                                          "science": science,
                                          "conference": conference,
                                          "gallery": gallery,
                                          "answers": answers,
                                          "questions": questions,
                                          })
