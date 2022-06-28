"""WXProgram URL Configuration
first-level interface(apps): amniocentesisAppoint, multidisciplinaryConsultation, addPatient
"""


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("amniocentesisAppoint/", include(("amniocentesisAppoint.urls", "amniocentesisAppoint"),
    #                                       namespace="amniocentesisAppoint")),
    # path("multidisciplinaryConsultation/", include(("multidisciplinaryConsultation.urls",
    #                                                 "multidisciplinaryConsultation"),
    #                                                namespace="multidisciplinaryConsultation")),
    # path("addPatient/", include(("addPatient.urls", "addPatient"), namespace="addPatient")),
    path("MedicalCareServerApp/", include(("MedicalCareServerApp.urls", "MedicalCareServerApp"), namespace="MedicalCareServerApp")),
]
