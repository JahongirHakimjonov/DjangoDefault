from silk.middleware import SilkyMiddleware


class CustomSilkyMiddleware(SilkyMiddleware):
    def process_request(self, request):
        if (
            request.path.startswith("/static/")
            or request.path.startswith("/media/")
            or request.path.startswith("/uz/")
            or request.path.startswith("/ru/")
        ):
            return None
        return super().process_request(request)
