from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")  # Забираем значение типа str
# ADMINS = {784007452, 374927548, 484085985}
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
#IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
USER = env.str("USER")
PASS = env.str("PASS")
host = env.str("host")
db_name = env.str("db")
