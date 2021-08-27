from django.db import models

# Create your models here.


# Первый блок
class FirstBlock(models.Model):
    text = models.CharField("First Block", default="First Block", max_length=20, blank=True)
    text_facultet1 = models.CharField("Text facultet 1", max_length=120, blank=False)
    description_facultet1 = models.TextField("Description facultet 1", blank=False)
    picture_facultet1 = models.ImageField("Picture facultet 1", upload_to='media/first_block/', blank=False)
    text_facultet2 = models.CharField("Text facultet 2", max_length=120, blank=False)
    description_facultet2 = models.TextField("Description facultet 2", blank=False)
    picture_facultet2 = models.ImageField("Picture facultet 2", upload_to='media/first_block/', blank=False)
    # valid_for = models.CharField("Valid for", max_length=120, blank=False)
    years = models.SmallIntegerField("Valid for Years", default=20, blank=False)
    text_facultet3 = models.CharField("Text facultet 3", max_length=120, blank=False)
    description_facultet3 = models.TextField("Description facultet 3", blank=False)
    picture_facultet3 = models.ImageField("Picture facultet 3", upload_to='media/first_block/', blank=False)

    class Meta:
        verbose_name = "Первый блок"
        verbose_name_plural = "Первый блок"


# Награды
class AwardsManagement(models.Model):
    title = models.CharField("Name of", max_length=120, blank=True)
    management = models.ForeignKey("Management", on_delete=models.CASCADE, related_name="awards")

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


class AwardsProfessors(models.Model):
    title = models.CharField("Name of", max_length=120, blank=True)
    professors = models.ForeignKey("Professors", on_delete=models.CASCADE, related_name="awards")

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


class AwardsStudents(models.Model):
    title = models.CharField("Name of", max_length=120, blank=True)
    students = models.ForeignKey("Students", on_delete=models.CASCADE, related_name="awards")

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


# Руководство
class Management(models.Model):
    picture = models.ImageField("Фотография", upload_to='media/management/')
    name = models.CharField("ФИО: ", max_length=120)

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"


# Кафедры
class Departament(models.Model):
    title = models.CharField("Title", max_length=120)
    picture = models.ImageField("Image", upload_to='media/departament/')
    one_list = models.CharField("One List", max_length=120)
    text1 = models.TextField("Text 1")
    text2 = models.TextField("Text 2")

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"


# Профессоры
class Professors(models.Model):
    name = models.CharField("ФИО", max_length=120)
    post = models.TextField("Post", max_length=250)
    photo = models.ImageField("Photo", upload_to='media/professors/')

    class Meta:
        verbose_name = "Профессор"
        verbose_name_plural = "Профессора"


# У нас учились
class Students(models.Model):
    name = models.CharField("ФИО", max_length=120)
    post = models.TextField("Post", max_length=250)
    photo = models.ImageField("Photo", upload_to='media/students')

    class Meta:
        verbose_name = "У нас учились"
        verbose_name_plural = "У нас учились"


class Practice(models.Model):
    phrase = models.CharField("Phrase", max_length=120)
    text1 = models.TextField("Text 1")
    text2 = models.TextField("Text 2")
    image1 = models.ImageField("Image 1", upload_to='media/practice')
    image2 = models.ImageField("Image 2", upload_to='media/practice')
    image3 = models.ImageField("Image 3", upload_to='media/practice')
    image4 = models.ImageField("Image 4", upload_to='media/practice')

    class Meta:
        verbose_name = "Практика"
        verbose_name_plural = "Практика"


class Science(models.Model):
    one_list = models.CharField("One list", max_length=120)
    image1 = models.ImageField("Image 1", upload_to='media/science')
    image2 = models.ImageField("Image 2", upload_to='media/science')
    text1 = models.TextField("Text 1")
    text2 = models.TextField("Text 2")

    class Meta:
        verbose_name = "Наука"
        verbose_name_plural = "Наука"


class Conference(models.Model):
    conference = models.CharField("Name", default="Conference", max_length=120)
    image1 = models.ImageField("Image 1", upload_to='media/conference')
    text1 = models.TextField("Text 1")
    image2 = models.ImageField("Image 2", upload_to='media/conference')
    text2 = models.TextField("Text 2")
    image3 = models.ImageField("Image 3", upload_to='media/conference')
    text3 = models.TextField("Text 3")

    class Meta:
        verbose_name = "Конференции"
        verbose_name_plural = "Конференции"


class Gallery(models.Model):
    title = models.CharField('Gallery', max_length=120, default="Gallery")
    image1 = models.ImageField("Image 1", upload_to='media/gallery/')
    image2 = models.ImageField("Image 2", upload_to='media/gallery/')
    image3 = models.ImageField("Image 3", upload_to='media/gallery/')
    image4 = models.ImageField("Image 4", upload_to='media/gallery/')
    image5 = models.ImageField("Image 5", upload_to='media/gallery/')
    image6 = models.ImageField("Image 6", upload_to='media/gallery/')
    image7 = models.ImageField("Image 7", upload_to='media/gallery/')
    image8 = models.ImageField("Image 8", upload_to='media/gallery/')
    image9 = models.ImageField("Image 9", upload_to='media/gallery/')
    image10 = models.ImageField("Image 10", upload_to='media/gallery/')
    image11 = models.ImageField("Image 11", upload_to='media/gallery/')

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"


class Answers(models.Model):
    title = models.CharField("Answers", max_length=120, default="Answers")
    question = models.CharField("Question", max_length=250)
    answer = models.TextField("Answer")

    class Meta:
        verbose_name = "Абитуриентам"
        verbose_name_plural = "Абитуриентам"


class Questions(models.Model):
    question = models.CharField("Question", max_length=250)
    answer = models.TextField("Answer")

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"









