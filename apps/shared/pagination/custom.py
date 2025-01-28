from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_size = 5

    def get_paginated_response(self, data):
        paginator = self.page.paginator
        return Response(
            {
                "success": True,
                "message": "Data fetched successfully.",
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "total_items": paginator.count,
                "total_pages": paginator.num_pages,
                "page_size": self.get_page_size(self.request),
                "current_page": self.page.number,
                "data": data,
            }
        )
