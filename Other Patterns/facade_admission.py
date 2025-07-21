"""
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This pattern can be seen in the Python standard library.
"""
class Online_appl:

    def submission(self):
        print("submit the application")

class Call_letter:
    
    def notification(self):
        print("Sent call letter for interview")


class Interview:
    
    def attend(self):
        print("Attend interview")

class Fee_Payment:
    
    def selected(self):
        print("Proceed for fee payment")


class AdmissionFacade:
    
    def __init__(self):
        #self.name=name
        self.online_appl = Online_appl()
        self.call_letter = Call_letter()
        self.interview = Interview()
        self.fee_Payment = Fee_Payment()
        
    def start(self):
        self.online_appl.submission()
        self.call_letter.notification()
        self.interview.attend()
        self.fee_Payment.selected()
        

#driver code
        
admission_facade = AdmissionFacade()
admission_facade.start()


print(100*"-")

class development:
    def plot(self):
        print("Developing the Plot")

class pre_production:
    def story(self):
        print("Writing the Story in the scene paper")

class production:
    def direction(self):
        print("Directing the Movie")

class post_production:
    def cgi(self):
        print("Working on CGI Works")

class distribution:
    def sale(self):
        print("Selling the Movies to all the distributor")

class release:
    def __init__(self):
        self.development=development()
        self.pre_production=pre_production()
        self.production=production()
        self.post_production=post_production()
        self.distribution=distribution()
    
    def start(self):
        self.development.plot()
        self.pre_production.story()
        self.production.direction()
        self.post_production.cgi()
        self.distribution.sale()

rel=release()
rel.start()
