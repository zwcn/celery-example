from celery.result import AsyncResult
from app import app

async_result = AsyncResult(id='f08fd46a-88f7-4743-9bc1-7ef1de4980b8', app=app)

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print('failed')
else:
    print(async_result.status)


async_result = AsyncResult(id='9fd37546-5445-468e-b477-7ff860d8238a', app=app)

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print('failed')
else:
    print(async_result.status)
