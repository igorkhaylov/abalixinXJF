from django.contrib import admin
from .models import FirstBlock, Management, Departament, Professors, Students, AwardsManagement, AwardsProfessors, \
    AwardsStudents, Practice, Science, Conference, Gallery, Answers, Questions
from modeltranslation.admin import TranslationAdmin


# @admin.register(Awards)
class AwardsManagementInline(admin.StackedInline):
    model = AwardsManagement
    extra = 1


class AwardsProfessorsInline(admin.StackedInline):
    model = AwardsProfessors
    extra = 1


class AwardsStudentsInline(admin.StackedInline):
    model = AwardsStudents
    extra = 1


@admin.register(FirstBlock)
class FirstBlockAdmin(TranslationAdmin):
    list_display = ('text',)
    list_display_links = ('text', )
    readonly_fields = ('text', )
    save_on_top = True

    # def response_add(self, request, obj, post_url_continue=None):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Management)
class ManagementAdmin(TranslationAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    inlines = [
        AwardsManagementInline,
    ]
    save_as = True


@admin.register(Departament)
class DepartamentAdmin(TranslationAdmin):
    list_display = ('title', )
    list_display_links = ('title', )


@admin.register(Professors)
class ProfessorsAdmin(TranslationAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    inlines = [
        AwardsProfessorsInline,
    ]


@admin.register(Students)
class StudentsAdmin(TranslationAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    inlines = [
        AwardsStudentsInline,
    ]


@admin.register(Practice)
class PracticeAdmin(TranslationAdmin):
    list_display = ('phrase', )
    list_display_links = ('phrase', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Science)
class ScienceAdmin(TranslationAdmin):
    list_display = ('one_list', )
    list_display_links = ('one_list', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Conference)
class ConferenceAdmin(TranslationAdmin):
    list_display = ('conference', )
    list_display_links = ('conference', )
    readonly_fields = ('conference', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    readonly_fields = ('title', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Answers)
class AnswersAdmin(TranslationAdmin):
    list_display = ('question',)
    list_display_links = ('question', )
    readonly_fields = ('title', )


@admin.register(Questions)
class QuestionsAdmin(TranslationAdmin):
    list_display = ('question', )
    list_display_links = ('question', )




# admin.site.register(FirstBlock)

