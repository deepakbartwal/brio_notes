from django.contrib import admin
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from core.models import *

# Register your models here.

# class NotesInline(NestedStackedInline):
#     """
#     Admin view for adding and viewing notes.
#     """
#     model = Notes
#     extra = 1
#     fk_name = 'category'

# class QuestionPaperInline(NestedStackedInline):
#     """
#     Admin view for adding and viewing question papers.
#     """
#     model = QuestionPaper
#     extra = 1
#     fk_name = 'category'

# class NotesAdmin(NestedModelAdmin):
#     inlines = [
#         NotesInline
#     ]

# class QuestionPaperAdmin(NestedModelAdmin):
#     inlines = [
#         QuestionPaperInline
#    ]
admin.site.register(Notes)
admin.site.register(QuestionPaper)
admin.site.register(Category)
admin.site.register(Stream)
admin.site.register(Notes_Connector)
admin.site.register(QP_Connector)
# admin.site.register(NotesAdmin)
# admin.site.register(QuestionPaperAdmin)
