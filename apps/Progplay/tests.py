from django.test import TestCase
import unittest
from django.shortcuts import render,redirect
from apps.Progplay.models import Usuarios,Pais,Post
from apps.Progplay.views import detallePost
# Create your tests here.

class TestdetallePost(unittest.TestCase):
    def test_detallePost(self):
      
    self.assertEqual(mymodule.detallePost(True))