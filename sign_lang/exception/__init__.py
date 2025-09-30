# ─────────────────────────────────────────────────────────────
# Custom Exception Handler — Traceable, Audit-Friendly Errors
# ─────────────────────────────────────────────────────────────

import sys

# Extracts detailed traceback info for debugging and audit logs
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()                    # get traceback object

    file_name    = exc_tb.tb_frame.f_code.co_filename         # source file
    line_number  = exc_tb.tb_lineno                           # line where error occurred

    # Structured error message for logging and traceability
    return f"Error in script [{file_name}] at line [{line_number}]: {str(error)}"


# Custom exception class for consistent error formatting
class AppException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)

        # Attach full traceback context to the exception
        self.error_message = error_message_detail(
                                                    error_message, 
                                                    error_detail = error_detail
                                                 )

    def __str__(self):
        return self.error_message