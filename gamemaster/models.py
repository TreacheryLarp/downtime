from django.db import models
from django_comments.signals import comment_was_posted
from django.core.mail import send_mail


# Signals
def notify_user_about_comment(sender, **kwargs):
    try:
        comment = kwargs['comment']

        # Only send on GM comment
        if not comment.user.is_staff:
            return

        target_object = comment.content_object
        receipient_user = target_object.character.user
        to_address = receipient_user.email
        html = """
        <html>
        <body>
            <h2>Treachery Downtime Notification</h2>
            <p>
                Hi %s!
                <br><br>
                You have recieved a new comment on one of your downtime actions. Please login and reply if needed.
                <br><br>
                <b>%s</b> commented on your action <i>%s</i>:
                <br><br>
                <div style='padding-left:10px'>
                %s
                </div>
            </p>
        </body>
        </html>
        """ % (receipient_user.username, comment.name, target_object,
               comment.comment)

        send_mail('[Treachery Downtime]: New comment',
                  '',
                  '',
                  [to_address],
                  fail_silently=True,
                  html_message=html)
    except:
        print('Error while sending mail notification: %s' % kwargs)


comment_was_posted.connect(notify_user_about_comment)
