# """
# Test for patient api
# """
# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse

# from rest_framework import status
# from rest_framework.test import APIClient

# from core.models import Patient

# PATIENT_URL = reverse('patient:patient-det')


# def create_patient(**params):
#     """create and return a sample patient"""
#     defaults = {
#         'patient_name': 'abcd',
#         'phone_no': 1234567890,
#         'address': 'abc',
#         'landmark': 'asdf',
#         'country': 'zxcvb',
#         'city': 'mno',
#         'state': 'mnop',
#         'pincode': 12345,
#     }
#     defaults.update(params)

#     patient = Patient.objects.create(**defaults)
#     return patient


# class PublicTestPatientApi(TestCase):
#     """Test the public feature for patient api"""

#     def set_up(self):
#         self.client = APIClient()

#     def test_patient_for_success(self):
#         """successfully created """
#         payload = {
#             'patient_name': 'abcd',
#             'phone_no': 1234567890,
#             'address': 'abc',
#             'landmark': 'asdf',
#             'country': 'zxcvb',
#             'city': 'mno',
#             'state': 'mnop',
#             'pincode': 12345,
#         }
#         res = self.client.poast(PATIENT_URL, payload)
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)

#     def test_for_similar_phone_no_exists(self):
#         """Test if similar phone exists return error"""
#         payload = {
#             'patient_name': 'abcd',
#             'phone_no': 1234567890,
#             'address': 'abc',
#             'landmark': 'asdf',
#             'country': 'zxcvb',
#             'city': 'mno',
#             'state': 'mnop',
#             'pincode': 12345,
#         }
#         create_patient(**payload)
#         res = self.client.post(PATIENT_URL, payload)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    

