from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina korish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # ozgartirish uchun faqatgina post muallifi uchun
        return obj.author == request.user
    