# -*- coding: utf-8 -*-
# generate_secret.py
from django.core.management import utils

print(utils.get_random_secret_key())
