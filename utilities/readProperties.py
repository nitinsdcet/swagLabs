import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        userEmail = config.get('common info', 'username')
        return userEmail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getFirstName():
        firstName = config.get('common info', 'firstName')
        return firstName

    @staticmethod
    def getLastName():
        lastName = config.get('common info', 'lastName')
        return lastName

    @staticmethod
    def getZip():
        zip = config.get('common info', 'zip')
        return zip


