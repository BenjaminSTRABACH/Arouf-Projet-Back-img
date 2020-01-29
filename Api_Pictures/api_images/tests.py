from django.urls import reverse

import django

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class ImgTest(APITestCase):

    django.setup()
    client = APIClient()

    def test_sendPicture(self):
        response = self.client.post(reverse('api_img:sendPicture'), data={'file': open('test_file.png', 'rb')}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.content.decode("utf-8") , 'True')


    def test_getAllPictures(self):
        response = self.client.get(reverse('api_img:getAllPictures'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
