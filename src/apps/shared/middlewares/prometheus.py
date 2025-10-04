import time

from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from prometheus_client import Counter, Histogram

REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request duration by path", ["path"])
REQUEST_COUNT = Counter("http_request_total", "Total HTTP requests by path and status", ["path", "status"])


class MetricsMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest) -> HttpResponse | None:
        request.META["metrics_start_time"] = time.time()
        return None

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        start_time = request.META.get("metrics_start_time")
        if start_time is not None:
            duration = time.time() - start_time
            path = request.path
            REQUEST_LATENCY.labels(path=path).observe(duration)
            REQUEST_COUNT.labels(path=path, status=response.status_code).inc()
        return response
