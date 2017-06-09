#!/bin/bash
ps aux | grep uwsgi | grep -v grep | awk '{print "kill -9", $2}' | sh
cd /home/ec2-user/book_manager_server && uwsgi --ini /home/ec2-user/book_manager_server/setting/uwsgi.ini &
