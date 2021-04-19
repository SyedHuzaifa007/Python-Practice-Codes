import logging

def main():
    # Configure The Logging System
    logging.basicConfig(filename='app.log', level=logging.ERROR)

    # Variables (To Make The Calls That Follow Work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example Logging Calls (Insert Into Your Program)
    logging.critical('Host %s is unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')
    
if __name__ == '__main__':
    main()

