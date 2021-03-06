from .common import *

DEBUG = False
ALLOWED_HOSTS = ['bizchoollab.pythonanywhere.com', '127.0.0.1', 'bizchoollab.com']


AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'bizchoolblog'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION_STATIC = 'static'
AWS_LOCATION_MEDIA = 'media'


AWS_DEFAULT_ACL = 'public-read'


# STATIC_DIRS = os.path.join(BASE_DIR, 'mysite', 'static')
# STATICFILES_DIRS = [
#     STATIC_DIRS
# ]
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION_STATIC)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'


MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION_MEDIA)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
