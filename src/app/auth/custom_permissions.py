from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework import status
from rest_framework import exceptions

from app import auth


class CoordinatorPermission(BasePermission):
    """Nível de permissao de Coordenador

    Args:
        BasePermission (_type_): classe de permissão
    """
    permission_title = 'coordenador'
    def has_permission(self, request, view):
        try:
            if not request.user.is_authenticated:
                raise auth.PermissionException(code=401, detail=[{'msg': 'usuario nao autenticado'}])

            if not request.user.groups.filter(name=self.permission_title).exists():
                raise auth.PermissionException(code=403, detail=[{'msg': f'usuario não possui permissão de {self.permission_title}'}])
            
            return True
        except exceptions.APIException as e:
            raise e

class StudentPermission(BasePermission):
    """Nível de permissão de Aluno

    Args:
        BasePermission (_type_): classe de permissão
    """
    permission_title = 'estudante'

    def has_permission(self, request, view):
        try:
            if not request.user.is_authenticated:
                raise auth.PermissionException(code=401, detail=[{'msg': 'usuario nao autenticado'}])

            if not request.user.groups.filter(name=self.permission_title).exists():
                raise auth.PermissionException(code=403, detail=[{'msg': f'usuario não possui permissão de {self.permission_title}'}])
            
            return True
        except exceptions.APIException as e:
            raise e


