#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Dump all replication events from a remote mysql server
#
from pymysqlreplication import BinLogStreamReader
MYSQL_SETTINGS = {
    "host": "10.200.142.50",
    "port": 3333,
    "user": "admin",
    "passwd": "admin"
}
def main():
    # server_id is your slave identifier, it should be unique.
    # set blocking to True if you want to block and wait for the next event at
    # the end of the stream
    stream = BinLogStreamReader(connection_settings=MYSQL_SETTINGS,
                                server_id=503333,
                                blocking=True)

    for binlogevent in stream:
        print("event_type%s", binlogevent.event_type)
	if binlogevent.event_type == 30:
   	    for row in binlogevent.rows:
	        print(row)
        #binlogevent.dump()
    stream.close()
if __name__ == "__main__":
    main()

