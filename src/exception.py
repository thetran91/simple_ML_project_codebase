import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # exc_tb is the only one returned values we need to extract exception information.
    file_name=exc_tb.tb_frame.f_code.co_filename # search "custom exception handling" for using custom exception handling
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
## Create CustomException class to handle exceptions everytime it is encountered. Especial exception in try ... catch
## This class inherits from Exception class.

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        """
        ___str__() for printing the error message
        
        """
        return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Error: Devided to zero value!")
#         raise CustomException(e, sys)