import logging

from settings.settings import base_dir, usuario

log_path = rf'{base_dir}\data\logs\log.log'

logging.basicConfig(
    level=logging.INFO,
    filename=log_path,
    format='%(levelname)s: %(asctime)s - Module: %(module)s Function: %(funcName)s -> %(message)s',
)

logger = logging.getLogger(__name__)

logger.info(f'\nSystem started by user: {usuario}\n')
