# Initializes the Flask app

import os
import logging
from flask import Flask
from config import DefaultConfig
from analyze import analyze_route


def create_app(config=None):
    """
    Create and configure the Flask app
    :param config: Optional configuration object to override defaults
    :return: Configured Flask app instance
    """
    app = Flask(
        DefaultConfig.PROJECT,  # App name
        instance_relative_config=True  # Allow relative config loading
    )

    # Load configuration
    app.config.from_object(config or DefaultConfig)

    # Set up logging
    configure_logging(app)

    # Register all routes
    analyze_route(app)

    return app


def configure_logging(app):
    """
    Configures rotating file logging for the application
    :param app: Flask app instance
    """
    from logging.handlers import RotatingFileHandler

    log_path = os.path.join(app.config["LOG_FOLDER"], "info.log")

    file_handler = RotatingFileHandler(log_path, maxBytes=100000, backupCount=5)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
