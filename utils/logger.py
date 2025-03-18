import os

class Logger:
    def info(self, message):
        if (os.environ.get('LOG_ON')):
            print('>>>>',message)

    def error(self, message):
        if (os.environ.get('LOG_ON')):
            print('!!!!!ERROR!!!!\n'+message)