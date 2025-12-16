import exceptions
class AppException(Exception):
    status_code=400
    message="application error"

    def __init__(self, message=None):
        super().__init__(message)
        if message:
            self.message=message
class PersonNotFound(AppException):
    status_code = 404
    message = "Person not found"


class PersonAlreadyExists(AppException):
    status_code = 409
    message = "Person already exists"


class InvalidCredentials(AppException):
    status_code = 401
    message = "Invalid email or password"
    