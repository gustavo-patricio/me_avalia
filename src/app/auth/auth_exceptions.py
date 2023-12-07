from rest_framework import exceptions

class PermissionException(exceptions.APIException):
    """Erros de permissao
    
    """
    def __init__(self, detail, code=None):
        self.status_code = code
        self.detail = detail
