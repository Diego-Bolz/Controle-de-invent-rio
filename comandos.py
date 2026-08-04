import sqlite3 
class inventario(object):
    def __init__(self):
        self.arquivo = None
        self.conn = None
        self.cursor = None
        self.info = []

    def criar_inventario(self,nome):
        self.conn = sqlite3.connect(nome + '.db')
        sql = f'''CREATE TABLE {nome}('Código do Produto' text, 'Descrição do produto' text, 'Categoria' text, 'Quantidade em Estoque' text, 'Localização' text, 'Data de Entrada' text, 'Valor Unitário' text, 'Valor Total' text, 'Observações' text)'''
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()

    def acessar_inventario(self,nome):
        self.conn = sqlite3.connect(nome + '.db')
        self.ursor = self.conn.cursor()

    def adicionar_inventario(self,valores,nome):
        self.info.append(valores)
        sql = f"""INSERT INTO {nome} VALUES('{valores[0]}', '{valores[1]}', '{valores[2]}', '{valores[3]}', '{valores[4]}', '{valores[5]}', '{valores[6]}', '{valores[7]}', '{valores[8]}')"""
        self.cursor.execute(sql)
        self.conn.commit()

    def visualizar_inventario(self, nome):
        sql = f"""SELECT rowid, * FROM {nome} ORDER BY Código do Produto"""
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)