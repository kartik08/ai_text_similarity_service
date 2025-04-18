import os

from utils import make_dir

class BaseConfig(object):

    """
    Base Config for the Flask App
    :param config: Flask app instance config
    """

    # Name of the PROJECT
    PROJECT = "ai_text_similarity_service"

    # Get Dir path of this PROJECT
    PROJECT_ROOT= os.path.abspath(os.path.dirname(__file__))

    # Logging FOLDER
    LOG_FOLDER = make_dir(PROJECT_ROOT +"\logs")

    DEBUG = False

class DefaultConfig(BaseConfig):

    """
    Default Config for the Flask App
    :Inherting BaseConfig: Flask app BaseConfig 
    """

    DEBUG = True


temp = BaseConfig()


