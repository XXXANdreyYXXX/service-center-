from rest_framework import permissions

class IsEmployee(permissions.BasePermission):
    """
    Доступ только сотрудникам
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'employeeprofile')
    
class IsClient(permissions.BasePermission):
    """
    Клиентский доступ
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        
    def has_object_permission(self, request, view, obj):
         if request.method != 'GET':
             return True
         
