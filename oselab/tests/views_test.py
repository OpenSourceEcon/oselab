from oselab import app
import unittest

class OSELabTestCase(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()

  def test_home_view(self):
    request = self.app.get('/')
    self.assertEqual(request.status_code, 200)

  def test_gallery_view(self):
    request = self.app.get('/gallery')
    self.assertEqual(request.status_code, 200)

  def test_marginal_effective_corporate_taxes_view(self):
    request = self.app.get('/gallery/marginal_effective_corporate_taxes')
    self.assertEqual(request.status_code, 200)

  def test_overlapping_generations_view(self):
    request = self.app.get('/gallery/overlapping_generations')
    self.assertEqual(request.status_code, 200)

  def test_tax_increase_decrease_view(self):
    request = self.app.get('/gallery/tax_increase_decrease')
    self.assertEqual(request.status_code, 200)

def run_tests():
  unittest.main()

if __name__ == '__main__':
  run_tests()
