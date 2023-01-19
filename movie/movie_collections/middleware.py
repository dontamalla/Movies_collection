from django.utils.deprecation import MiddlewareMixin

class RequestCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.session['request_count'] = request.session.get('request_count', 0) + 1
