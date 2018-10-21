import logging

#create and configure logger
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "D:\\old\\e\\learn\\Python\\Learn_h\\lumberjack.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger=logging.getLogger()

#test the logger
logger.debug("This is hrmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry but i can't do that.")
logger.error("Did you just try to divide by zero?")
logger.critical("The intire internet is down!!.")

#print(logger.level)




