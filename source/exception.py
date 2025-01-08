import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message including the file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Custom Exception class that formats the error message.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    # Main block to test the exception handling
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Divide by Zero Error")  # Use error level for logging exceptions
        raise CustomException(e, sys)
