import os
from configparser import ConfigParser

class AppConfig(object):
    def __init__(self):
        super(AppConfig, self).__init__()
        self.config = ConfigParser()
        self.config.read('./config.ini')

    def get_base_url(self):
        return self.config.get('api', 'base_url')

    def get_db_file(self):
        return self.config.get('db', 'file')

config = AppConfig()
