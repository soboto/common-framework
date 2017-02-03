import importlib
from django.core.exceptions import ImproperlyConfigured
import calendar
import datetime
from django.utils.timezone import utc


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
