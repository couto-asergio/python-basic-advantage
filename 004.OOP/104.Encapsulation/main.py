from encapsulation import DataBase

db = DataBase()
db.add_client(1, 'Otávio')
db.add_client(2, 'Miranda')
db.add_client(1, 'Rose')

db.list_client()

# With the below instruction the entire class will be boken
db.data = 'Another thing'
