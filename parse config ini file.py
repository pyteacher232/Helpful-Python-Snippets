import configparser

# parse config file
config = configparser.RawConfigParser()
config.read('config.ini')
Username = config['DEFAULT']['Username']
Password = config['DEFAULT']['Password']
state = config['CODE']['State']
NPA = config['CODE']['NPA']
OCN = config['CODE']['OCN']
parameters = config['CODE']['Quantity of Blocks Requested']