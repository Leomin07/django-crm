from rest_framework.pagination import PageNumberPagination


# https://www.django-rest-framework.org/api-guide/pagination/
class StandardResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
