# AWS SQS and Email Services

Server needs few thing in it to run successfully which is listed below

## Technologies

- Python version  3.11 & above

### Install requirements of project

```bash
$ pip install -r requirements.txt
```

### create config.ini in the root directory of project where manage.py placed

```bash
$ nano config.ini
```

### Copy all sections and key-value pairs from `.ini.sample` or from below:

```ini
[Email]
EMAIL_HOST = 
EMAIL_PORT = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 
FROM_ALIAS = 

[AWS]
AWS_ACCESS_KEY = 
AWS_SECRET_ACCESS_KEY = 
GERMINATION_QUEUE_URL = 
GERMINATION_DLQ_QUEUE_URL = 

PLANET_IMAGERY_QUEUE_URL = 

[PLANET]
API_KEY = 
SEARCH_ITEM_URL = 
ORDER_URL = 

```

### Run Django Server using below command

```bash
$ python manage.py runserver
```