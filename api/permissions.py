from rest_framework.permissions import BasePermission

# class IsOwner(BasePermission):
#     message = "You must be the owner."

#     def has_object_permission(self, request, view, obj):
#         if request.user.is_staff or (obj.owner == request.user):
#             return True
#         else:
#             return False
