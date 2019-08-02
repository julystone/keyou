import configparser
from common import constants


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(constants.globalroute, encoding='utf-8')
        open = self.config.getboolean('switch', 'open')

        if open:
            self.config.read(constants.testroute, encoding='utf-8')
        else:
            self.config.read(constants.test2route, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)
