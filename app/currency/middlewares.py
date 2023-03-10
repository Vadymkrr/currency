from time import time

from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        end = time()

        path = request.path
        request_method = request.method
        time_taken = end - start

        RequestResponseLog.objects.create(path=path, request_method=request_method, time=time_taken)

        return response
