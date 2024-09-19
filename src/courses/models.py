from django.db import models

# Create your models here.
"""
# Building a Course Platform

## Overview
What we are building

- Courses:
	- Title
	- Description
	- Thumbnail/Image
	- Access:
		- Anyone
		- Email required
        - Purchase required
		- User required (n/a)
	- Status: 
		- Published
		- Coming Soon
		- Draft
"""
class AccessRequirement(models.Textchoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email_required', 'Email Required'
    PURCHASE_REQUIRED = 'purchase_required', 'Purchase Required'
    USER_REQUIRED = 'user_required', 'User Required'

class PublishStatus(models.TextChoices):
    PUBLISHED = 'published', 'Published'
    COMING_SOON = 'coming_soon', 'Coming Soon'
    DRAFT = 'draft', 'Draft'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
#     thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    access = models.CharField(max_length=20,
                               choices=AccessRequirement.choices,
                               default=AccessRequirement.ANYONE
                               )
    
    status = models.CharField(max_length=20, 
                              choices=PublishStatus.choices, 
                              default=PublishStatus.DRAFT
                              )
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED


"""
	- Lessons
		- Title
		- Description
		- Video
		- Status: Published, Coming Soon, Draft
"""



"""
- Email verification for short-lived access
	- Views:
		- Collect user email
		- Verify user email
			- Activate session
	- Models:
		- Email
		- EmailVerificationToken
"""