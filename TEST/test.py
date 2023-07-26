import unittest
import requests

class TestContactsAPI(unittest.TestCase):

    def setUp(self):
        # Configurar a URL base da API
        self.base_url = "http://localhost:5000"
        # Dados do contato de exemplo para testes
        self.data = {
            "nome": "João",
            "sobrenome": "Silva",
            "email": "joao@example.com",
            "telefone": "(11) 98765-4321"
        }

    def test_create_contact(self):
        # Testar a criação de um novo contato
        # Remova o campo "id" dos dados do contato antes de enviar a requisição
        self.data.pop("id", None)
        response = requests.post(f"{self.base_url}/contatos", json=self.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())


    def test_read_contact(self):
        # Testar a leitura de um contato pelo ID
        response = requests.get(f"{self.base_url}/contatos/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["nome"], "João da Silva")

    def test_update_contact(self):
        # Testar a atualização de um contato pelo ID
        data = {
            "nome": "João da Silva",
            "email": "joao.silva@example.com"
        }
        response = requests.put(f"{self.base_url}/contatos/1", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Contato atualizado com sucesso")

    def test_delete_contact(self):
        # Testar a exclusão de um contato pelo ID
        response = requests.delete(f"{self.base_url}/contatos/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Contato excluído com sucesso")

    def test_search_contact(self):
        # Testar a pesquisa de contatos por parte do nome
        search_name = "Jo"
        response = requests.get(f"{self.base_url}/contatos/search?nome={search_name}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertTrue(len(response.json()) > 0)

class OrderedTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        ordered_test_names = [
            "test_create_contact",
            "test_read_contact",
            "test_update_contact",
            "test_search_contact",
            "test_delete_contact",
        ]
        return sorted(test_names, key=lambda x: ordered_test_names.index(x))

if __name__ == '__main__':
    unittest.main(testLoader=OrderedTestLoader())
