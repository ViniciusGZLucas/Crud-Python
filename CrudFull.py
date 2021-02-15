import mysql.connector
import mysql

#Informações utilizadas para fazer login no banco de dados
Host = "localhost"
DataBase = "crud"
Port = 3306
User = "root"
Password = ""

#Funções que iram fazer alterações ou consultas no banco de dados
def exibirconsole(txt):
    print(txt)

def consultar(cmd):
    cursor.execute(cmd)
    result = cursor.fetchall()
    print(result)

def editar(cmd):
    return cursor.execute(cmd)

#Conectar no xampp para mecher no banco de dados ou criar
conn = mysql.connector.connect(database=DataBase, host=Host, port=Port, user=User, password=Password)
cursor = conn.cursor()

#Criar banco de dados
try:
    cursor.execute('create database Crud')
except mysql.connector.errors.DatabaseError:
    print("Banco de Dados já existente")

#Criar Tabelas
try:
    cursor.execute("create table Usuarios(Cpf char(10) primary key,Nome varchar(30),Idade varchar(3),Email varchar(50));")
except mysql.connector.errors.DatabaseError:
    print("Tabela Já existente")

#Inserir informações na tabela
try:
    cursor.execute("insert into Usuarios(Cpf,Nome,Idade,Email) values('61286928184','Sebastião César Jesus','20','ssebastiaocesarjesus@liv.com');")
    cursor.execute("insert into Usuarios(Cpf,Nome,Idade,Email) values('59986785324','Catarina Benedita Souza','27','atarinabeneditasouza__catarinabeneditasouza@realbit.com.br');")
    cursor.execute("insert into Usuarios(Cpf,Nome,Idade,Email) values('28234252763','Murilo Jorge Filipe Jesus','30','murilojorgefilipejesus__murilojorgefilipejesus@atualvendas.com');")
    conn.commit()
except mysql.connector.errors.DatabaseError:
    print("Essas informações ja foram inseridas")

consultar(cmd='Select * from Usuarios')
consultar(cmd="select Nome from usuarios")
consultar(cmd="select Cpf from usuarios where Nome='Catarina Benedita Souza'")