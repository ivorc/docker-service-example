import datetime

# Date Time, Service Name, Server Name, Log Level, RequestId, SessionId, Event Name, Text, Data (JSON)
class LogEntry:
    def __init__(self, service_name, server_name, log_level, request_id,
     session_id, event_name, text, data):
       self.date_time = datetime.datetime.now()
       self.service_name = service_name
       self.server_name = server_name
       self.log_level = log_level
       self.request_id = request_id
       self.session_id = session_id
       self.event_name = event_name
       self.text = text
       self.data = data
