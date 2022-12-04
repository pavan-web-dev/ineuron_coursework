# import logging
# logging.basicConfig(filename='simple.log',filemode='w',format='%(asctime)s %(name)s %(levelname)s %(message)s',level=logging.DEBUG)
# print_as_well = logging.StreamHandler()
# print_as_well.setLevel(logging.DEBUG)
# print_as_well.setFormatter(logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s %(message)s'))
# logging.getLogger().addHandler(print_as_well)

# my_logger  = logging.getLogger()

# my_logger.debug('Trial 1')

import logging

logger = logging.getLogger('user')
logger.setLevel(logging.DEBUG)
# Add a file handler
file_handler = logging.FileHandler('simple_.log',mode = 'w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
logger.addHandler(file_handler)

# Stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
logger.addHandler(stream_handler)
# Add the handler to the main logger



logger.debug('Test1')
logger.info('Test2')
logger.warning('Wrath')