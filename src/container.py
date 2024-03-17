"""Application Container"""

import os
import logging.config
import boto3

from dependency_injector import containers, providers

from common.fs_helper import LocalFsHelper

FILE_DIR = os.path.dirname(__file__)
DEFAULT_CONFIG = os.path.join(FILE_DIR, './configs/config.yml')
DB_CONFIG = os.path.join(FILE_DIR, './configs/encrypted_credentials.yaml')
LOGGING_FILE = os.path.join(FILE_DIR, './configs/logging.ini')


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=[DEFAULT_CONFIG])
    db_config = providers.Configuration(yaml_files=[DB_CONFIG])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname=LOGGING_FILE
    )

    local_fs_helper = providers.Singleton(
        LocalFsHelper
    )

