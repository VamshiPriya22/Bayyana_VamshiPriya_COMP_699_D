class AppException(Exception):
    """Base Exception for application"""
    def __init__(self, message="Application error occurred"):
        self.message = message
        super().__init__(self.message)


class ValidationException(AppException):
    """Validation related errors"""
    pass


class NotFoundException(AppException):
    """Resource not found"""
    pass


class PermissionException(AppException):
    """Permission denied"""
    pass