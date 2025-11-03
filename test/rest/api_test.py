import http.client
import os
import unittest
import json
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # Verifica que la API responde correctamente con la suma de dos números.
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        data = response.read().decode()
        self.assertEqual(data, "4")
    
    # Verifica que la API devuelve un error 400 
    # si uno de los parametros es texto no numérico.
    def test_api_add_invalid_string(self):
        url = f"{BASE_URL}/calc/add/hola/5"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )
        
    # Verifica que la API devuelve un error 404 
    # si falta uno de los parámetros en la url.
    def test_api_add_missing_parameter(self):
        url = f"{BASE_URL}/calc/add/10"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        self.assertEqual(
            cm.exception.code, 
            http.client.NOT_FOUND,
            "La API no devolvió 404 Not Found ante una URL incompleta."
        )

    # Verifica que la API responde correctamente con la resta de dos números.
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        data = response.read().decode()
        self.assertEqual(data, "3")

    # Verifica que la API devuelve un error 400 
    # si uno de los parametros es texto no numérico.
    def test_api_substract_invalid_string(self):
        url = f"{BASE_URL}/calc/substract/hola/5"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )

    # Verifica que la API devuelve un error 404 
    # si falta uno de los parámetros en la url.
    def test_api_substract_missing_parameter(self):
        url = f"{BASE_URL}/calc/substract/10"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        self.assertEqual(
            cm.exception.code, 
            http.client.NOT_FOUND,
            "La API no devolvió 404 Not Found ante una URL incompleta."
        )
    
    # Verifica que la API responde correctamente con la multiplicación de dos números.
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
 
    # Verifica que la API devuelve un error 400 
    # si uno de los parametros es texto no numérico.
    def test_api_multiply_invalid_string(self):
        url = f"{BASE_URL}/calc/multiply/hola/5"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )

    # Verifica que la API devuelve un error 404 
    # si falta uno de los parámetros en la url.
    def test_api_multiply_missing_parameter(self):
        url = f"{BASE_URL}/calc/multiply/10"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        self.assertEqual(
            cm.exception.code, 
            http.client.NOT_FOUND,
            "La API no devolvió 404 Not Found ante una URL incompleta."
        )
    
    # Verifica que la API responde correctamente con la división de dos números.
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/6/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        data = response.read().decode()
        self.assertEqual(data, "2.0")
    
     
    # Verifica que la API devuelve un error 400 
    # si se intenta dividir por cero.
    def test_api_divide_with_zero(self):
        url = f"{BASE_URL}/calc/divide/5/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )


    # Verifica que la API devuelve un error 400 
    # si uno de los operandos es texto no numérico.
    def test_api_divide_invalid_string(self):
        url = f"{BASE_URL}/calc/divide/hola/5"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )

    # Verifica que la API devuelve un error 404 
    # si falta uno de los parámetros en la url.
    def test_api_divide_missing_parameter(self):
        url = f"{BASE_URL}/calc/divide/10"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        self.assertEqual(
            cm.exception.code, 
            http.client.NOT_FOUND,
            "La API no devolvió 404 Not Found ante una URL incompleta."
        )

    # Verifica que la API responde correctamente con la potencia elevada al número indicado.
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/3/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        data = response.read().decode()
        self.assertEqual(data, "9")

    # Verifica que la API responde correctamente 
    # con la potencia base 0
    def test_api_power_with_base_zero(self):
        url = f"{BASE_URL}/calc/power/0/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        data = response.read().decode()
        self.assertEqual(data, "0")

    # Verifica que la API devuelve un error 400 
    # si uno de los operandos es texto no numérico.
    def test_api_power_invalid_string(self):
        url = f"{BASE_URL}/calc/power/hola/5"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )

    # Verifica que la API devuelve un error 404 
    # si falta uno de los parámetros en la url.
    def test_api_power_missing_parameter(self):
        url = f"{BASE_URL}/calc/power/10"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        self.assertEqual(
            cm.exception.code, 
            http.client.NOT_FOUND,
            "La API no devolvió 404 Not Found ante una URL incompleta."
        )

    # Verifica que la API responde correctamente con la raíz cuadrada del número indicado.
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        data = response.read().decode()
        self.assertEqual(data, "4.0")

    # Verifica que la API devuelve un error 400 
    # si uno de los operandos es texto no numérico.
    def test_api_sqrt_invalid_string(self):
        url = f"{BASE_URL}/calc/sqrt/hola"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )

    # Verifica que la API devuelve un error 404 
    # si falta uno de los parámetros en la url.
    def test_api_sqrt_missing_parameter(self):
        url = f"{BASE_URL}/calc/sqrt/"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        self.assertEqual(
            cm.exception.code, 
            http.client.NOT_FOUND,
            "La API no devolvió 404 Not Found ante una URL incompleta."
        )

    # Verifica que la API responde correctamente con el logaritmo del número indicado.
    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    # Verifica que la API devuelve un error 400 
    # si uno de los operandos es texto no numérico.
    def test_api_log10_invalid_string(self):
        url = f"{BASE_URL}/calc/log10/hola"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            cm.exception.code, 
            http.client.BAD_REQUEST,
            "La API no devolvió 400 Bad Request ante un string inválido."
        )

    # Verifica que la API devuelve un error 404 
    # si falta uno de los parámetros en la url.
    def test_api_log10_missing_parameter(self):
        url = f"{BASE_URL}/calc/log10/"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            
        self.assertEqual(
            cm.exception.code, 
            http.client.NOT_FOUND,
            "La API no devolvió 404 Not Found ante una URL incompleta."
        )
