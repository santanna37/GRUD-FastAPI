# estudo 

# getatt 
""" é uma função que permite fazer busca 
 alterar objetos de classe, e se o valor 
 não existir ele cria esse valor na classe  """

# 

class Person:
    age = 38
    name = "luiz"
    location = "brasil"

obj = Person()

print(getattr(obj, 'age'))
print(getattr(obj,'altura', 180))

print("===")


# setattr 
""" ele busca o atrubuto no objeto, e altera o valor
ele não retorna nd
se o atributo não existir ele cria 
"""

setattr(obj, 'salario', 20000)

setattr(obj, 'age', 40)

print(getattr(obj, 'salario'))
print(getattr(obj, 'age'))

print(getattr(obj, 'lazer', 'bola'))



# hasattr 
""" ele busca o atributo na classe e retorna TRUE e FALSE 
 pode ser usado em if para buscas e alterações  
"""

print(hasattr(obj, 'age'))
print(hasattr(obj, 'casa'))


# delattr
""" usado para deletar o atribudo da classe 
deve clamar a classe e o atributo que deseja deletar
"""

print(hasattr(obj, 'age'))

delattr(Person, 'age')

print(hasattr(obj, 'age'))


# teste de handelers 

class Person2:
    def __init__(self, name: str, age: int, location: str):
        self.name = name
        self.age = age
        self.location = location

# Simulando um "banco de dados" com objetos da classe Person
database = [
    Person2("luiz", 38, "brasil"),
    Person2("ana", 30, "portugal"),
    Person2("maria", 25, "brasil"),
]


def get(obj: dict):

    filters = {"name", "age"}

    print('Iniciando buscas..')
    lista = []

    print(f'person2 = {Person2.__init__.__annotations__.keys()}')

    entity_class = Person2.__init__.__annotations__.keys()

    for field, value in obj.items():
        print(f"[DEBUG] Campo recebido: {field} = {value}")
        # Ex: field = "email", value = "luiz@gmail.com"
        
        if field in filters and hasattr(Person2, field):
            print(f'achei{field}')
        #     # column_attr = getattr(self.entity_class, field)  # self.entity_class.email
        #     query = query.filter(column_attr == value)
        #     print(f"[DEBUG] Aplicado filtro: {field} == {value}")

        # results = query.all()
        # print(f"[DEBUG] Resultado bruto do banco: {results}")

        # return [self.mapper.to_domain(entity) for entity in results]


lista = {'name':'luiz', 'location':'brasil'}

print(get(obj=lista))