# -*- coding: utf-8 -*-

from django.conf import settings

from rest_framework import pagination
from rest_framework.response import Response

from apps.contrib.utils.dates import local_datetime


class HeaderPagination(pagination.PageNumberPagination):
    """Manages a custom header pagination."""

    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']

    def get_paginated_response(self, response_data) -> Response:
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()
        headers = {
            'x-count': self.page.paginator.count,
            'x-next': next_url if next_url else 'null',
            'x-prev': previous_url if previous_url else 'null',
            'x-timestamp': local_datetime(),
        }

        if next_url or previous_url:
            headers['x-paginated'] = 'true'
            headers['x-page-size'] = self.get_page_size(response_data)

        return Response(response_data, headers=headers)
