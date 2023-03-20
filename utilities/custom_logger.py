import inspect
import logging


def customLogger(logLevel=logging.DEBUG, where="cmd"):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    if where == "file":
        fileHandler = logging.FileHandler("automation.log", mode='a')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        return logger
    elif where == "cmd":
        chandler = logging.StreamHandler()
        chandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        chandler.setFormatter(formatter)
        logger.addHandler(chandler)
        return logger
    else:
        print("Set proper 'WHERE' argument")

