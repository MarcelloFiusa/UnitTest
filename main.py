from scr.models.store import Store
from scr.models.user import User
from scr.service.service_user import ServiceUser

# user_1 = User("Marcello", "Analista")
# user_2 = User("Cynthia", "Professor")
#
# store = Store()
# store.bd.append(user_1)
# store.bd.append(user_2)

service = ServiceUser()
resultado = service.add_user("Marcello", "Tester")
resultado = service.add_user(10, "Analista")
resultado = service.add_user("Marcello", "Tester")
resultado = service.add_user("Karlos", "Tester")

resultado = service.remove_user("Marcello", "Tester")
resultado = service.remove_user("passaro", "Tester")

resultado = service.get_user_by_name("Karlos")

resultado = service.update_user("Karlos", "Developer")
