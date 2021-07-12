import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getapplicationurl():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password
