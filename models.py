
class Index:

    def __init__(self, title='index', content='index'):
        self.__title = title
        self.__content = content

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        self.__content = content
