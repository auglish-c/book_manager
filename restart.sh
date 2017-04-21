#!/bin/bash
ps aux | grep uwsgi | grep -v grep | awk '{print "kill -9", $2}' | sh
uwsgi --ini ~/book_manager_server/setting/uwsgi.ini &
