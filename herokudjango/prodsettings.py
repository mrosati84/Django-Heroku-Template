import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ('127.0.0.1', 'localhost', 'fierce-sea-6758.herokuapp.com')

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*@ov6)8kv-l@9)4-zkuuy!!&amp;f2qxw1^&amp;10nu65b^&amp;4jno6zo#e'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
