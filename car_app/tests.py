from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Car

class CarModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')

        test_user.save()

        test_Car =Car.objects.create(
            user = test_user,

            name_of_car = 'Name of Car',

            body = 'The Cars world'
        )
        test_Car.save()


    def test_car_content(self):

        car =Car.objects.get(id=1)

        self.assertEqual(str(car.user), 'tester')

        
        self.assertEqual(car.name_of_car, 'Name of Car')
        
        self.assertEqual(car.body, 'The Cars world')


class APITest(APITestCase):
   
    # def test_cars_list(self):
   
    #     response = self.client.get(reverse('cars_list'))
   
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cars_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
       
        test_user.save()

        test_Car =Car.objects.create(
       
            user = test_user,
       
            name_of_car = 'Name of Car',
       
            body = 'The Cars world'
        )
        test_Car.save()

        response = self.client.get(reverse('cars_detail', args=[1]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, 'id')

        self.assertAlmostEqual(response.data['id'],1)


    def test_cars_create(self):
       
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
       
        test_user.save()

        url = reverse('cars_list')

        data = {
       
            "name_of_car":'Name of Car',
       
            "body": 'The Cars world' ,
       
            "user":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Car.objects.count(), 1)

        self.assertEqual(Car.objects.get().name_of_car, data['name_of_car'])

    def test_cars_update(self):
      
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
      
        test_user.save()

        test_Car =Car.objects.create(
      
            user = test_user,

            name_of_car = 'Name of Car' , 

            body =  'The Cars world'
        )

        test_Car.save()

        url = reverse('cars_detail',args=[test_Car.id])

        data = {

            "name_of_car": 'Name of Car' ,

            "user":test_Car.user.id,

            "body":test_Car.body,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Car.objects.count(), test_Car.id)

        self.assertEqual(Car.objects.get().name_of_car, data['name_of_car'])



    def test_cars_delete(self):
 
  
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
 

 
        test_user.save()

 
        car =Car.objects.create(


            user = test_user,


            name_of_car = 'Name of Car',


            body =  'The Cars world'

        )

        car.save()

        car1 =Car.objects.get()

        url = reverse('cars_detail', kwargs={'pk':car1.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)