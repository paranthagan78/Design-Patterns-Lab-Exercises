class Subject():

    sub_name = 'PDP' # class attribute

    def __init__(self):
        self.code = 12345  # instance attribute

    @staticmethod
    def display():
       sub_name='DS'
       sub_code=1111
       print(sub_name, sub_code)

sub=Subject.display()

subj=Subject()
subj.display()


