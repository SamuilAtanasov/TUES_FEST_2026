from django.http import HttpResponseForbidden

class StaffOnlyAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/guitar_hub_superpanel/'):
            if not request.user.is_authenticated or not request.user.is_staff:
                return HttpResponseForbidden("Access denied")
        return self.get_response(request)