from rest_framework.permissions import BasePermission


class IsWebsiteOwner(BasePermission):
    message = 'You must be this website'

    def has_object_permission(self, request, view, obj):
        if request.method in 'GET' and obj.user == request.user:
            return True


class IsWebSiteUser(BasePermission):
    message = 'You must be th owner of this website '

    def has_object_permission(self, request, view, obj):
        if obj.website.user == request.user:
            return True
