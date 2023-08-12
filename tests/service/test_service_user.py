from scr.service.service_user import ServiceUser
from unittest import TestCase


class TestServiceUser(TestCase):

    def test_add_user_com_sucesso(self):
        service = ServiceUser()
        us1 = service.add_user("Grupo5", "Testadores")
        self.assertEqual(us1, "Usuário adicionado")

    def test_add_user_com_falha(self):
        service = ServiceUser()
        us1 = service.add_user(10, "Analista")
        self.assertEqual(us1, "Entradas devem ser strings")

    def test_add_user_com_duplicado(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        usr2 = service.add_user("Grupo5", "Testadores")
        self.assertEqual(usr2, "Usuário duplicado")

    def test_remover_usuario_com_sucesso(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        userRemove = service.remove_user("Grupo5", "Testadores")
        expected_result = "Usuário Removido"
        self.assertEqual(userRemove, expected_result)

    def test_remover_usuario_sem_sucesso(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        userRemove = service.remove_user("Passaro", "Animal")
        expected_result = "Usuário não está na lista"
        self.assertEqual(userRemove, expected_result)

    def test_get_user_com_sucesso(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        userJob = service.get_user_by_name("Grupo5")
        expected_result = "Testadores"
        self.assertEqual(userJob, expected_result)

    def test_get_user_sem_sucesso(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        userJob = service.get_user_by_name("João")
        expected_result = "Usuário não encontrado"
        self.assertEqual(userJob, expected_result)

    def test_update_user_com_sucesso(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        userUp = service.update_user("Grupo5", "Desenvolvedores")
        expected_result = "Job atualizado"
        self.assertEqual(userUp, expected_result)

    def test_update_user_sem_sucesso(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        userUp = service.update_user("João", "Developer")
        expected_result = "Usuário não cadastrado"
        self.assertEqual(userUp, expected_result)



