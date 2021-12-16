from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=128, blank=True)
    start_date = models.DateTimeField('Date published')
    end_date = models.DateTimeField('Date published')
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Type:
        TEXT = 'TEXT'
        CHOICE = 'CHOICE'
        MULTICHOICE = 'MULTICHOICE'

        choices = (
            (TEXT, 'TEXT'),
            (CHOICE, 'CHOICE'),
            (MULTICHOICE, 'MULTICHOICE'),
        )

    poll = models.ForeignKey('Poll', related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    question_type = models.CharField(max_length=200, choices=Type.choices, default=Type.TEXT)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=300)

    def __str__(self):
        return self.Choice_text


class Reply(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.PROTECT)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.PROTECT)
    Choice = models.ForeignKey(Choice, related_name='Choice', on_delete=models.CASCADE, null=True)
    Choice_text = models.CharField(max_length=300, null=True)
