#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Dump all replication events from a remote mysql server
#
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.event import QueryEvent, RotateEvent, FormatDescriptionEvent
MYSQL_SETTINGS = {
    "host": "10.xx",
    "port": 3333,
    "user": "admin",
    "passwd": "admin"
}
def main():
    stream = BinLogStreamReader(  
        connection_settings=MYSQL_SETTINGS,  
        server_id=3,  
        blocking=True,  
        only_schemas=["jintui"],  
        only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent])  
    producer = KafkaProducer(kafka_setting,topic_setting)  
    for binlogevent in stream:  
        for row in binlogevent.rows:  
            event = {"schema": binlogevent.schema, "table": binlogevent.table}  
            if isinstance(binlogevent, DeleteRowsEvent):  
                event["action"] = "delete"  
                event["values"] = dict(row["values"].items())  
                event = dict(event.items())  
            elif isinstance(binlogevent, UpdateRowsEvent):  
                event["action"] = "update"  
                event["before_values"] = dict(row["before_values"].items())  
                event["after_values"] = dict(row["after_values"].items())  
                event = dict(event.items())  
            elif isinstance(binlogevent, WriteRowsEvent):  
                event["action"] = "insert"  
                event["values"] = dict(row["values"].items())  
                event = dict(event.items())  
            print json.dumps(event)  
            sys.stdout.flush()  
  
  
    stream.close()  
  
  
if __name__ == "__main__":  
    main()  
if __name__ == "__main__":
    main()
        


