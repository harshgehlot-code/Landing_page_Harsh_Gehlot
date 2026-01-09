from django.shortcuts import render


def landing_page(request):
    """Serve the landing page"""
    return render(request, 'index.html')

