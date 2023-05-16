from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
            
        print('has_permission method is called--->')
        if request.user and request.user.is_authenticated:
            print('user is Authenticated--->')
            return True
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return False

        elif str(request.user) == obj.owner :
            return True