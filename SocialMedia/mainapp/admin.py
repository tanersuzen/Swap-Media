from django.contrib import admin
from mainapp.models import Profile



class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username Group',{"fields":["username"]}),
        ('ProfileImage Group',{"fields":["profile_image"]}),
        ('CoverImage Group',{"fields":["cover_image"]}),
        ('Email Group',{"fields":["email"]}),
        ('Age Group',{"fields":["age"]}),
        ('Info Group',{"fields":["info"]})
    ]
    #fields = ['message','nickname']


admin.site.register(Profile,ProfileAdmin)

