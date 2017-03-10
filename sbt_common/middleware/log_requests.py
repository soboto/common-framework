# http://stackoverflow.com/questions/15578946/logging-requests-to-django-rest-framework/27928365#27928365

import json

from django.utils.timezone import now

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('sbt_common.log_requests')


class LogRequestsMiddleware(object):
    _log_data = None
    _requested_at = None
    IGNORE_METHODS = {
        'OPTIONS',
    }

    def _get_headers(self, request):

        HEADERS = {
            'HTTP_USER_AGENT': 'User-Agent',
            'HTTP_CONTENT_LANGUAGE': 'Content-Language',
            'HTTP_ACCEPT_LANGUAGE': 'Accept-Language',
            'HTTP_AUTHORIZATION': 'Authorization',
            'HTTP_ADAPTER_IDENTIFIER': 'Adapter-Identifier',
        }

        headers = {}
        for field, key in HEADERS.iteritems():
            if field in request.META:
                headers[key] = request.META[field]

        return headers

    def process_request(self, request, *args, **kwargs):
        """Set current time on request"""
        self._requested_at = now()

        if request.method in self.IGNORE_METHODS:
            return

        # get request data
        request_data = request.body

        if '"password"' in request_data and 'auth' in request.path:
            data = json.loads(request_data)
            data['password'] = '*****'
            request_data = json.dumps(data)

        self._log_data = {
            'address': request.get_host() + request.path,
            'http-method': request.method,
            'headers': self._get_headers(request),
            'query-string': request.META.get('QUERY_STRING', ''),
            'payload': request_data,
        }

        # add user to log after auth
        # TODO: add user to log after auth

    def process_response(self, request, response, *args, **kwargs):

        if not self._log_data:
            return response

        # compute response time
        response_ms = 0
        if self._requested_at:
            response_timedelta = now() - self._requested_at
            response_ms = int(response_timedelta.total_seconds() * 1000)

        # get response dict
        try:
            response_data = json.loads(response.rendered_content)
        except:  # if already a dict, can't dictify
            response_data = None

        # save log
        self._log_data['content-type'] = response['content-type'] if 'content-type' in response else None
        self._log_data['status-code'] = response.status_code
        self._log_data['response-time'] = response_ms
        self._log_data['response'] = response_data

        logger.debug(self._log_data)

        # return
        return response
