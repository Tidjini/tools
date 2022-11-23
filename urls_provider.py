from importlib import import_module
from django.urls import include, path

# set your list provider
# here is an example
# as conventions all our urlspatterns are collected in urls.py in each application
sample_provider_list = []

urlpatterns = [path("", include("applications.sample_app.urls"))]

# collect urlpattern for other applications
applications_urlpatterns = []

for provider in sample_provider_list:
    try:
        _module = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue

    # get urlpatterns from each module, if exist
    if "urlpatterns" in _module:
        applications_urlpatterns += _module["urlpatterns"]

# add other applications urlpatterns to this main one
urlpatterns += applications_urlpatterns
