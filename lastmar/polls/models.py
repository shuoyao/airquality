from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class mcsv(models.Model):
    col1 = models.CharField(max_length=200)
    col2 = models.CharField(max_length=200)
    col3 = models.CharField(max_length=200)
   
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
   
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     c1 = models.CharField(max_length=200)
#     c2 = models.CharField(max_length=200)
#     c3 = models.CharField(max_length=200)
#     sub = models.BooleanField(default = False)

@python_2_unicode_compatible 
class Survey(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text


   
@python_2_unicode_compatible
class Response(models.Model):
    # question = models.ForeignKey(Survey, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=5)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    # YEAR_IN_SCHOOL_CHOICES = (
    #     (FRESHMAN, 'Freshman'),
    #     (SOPHOMORE, 'Sophomore'),
    #     (JUNIOR, 'Junior'),
    #     (SENIOR, 'Senior'),
    # )
    
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    YES_NO_CHOICES = (
        (ONE, 'Yes'),
        (TWO, 'No'),
    )

    INCOME_CHOICES = (
        (ONE, '$25,000 or less'),
        (TWO, '$25,001 - $50,000'),
        (THREE, '$50,001 - $75,000'),
        (FOUR, '$75,001 - $100,000'),
        (FIVE, 'Above $100,000'),
    )



    EDUCATION_CHOICES = (
        (ONE, 'Not Graduate from High school'),
        (TWO, 'High school'),
        (THREE, 'College'),
        (FOUR, 'Graduate school'),
        (FIVE, 'Post Grduate'),
    )
    AGE_CHOICES = (
        (ONE, '18-24'),
        (TWO, '25-34'),
        (THREE, '35-44'),
        (FOUR, '45-54'),
        (FIVE, '55-64'),
        (SIX, '65+'),
    )
    POLITICS_CHOICES = (
        (ONE, 'Very conservative'),
        (TWO, 'Moderately conservative'),
        (THREE, 'Neither'),
        (FOUR, 'Moderately liberal'),
        (FIVE, 'Very liberal'),
    )

    # year_in_school = models.CharField(max_length=2,
    #                                   choices=YEAR_IN_SCHOOL_CHOICES,
    #                                   default=FRESHMAN)
    support_or_not = models.IntegerField(max_length=100,
                                      choices=YES_NO_CHOICES,
                                      default=ONE)

    email_or_not = models.IntegerField(max_length=100,
                                  choices=YES_NO_CHOICES,
                                  default=ONE)

    income = models.IntegerField(max_length=200,
                                  choices=INCOME_CHOICES,
                                  default=ONE)

    education = models.IntegerField(max_length=200,
                              choices=EDUCATION_CHOICES,
                              default=ONE)

    age = models.IntegerField(max_length=200,
                              choices=AGE_CHOICES,
                              default=ONE)

    politics = models.IntegerField(max_length=200,
                              choices=POLITICS_CHOICES,
                              default=ONE)


    def __str__(self):
        return str(self.zipcode)

    
