from modeltranslation.translator import register, TranslationOptions
from .models import FirstBlock, Management, Departament, Professors, Students, AwardsStudents, AwardsProfessors, \
    AwardsManagement, Practice, Science, Conference, Answers, Questions


@register(FirstBlock)
class FirstBlockTranslationOptions(TranslationOptions):
    fields = (
        'text_facultet1',
        'description_facultet1',
        'text_facultet2',
        'description_facultet2',
        'text_facultet3',
        'description_facultet3',
    )


@register(Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(AwardsManagement)
class AwardsManagementTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(AwardsProfessors)
class AwardsProfessorsTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(AwardsStudents)
class AwardsStudentsTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Departament)
class DepartamentTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'one_list',
        'text1',
        'text2',
    )


@register(Professors)
class ProfessorsTranslationOptions(TranslationOptions):
    fields = ('name', 'post',)


@register(Students)
class StudentsTranslationOptions(TranslationOptions):
    fields = ('name', 'post',)


@register(Practice)
class PracticeTranslationOptions(TranslationOptions):
    fields = ('phrase', 'text1', 'text2')


@register(Science)
class ScienceTranslationOptions(TranslationOptions):
    fields = ('one_list', 'text1', 'text2')


@register(Conference)
class ConferenceTranslationOptions(TranslationOptions):
    fields = ('text1', 'text2', 'text3')


@register(Answers)
class AnswersTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')



