# -*- coding: utf-8 -*-
# @Time    : 2022/10/13 11:02
# @Author  : jinjie
# 创建celery对象，并且添加任务

from celery import Celery
# broker存放需要执行的后台任务，backed存放完成任务后的结果，等待后端调用
#Celery官方推荐的Broker和Backend搭配为：RabbitMQ（Baoker）+Redis（Backend）
from flask_mail import Message
from commons import mail


"""
# 启动监听任务
cmd> celery -A app.celery worker --loglevel=info -P gevent
"""

# 定义任务函数
def send_mail(recipient,subject,body):
  print(recipient,subject,body)
  message = Message(subject=subject,recipients=[recipient],body=body)
  mail.send(message)
  return {"status": "SUCCESS"}


# 创建celery对象
def make_celery(app):
  celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                  broker=app.config['CELERY_BROKER_URL'])
  celery.conf.update(app.config)
  TaskBase = celery.Task
  class ContextTask(TaskBase):
    abstract = True

    def __call__(self, *args, **kwargs):
      with app.app_context():
        return TaskBase.__call__(self, *args, **kwargs)

  celery.Task = ContextTask
  app.celery = celery

  # 添加任务
  celery.task(name="send_mail")(send_mail)

  return celery