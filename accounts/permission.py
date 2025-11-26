# # accounts/permissions.py
# from rest_framework.permissions import BasePermission

# class IsDoctor(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         return bool(user and user.is_authenticated and (user.is_doctor()))

# class IsEditor(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         return bool(user and user.is_authenticated and (user.is_editor()))

# class IsPatient(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         return bool(user and user.is_authenticated and (user.is_patient()))

# class IsOwnerOrEditor(BasePermission):
#     """
#     اجازه می‌دهد خودِ صاحب یک رکورد یا Editor (که حق ویرایش رکوردهای خودش را دارد) عمل کند.
#     برای استفاده در viewsetها: اگر obj.user == request.user -> اجازه، یا اگر کاربر Editor و obj.created_by==request.user
#     """
#     def has_object_permission(self, request, view, obj):
#         if not request.user or not request.user.is_authenticated:
#             return False
#         # کاربر صاحب شیء است
#         if getattr(obj, "created_by", None) == request.user:
#             return True
#         # یا Editor و سوپروزر نیست
#         if request.user.is_editor():
#             # Editor فقط روی اشیاء خودش باید اجازه داشته باشد — این چک بالا این را پوشش می‌دهد.
#             return False
#         # سوپروزر اجازه
#         if request.user.is_superuser:
#             return True
#         return False
