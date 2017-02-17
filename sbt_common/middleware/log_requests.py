# http://stackoverflow.com/questions/15578946/logging-requests-to-django-rest-framework/27928365#27928365

import json

from django.utils.timezone import now

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('sbt_common.log_requests')


class LogRequestsMiddleware(object):
    _log_data = None

    def process_request(self, request, *args, **kwargs):
        """Set current time on request"""
        # get data dict
        try:
            data_dict = request.body.dict()
        except AttributeError:  # if already a dict, can't dictify
            data_dict = request.body

        # get IP
        ipaddr = request.META.get("HTTP_X_FORWARDED_FOR", None)
        if ipaddr:
            # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
            ipaddr = ipaddr.split(", ")[0]
        else:
            ipaddr = request.META.get("REMOTE_ADDR", "")

        self._log_data = {
            'requested_at': now(),
            'path': request.path,
            'remote_addr': ipaddr,
            'host': request.get_host(),
            'method': request.method,
            'query_params': request.META.get('QUERY_STRING', ''),
            'request_data': data_dict,
        }

        # add user to log after auth
        # TODO: add user to log after auth

    def process_response(self, request, response, *args, **kwargs):

        if not self._log_data:
            return response

        # compute response time
        response_timedelta = now() - self._log_data.pop('requested_at')
        response_ms = int(response_timedelta.total_seconds() * 1000)

        # get response dict
        try:
            response_data = json.loads(response.rendered_content)
        except ValueError:  # if already a dict, can't dictify
            response_data = '<<NOT JSON>>'

        # save log
        self._log_data['content_type'] = response['content-type'] if 'content-type' in response else None
        self._log_data['status_code'] = response.status_code
        self._log_data['response_ms'] = response_ms

        logger.debug(response_data, extra=self._log_data)

        # return
        return response
