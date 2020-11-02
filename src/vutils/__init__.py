import requests
import logging

log = logging.getLogger('main')


def send_heartbeat(endpoint, status='running', info_message=None, failure_reason=None, *args, **kwargs):
    """
    Send a "heartbeat"
    :param endpoint:
    :param status:
    :return:
    """
    if not endpoint:
        return
    try:
        data = {'status': status}
        if info_message:
            data['infoMs'] = info_message
        if status == 'failed':
            data['failure_reason'] = failure_reason
        requests.post(endpoint, data=data)
    except:
        log.exception("An error occurred sending the heartbeat")
    return
