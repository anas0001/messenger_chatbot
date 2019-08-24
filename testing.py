#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 06:11:03 2019

@author: User
"""

payload = {"message":{"text":"hello"}}
payload['recipient'] = {'id': 1234}
payload['notification_type'] = 'REGULAR'
print(payload)

