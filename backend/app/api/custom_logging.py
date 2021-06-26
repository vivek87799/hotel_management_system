# Custom Logger Using Loguru
import logging
logging.basicConfig(handlers=[logging.FileHandler(filename="./log_records.txt", 
                                                 encoding='utf-8', mode='a')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s", 
                    datefmt="%F %A %T", 
                    level=logging.DEBUG)


class LogModule:
    @staticmethod
    def log_enter_module(module_name):
        logging.info("Entering {} module".format(module_name))
    
    @staticmethod
    def log_message(message, module_name=""):
        logging.info("{}".format(message))
    
    @staticmethod
    def log_error(module_name, error):
        logging.error("Error in {} module, {}".format(module_name, error))
    
    @staticmethod
    def log_exit_module(module_name=""):
        logging.info("Exiting module {}".format(module_name))