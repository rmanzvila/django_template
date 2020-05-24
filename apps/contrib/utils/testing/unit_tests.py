# -*- coding: utf-8 -*-

from django.core import mail

from faker import Factory
from faker.providers import misc, profile

fake = Factory.create()
fake.add_provider(profile)
fake.add_provider(misc)


def mail_outbox():
    return len(mail.outbox)


def has_valid_format(reponse):
    response_json = reponse.json()
    return (
        isinstance(response_json, dict) and
        {'code', 'message'} <= set(response_json.keys())
    )


class ResponseMock:

    def __init__(self, content=None):
        self.content = content or {}

    def json(self, data=None):
        return self.content
