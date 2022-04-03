from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "User has no permission"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.method in SAFE_METHODS:
            return True
        else:
            return False

class UserIsHimselfOrRO(BasePermission):
    message = "User has no permission"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if request.user.user_name == obj.user_name or request.method in SAFE_METHODS:
            return True
        else:
            return False