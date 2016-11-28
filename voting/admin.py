from django.contrib import admin
from .models import Voting, Answer


class AnswersInline(admin.TabularInline):
    model = Answer
    extra = 1

@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ['text','is_active','id']
    list_display_links = ['text','id']  # XXX
    search_fields = ['text']
    list_filter = ['is_active']
    inlines = [ AnswersInline ]     # XXX

