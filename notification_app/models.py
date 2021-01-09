from django.db import models
from users.models import User
from django.core.mail import EmailMessage

class notification_model(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    subject = models.CharField(max_length=400,default='')
    body = models.TextField(max_length=4000)
    notification_type = models.BooleanField(default=True) # True = arrow  /  False = comment
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class notification_pref(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    rfs_daily = models.BooleanField(default=False)
    rfs_week = models.BooleanField(default=False)
    comment_mention = models.BooleanField(default=False)
    comment_reply = models.BooleanField(default=False)
    play_sound = models.BooleanField(default=False)
    before_auction = models.BooleanField(default=False)
    new_bids = models.BooleanField(default=False)
    new_comments = models.BooleanField(default=False)
    questions_answered = models.BooleanField(default=False)
    auction_results = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


####### Use this function for notifications

def send_notification(user_obj,subject_text,body_text):
    """
    user is the user object
    """
    obj = notification_model()
    obj.user = user_obj
    obj.subject = subject_text
    obj.body = body_text
    obj.save()
    email_obj = EmailMessage(
        subject=subject_text,
        body=body_text,
        to=[user_obj.email],
    )
    email_obj.send()
    return 1