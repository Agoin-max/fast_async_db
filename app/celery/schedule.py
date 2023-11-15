from app.celery.run import celery_app
from datetime import timedelta

celery_app.conf.beat_schedule = {
    "update_db": {
        "task": "app.celery.user_tasks.printt",
        "schedule": timedelta(minutes=1),
    },
}