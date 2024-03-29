class CallEvent:

    def __init__(self, sender, reciever, timestamp):
        self.sender = sender
        self.reciever = reciever
        self.timestamp = timestamp

class Call(CallEvent):
    def __init__(self, sender, reciever, timestamp):
        super().__init__(sender, reciever, timestamp)
        self.name = 'call'

class Hangup(CallEvent):
    def __init__(self, sender, reciever, timestamp, ):
        super().__init__(sender, reciever, timestamp)
        self.name = 'hangup'

def main(ListOfEvents):
    active_calls = {}
    call_durations = {}
    for event in ListOfEvents:
        action, sender, reciever, timestamp = event.name, event.sender, event.reciever, event.timestamp
        timestamp = int(timestamp)
        participants = frozenset([sender, reciever])
        if action == "call":
            active_calls[participants] = (timestamp, sender)
        elif action == "hangup":
            if participants in active_calls:
                start_time, initiater = active_calls.pop(participants)
                duration  = timestamp - start_time
                if initiater in call_durations:
                    call_durations[initiater]["total_duration"] += duration
                    call_durations[initiater]["call_count"] += 1
                else:
                    call_durations[initiater] = {"total_duration": duration, "call_count": 1}
    result = [initiator for initiator, details in call_durations.items() 
              if details['call_count'] > 0 and (details['total_duration'] / details['call_count']) < 10]
    return result
