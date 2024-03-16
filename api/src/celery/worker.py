from celery import Celery
from celery import shared_task
import os
import time

worker = Celery(
    "WORKER",
    backend=os.getenv("CELERY_BACKEND_URL"),
    broker=os.getenv("CELERY_BROKER_URL"),
    include=["src.celery.tasks","src.celery.tasks"],
)

# Optional configuration, see the application user guide.
worker.conf.update(
    result_expires=3600,
)

if __name__ == "__main__":
    worker.start()