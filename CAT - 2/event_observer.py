class Participants:
    def __init__(self, name):
        self.name=name

    def update(self,event_name,date, ieee_event):
        print(f'Hi {self.name}. A new event {event_name} is conducted by the IEEE {ieee_event.soceity_name} on {date}')

class IEEE_Events():
    def __init__(self, soceity_name):
        self.soceity_name=soceity_name
        self.__dates=[]
        self.__participants=[]
        self.__events=[]
        
    def add_event(self,event_name,date):
        self. __events.append(event_name)
        self. __dates.append(date)
        self.alert_participants(event_name,date)
        
    def IEEE_MemParticipant(self,participant):
        self.__participants.append(participant)
        
    def IEEE_RemoveParticipant(self, participant):
        return self.__participants.remove(participant)

    def alert_participants(self,event_name,date):
        for participant in self.__participants:
            participant.update(event_name,date,self)

    def __str__(self):
        return self.__participants, self.__events, self.__dates
         

ieee_event=IEEE_Events('Computer Soceity')

participant1=Participants('John')
participant2=Participants('Jessy')

ieee_event.IEEE_MemParticipant(participant1)
ieee_event.IEEE_MemParticipant(participant2)

ieee_event.add_event('IEEEXtreme', '1-1-23')

ieee_event.IEEE_RemoveParticipant(participant2)

ieee_event.add_event('Guest Lecture Series', '2-1-23')

#print(ieee_event.__str__())
