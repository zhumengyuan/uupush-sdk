# encoding:utf-8


import json
import requests
import logging


logger = logging.getLogger('uupush')


class UUPush(object):

    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.session = requests.Session()

    def send(self, channel, context, ttl=0, apns=None):
        if self.app_id and self.app_secret:
            headers = {
                'X-APP-ID': self.app_id,
                'X-SECRET-KEY': self.app_secret,
            }
        else:
            headers = {}
        data = json.dumps({
            'context': context,
            'ttl': ttl,
            'apns': apns
        }, ensure_ascii=False).encode('utf8')

        retry = 3
        while retry > 0:
            try:
                resp = self.session.post(channel, data=data, headers=headers)
                logger.info("uupush %s:%s" % (channel, resp.status_code))
                return resp.status_code
            except (requests.exceptions.ConnectionError
                    or requests.exceptions.Timeout):
                retry -= 1
