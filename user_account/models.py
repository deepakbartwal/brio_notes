from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_noop

# Create your models here.
class UserProfile(models.Model):
    """
    This is where we store all the user demographic fields. We have a
    separate table for this rather than extending the built-in Django auth_user.
    """
    # # cache key format e.g user.<user_id>.profile.country = 'SG'
    # PROFILE_COUNTRY_CACHE_KEY = u"user.{user_id}.profile.country"

    class Meta(object):
        db_table = "auth_userprofile"

    # CRITICAL TODO/SECURITY
    # Sanitize all fields.
    # This is not visible to other users, but could introduce holes later
    user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile')
    name = models.CharField(blank=True, max_length=255, db_index=True)
    meta = models.TextField(blank=True)  # JSON dictionary for future expansion
    # for users imported from our first class.
    language = models.CharField(blank=True, max_length=255, db_index=True)
    location = models.CharField(blank=True, max_length=255, db_index=True)
    # Optional demographic data we started capturing from Fall 2012
    GENDER_CHOICES = (
        ('m', ugettext_noop('Male')),
        ('f', ugettext_noop('Female')),
        # Translators: 'Other' refers to the student's gender
        ('o', ugettext_noop('Other'))
    )
    gender = models.CharField(
        blank=True, null=True, max_length=6, db_index=True, choices=GENDER_CHOICES
    )
    LEVEL_OF_EDUCATION_CHOICES = (
        ('p', ugettext_noop('Doctorate')),
        ('m', ugettext_noop("Master's or professional degree")),
        ('b', ugettext_noop("Bachelor's degree")),
        ('a', ugettext_noop("Associate degree")),
        ('hs', ugettext_noop("Secondary/high school")),
        ('jhs', ugettext_noop("Junior secondary/junior high/middle school")),
        ('el', ugettext_noop("Elementary/primary school")),
        # Translators: 'None' refers to the student's level of education
        ('none', ugettext_noop("No Formal Education")),
        # Translators: 'Other' refers to the student's level of education
        ('other', ugettext_noop("Other Education"))
    )
    level_of_education = models.CharField(
        blank=True, null=True, max_length=6, db_index=True,
        choices=LEVEL_OF_EDUCATION_CHOICES
    )
    STATE_LIST = (
        ('AP',ugettext_noop('Andhra Pradesh')),
        ('AR',ugettext_noop('Arunachal Pradesh')),
        ('AS',ugettext_noop('Assam')),
        ('BR',ugettext_noop('Bihar')),
        ('CG',ugettext_noop('Chhattisgarh')),
        ('CHGH',ugettext_noop('Chandigarh')),
        ('DN',ugettext_noop('Dadra and Nagar Haveli')),
        ('DD',ugettext_noop('Daman and Diu')),
        ('DL',ugettext_noop('Delhi')),
        ('GA',ugettext_noop('Goa')),
        ('GJ',ugettext_noop('Gujarat')),
        ('HR',ugettext_noop('Haryana')),
        ('HP',ugettext_noop('Himachal Pradesh')),
        ('JK',ugettext_noop('Jammu and Kashmir')),
        ('JH',ugettext_noop('Jharkhand')),
        ('KA',ugettext_noop('Karnataka')),
        ('KL',ugettext_noop('Kerala')),
        ('MP',ugettext_noop('Madhya Pradesh')),
        ('MH',ugettext_noop('Maharashtra')),
        ('MN',ugettext_noop('Manipur')),
        ('ML',ugettext_noop('Meghalaya')),
        ('MZ',ugettext_noop('Mizoram')),
        ('NL',ugettext_noop('Nagaland')),
        ('OD',ugettext_noop('Odisha')),
        ('PB',ugettext_noop('Punjab')),
        ('PY',ugettext_noop('Pondicherry')),
        ('RJ',ugettext_noop('Rajasthan')),
        ('SK',ugettext_noop('Sikkim')),
        ('TN',ugettext_noop('Tamil Nadu')),
        ('TR',ugettext_noop('Tripura')),
        ('UP',ugettext_noop('Uttar Pradesh')),
        ('UK',ugettext_noop('Uttarakhand')),
        ('WB',ugettext_noop('West Bengal'))
        )
    state = models.CharField(blank=True, null=True, max_length=6, db_index=True,
        choices=STATE_LIST)
    city = models.CharField(blank=True, max_length=255, db_index=True)
    school_board = models.CharField(blank=True, max_length=255, db_index=True)
    grad_university = models.CharField(blank=True, max_length=255, db_index=True)
    post_grad_university = models.CharField(blank=True, max_length=255, db_index=True)
    # mailing_address = models.TextField(blank=True, null=True)
    # city = models.TextField(blank=True, null=True)
    # country = CountryField(blank=True, null=True)
    # goals = models.TextField(blank=True, null=True)
    # bio = models.CharField(blank=True, null=True, max_length=3000, db_index=False)