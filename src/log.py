import logging

# https://docs.python.org/3.7/library/logging.html#logrecord-attributes
logging.basicConfig(
    filename='logs.log',
    filemode='w+',
    level=20,
    format='%(asctime)s - %(levelname)s:%(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)
log = logging.getLogger()
