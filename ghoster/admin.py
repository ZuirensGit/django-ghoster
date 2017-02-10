from django.contrib import admin



class GhosterAdmin(admin.ModelAdmin):
    markdown_field = None
    title_field = None
    add_form_template = 'admin/ghoster_change_form.html'
    change_form_template = 'admin/ghoster_change_form.html'
