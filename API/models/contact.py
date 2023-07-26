from database.database import connect_db

class Contact:

    def __init__(self, id=None, nome=None, sobrenome=None, email=None, telefone=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

    def save(self):
        conn = connect_db()
        cursor = conn.cursor()

        if self.id is None:
            query = "INSERT INTO contato (nome, sobrenome, email, telefone) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.nome, self.sobrenome, self.email, self.telefone))
            self.id = cursor.lastrowid  # Atualiza o ID com o valor gerado pelo banco
        else:
            query = "UPDATE contato SET nome = %s, sobrenome = %s, email = %s, telefone = %s WHERE id = %s"
            cursor.execute(query, (self.nome, self.sobrenome, self.email, self.telefone, self.id))

        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = connect_db()
        cursor = conn.cursor()
        query = "DELETE FROM contato WHERE id = %s"
        cursor.execute(query, (self.id,))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def get_by_id(cls, id):
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM contato WHERE id = %s"
        cursor.execute(query, (id,))
        contato = cursor.fetchone()
        cursor.close()
        conn.close()

        if contato:
            return cls(*contato)
        else:
            return None

    @classmethod
    def search_by_name(cls, name):
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM contato WHERE nome LIKE %s"
        cursor.execute(query, ('%' + name + '%',))
        contatos = cursor.fetchall()
        cursor.close()
        conn.close()

        return [cls(*contato) for contato in contatos]
