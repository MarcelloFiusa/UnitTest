from scr.models.store import Store
from scr.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        user = User(name, job)
        if type(name) != str or type(job) != str:
            return "Entradas devem ser strings"
        if any(u.name == user.name for u in self.store.bd):
            return "Usuário duplicado"
        else:
            self.store.bd.append(user)
            return "Usuário adicionado"

    def remove_user(self, name, job):
        user = User(name, job)
        if type(name) != str or type(job) != str:
            return "Entradas devem ser strings"
        if any(u.name == user.name for u in self.store.bd):
            self.store.bd.pop()
            return "Usuário Removido"
        else:
            return "Usuário não está na lista"

    def get_user_by_name(self, name):
        if type(name) != str:
            return "Entradas devem ser strings"
        for search in self.store.bd:
            if name == search.name:
                return search.job
            else:
                return "Usuário não encontrado"

    def update_user(self, name, newjob):
        if type(name) != str or type(newjob) != str:
            return "Entradas devem ser strings"
        for search in self.store.bd:
            if name == search.name:
                search.job = newjob
                return "Job atualizado"
            else:
                return "Usuário não cadastrado"

