from app.celery.run import celery_app

@celery_app.task
def printt():
    print("task start run.")