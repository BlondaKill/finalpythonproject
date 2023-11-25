from django.test import TestCase

# Create your tests here.


class ArticuloTests(TestCase):
    """En esta clase van todas las pruebas del modelo Articulo."""

    def test_articulo_create(self):
        # caso uso esperado
        articulo = articulo(titulo="Titulo", subtitulo="subtitulo")
        articulo.save()

        # Compruebo que el articulo fue creado y la info fue guardada bien
        self.assertEqual(articulo.objects.count(), 1)
        self.assertEqual(articulo.nombre, "Titulo")
        self.assertEqual(articulo.subtitulo, "subtitulo")

    def test_articulo_str(self):
        articulo = articulo(nombre="Python", subtitulo="Django")
        articulo.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(articulo.__str__(), "Python (Django)")