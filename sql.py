from mysql.connector import connect, Error, cursor


try:
    with connect(
        host="localhost",
        user="root",
        password="root"
    )as connection:
        create_database = "CREATE DATABASE users"
        with connection.cursor() as cursor:
            connect().cursor().execute(create_database)
        print(connection)
except Error as e:
    print(e)


# try:
#     connection = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='root',
#         database='telegram',
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     try:
#         pass
#         # with connection.cursor() as cursor:
#         #     print("Table is deleted!")
#         # with connection.cursor() as cursor:
#         #     create_table_query = "CREATE TABLE IF NOT EXISTS `users`(id int AUTO_INCREMENT," \
#         #                          "name varchar(32), " \
#         #                          "password varchar(32)," \
#         #                          "email varchar(32), " \
#         #                          "PRIMARY KEY(id));"
#         #     cursor.execute(create_table_query)
#         #     print("Table created.")
#         #print("Created")
#         # with connection.cursor() as cursor:
#         #     insert_query = "INSERT INTO `users` (name, password, email) " \
#         #                    "VALUES ('Дмитрий', 'qwerty', 'dmitrii.kolesnikov02@mail.ru')"
#         #     cursor.execute(insert_query)
#         #     connection.commit()
#     finally:
#         connection.close()
#         # cursor.close()
# except Exception as ex:
#     print("Connection refused...")
#     print(ex)
# #
# # logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
# #                     level=logging.INFO)
