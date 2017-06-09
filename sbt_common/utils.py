import importlib
from django.core.exceptions import ImproperlyConfigured
import calendar
import datetime
from django.utils.timezone import utc
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text


def import_class(path):
    module_name, class_name = path.rsplit('.', 1)
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        raise ImproperlyConfigured('Could not find module "%s"' % module_name)
    else:
        try:
            return getattr(module, class_name)
        except AttributeError:
            raise ImproperlyConfigured('Cannot import "%s"' % class_name)


def datetime_to_epoch(value):
        try:
            return int(calendar.timegm(value.utctimetuple()))
        except (AttributeError, TypeError):
            return None


def epoch_to_datetime(value):
    return datetime.datetime.utcfromtimestamp(int(value)).replace(tzinfo=utc)


def encode_uid(pk):
    return urlsafe_base64_encode(force_bytes(pk)).decode()


def decode_uid(pk):
    return force_text(urlsafe_base64_decode(pk))


def send_monitoring_task(action, celery_app, request, data=""):
    user_id = -1
    item_id = -1

    if request.user.id is not None:
        user_id = request.user.id

    if hasattr(request, 'item_id'):
        item_id = request.item_id

    params = []
    params.append(action)
    params.append(user_id)
    params.append(item_id)
    params.append(data)

    celery_app.send_task(
        'monitoring_action',
        args=params
    )


class ActionViewMixin(object):
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self._action(serializer)
