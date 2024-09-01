from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
# A functional based view
# A ‘Librarian’ view accessible only to users identified as ‘Librarians’. The file should be named
def admin_view(request):
    if request.user.is_authenticated:
        return render(request,'admin.html')
    return render(request,'access_denied.html')
