import odoolib

connection = odoolib.get_connection(hostname="localhost", database="my_db", login="my_user", password="xxx")
user_model = connection.get_model("academy.course")
ids = user_model.search([])
user_info = user_model.read(ids[0], ["name"])
print(user_info["name"])