# bookshelf/middleware.py

class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # This header tells the browser to only trust scripts/styles from your own site
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self';"
        return response