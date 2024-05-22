from rest_framework import permissions



class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsLandlordUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'landlord'


class ISTenantUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'tenant'