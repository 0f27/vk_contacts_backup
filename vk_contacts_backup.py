#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#
import vk,sys,csv

session = vk.AuthSession(app_id=sys.argv[1],user_login=sys.argv[2],user_password=sys.argv[3])
api = vk.API(session)
friend_ids = api.friends.get()
contacts = api.users.get(user_ids=friend_ids,fields='bdate,contacts,sex,photo_max')

with open('contacts_vk.csv', 'w', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['uid', 'first_name', 'last_name', 'sex', 'home_phone', 'mobile_phone', 
'bdate', 'photo_max', 'deactivated'])
    w.writeheader()
    for i in contacts:
        w.writerow(i)
