from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3                      # per page 3 records show
    page_query_param = 'page_size'     # define tha page number for query page number
    page_size_query_param = 'record'   # per page record show that is diced the client
    max_page_size = 10                 # Number of page
    #last_page_strings = 'end'          # last page define


