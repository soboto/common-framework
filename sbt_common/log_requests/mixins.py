# http://stackoverflow.com/questions/15578946/logging-requests-to-django-rest-framework/27928365#27928365

import json

from django.utils.timezone import now

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RequestLogViewMixin(object):
    log_data = None

    """Mixin to log requests"""
    def initial(self, request, *args, **kwargs):
        """Set current time on request"""
        # get data dict
        try:
            data_dict = request.data.dict()
        except AttributeError:  # if already a dict, can't dictify
            data_dict = request.data

        # get IP
        ipaddr = request.META.get("HTTP_X_FORWARDED_FOR", None)
        if ipaddr:
            # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
            ipaddr = ipaddr.split(", ")[0]
        else:
            ipaddr = request.META.get("REMOTE_ADDR", "")

        # save to log
        self.log_data = {
            'requested_at': now(),
            'path': request.path,
            'remote_addr': ipaddr,
            'host': request.get_host(),
            'method': request.method,
            'query_params': request.query_params,
            'data': data_dict,
        }

        # regular intitial, including auth check
        super(RequestLogViewMixin, self).initial(request, *args, **kwargs)

        # add user to log after auth
        # TODO: add user to log after auth

    def finalize_response(self, request, response, *args, **kwargs):
        # regular finalize response
        response = super(RequestLogViewMixin, self).finalize_response(request, response, *args, **kwargs)

        if not self.log_data:
            return response

        # compute response time
        response_timedelta = now() - self.log_data['requested_at']
        response_ms = int(response_timedelta.total_seconds() * 1000)

        # get response dict
        try:
            response_data = json.loads(response.rendered_content)
        except ValueError:  # if already a dict, can't dictify
            response_data = '<<NOT JSON>>'

        # save log
        self.log_data['response'] = response_data
        self.log_data['content_type'] = response['content-type'] if 'content-type' in response else None
        self.log_data['status_code'] = response.status_code
        self.log_data['response_ms'] = response_ms

        # save log_data in some way
        if not hasattr(request, 'enable_log_request'):
            logger.debug(self.log_data)

        # return
        return response

