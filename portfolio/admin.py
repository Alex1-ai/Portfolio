from django.contrib import admin
from .models import Experience,Achievement, Education, Personal_Information, Skills,PortfolioGallery,Portfolio,Contact
# Register your models here.
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class PortfolioGalleryInline(admin.TabularInline):
    model = PortfolioGallery
    extra = 1


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ["product_name"]}
    list_display = ['title', 'langauge',
                    'link', 'client', 'project_type', 'image' ]
    inlines = [PortfolioGalleryInline]

@admin.register(Personal_Information)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','profession','email', 'created_at','updated_at']

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['years_of_experience','completed_projects','happy_customers','awards'
                    ]



@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name','level', 'created_at','updated_at'
                    ]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree','university','year', 'created_at','updated_at'
                    ]



@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position','company','year', 'created_at','updated_at'
                    ]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email', 'message'
                    ]
