"""
class User: 
    def __init__(self, name):
        self.name = name
    
    def update(self, article, blog_writer):
        print(f'For {self.name}, new article {article} by {blog_writer.name} is added')

class BlogWriter:
    '''
    BlogWriter class is useful to blog writer to add new article
    and manage subscribers as well
    '''
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.articles = [] # Article is the subject

    def add_article(self, article):
        '''
        Add new article and notify subscribers
        '''
        self.articles.append(article)
        self.notify_subscribers(article)

    def get_articles(self):
        '''
        Get articles written by {self}
        '''
        return self.articles

    def subscribe(self, subscriber):
        '''
        Add new subscriber to notify on adding article
        '''
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        '''
        User can unsubscribe from further notifications
        '''
        return self.subscribers.remove(subscriber)

    def subscribers(self):
        '''
        Get subsribers
        '''
        return self.subscribers

    def notify_subscribers(self, article):
        '''
        Notifying all the subsribers about new addition of an article
        '''
        for sub in self.subscribers:
            sub.update(article, self)
            
     
            

if __name__ == '__main__':
    blog_writer = BlogWriter('Hardik\'s blog')
    shailaja = User('Shailaja')
    aarav = User('Aarav')
    blog_writer.subscribe(shailaja)
    blog_writer.subscribe(aarav)
    blog_writer.add_article('Article 1')
    blog_writer.unsubscribe(aarav)
    blog_writer.add_article('Article 2')
    
"""

class User:
    def __init__(self,name):
        self.name=name
    
    def update(self,article,blog_writer):
        print(f"{self.name}, {article} has been Published by {blog_writer.name}.")

class BlogWriter:
    def __init__(self,name):
        self.name=name
        self.articles=[]
        self.subscribers=[]
    
    def add_subscriber(self,subscriber):
        return self.subscribers.append(subscriber)
    
    def remove_subscriber(self,subscriber):
        return self.subscribers.remove(subscriber)
    
    def add_article(self, article):
        self.articles.append(article)
        return self.notify(article)
    
    def remove_article(self,article):
        return self.articles.remove(article)
    
    def get_articles(self):
        return self.articles
    
    def notify(self,article):
        for sub in self.subscribers:
            sub.update(article,self)

blog_writer=BlogWriter("Blog writer Edward")
raja=User("Raja")
dharun=User("Dharun")
blog_writer.add_subscriber(dharun)
blog_writer.add_subscriber(raja)  
blog_writer.add_article("Hello World By Me")
