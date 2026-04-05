from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    def has_permission(self, request, view):
        user=request.user

        if user.role=='admin':
            return True
        
        if user.role=='analyst':
            return request.method in ['GET']
        
        if user.role=='viewer':
            return request.method=='GET'
        
        return False
          