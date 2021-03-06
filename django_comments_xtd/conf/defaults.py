from __future__ import unicode_literals

COMMENT_MAX_LENGTH = 3000

# Extra key to salt the XtdCommentForm
COMMENTS_XTD_SALT = b""

# Whether comment posts should be confirmed by email
COMMENTS_XTD_CONFIRM_EMAIL = True

# Maximum Thread Level
COMMENTS_XTD_MAX_THREAD_LEVEL = 0

# Maximum Thread Level per app.model basis
COMMENTS_XTD_MAX_THREAD_LEVEL_BY_APP_MODEL = {}

# Default order to list comments in
COMMENTS_XTD_LIST_ORDER = ('thread_id', 'order')

# Form class to use
COMMENTS_XTD_FORM_CLASS = "django_comments_xtd.forms.XtdCommentForm"

# Model to use
COMMENTS_XTD_MODEL = "django_comments_xtd.models.XtdComment"

# Send HTML emails
COMMENTS_XTD_SEND_HTML_EMAIL = True

# Whether to send emails in separate threads or use the regular method.
# Set it to False to use a third-party app like django-celery-email or 
# your own celery app.
COMMENTS_XTD_THREADED_EMAILS = True
