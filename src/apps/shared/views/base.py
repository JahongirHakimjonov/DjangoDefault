from django.http import JsonResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


def custom_handler404(request, exception=None):
    return JsonResponse(
        {
            "success": False,
            "message": "Not Found",
        },
        status=404,
    )


def custom_handler500(request):
    return JsonResponse(
        {
            "success": False,
            "message": "Server Error",
        },
        status=500,
    )


def custom_handler403(request, exception=None):
    return JsonResponse(
        {
            "success": False,
            "message": "Forbidden",
        },
        status=403,
    )


def custom_handler400(request, exception=None):
    return JsonResponse(
        {
            "success": False,
            "message": "Bad Request",
        },
        status=400,
    )
