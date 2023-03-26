import configparser

def get_settings(file):
    """
    Gets settings.ini settings into a dictionary.
    :param file: .ini file extension
    :return: settings dictionary
    """
    config = configparser.ConfigParser(interpolation=None)
    config.read(file)
    settings = {
        'api_key' : config['Twitter']['api_key'],
        'key_secret' : config['Twitter']['key_secret'],
        'bearer_token' : config['Twitter']['bearer_token'], 
        'access_token' : config['Twitter']['access_token'],
        'access_secret' : config['Twitter']['access_secret']
    }

    return settings


