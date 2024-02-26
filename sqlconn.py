import pypyodbc as podbc

class sql:
    def __init__(self, connectionstring):
        self.connectionstring = connectionstring

    def insert(self, query):
        conn = podbc.connect(self.connectionstring) 
        db_cursor = conn.cursor()
        try:
            db_cursor.execute(query)
        finally:
            db_cursor.close()
            conn.commit()
            conn.close()  
        
    def insert(self, inputparams, valueparams):
        conn = podbc.connect(self.connectionstring) 
        db_cursor = conn.cursor()
        try:
            sql = "EXEC " + inputparams
            db_cursor.execute(sql, valueparams)
        finally:
            db_cursor.close()
            conn.commit()
            conn.close()  

    def get(self, query): 
        conn = podbc.connect(self.connectionstring) 
        db_cursor = conn.cursor() 
        results = []
        try:          
            db_cursor.execute(query)
            for row in db_cursor:
                results.append(row)
            conn.commit()
        finally:
            db_cursor.close()
            conn.close()
        return results

    def delete(self, query): 
        conn = podbc.connect(self.connectionstring) 
        db_cursor = conn.cursor() 
        try:     
            db_cursor.execute(query)
            conn.commit()
        finally:
            db_cursor.close()
            conn.close()

    def execute(self, query, valueparams): 
        conn = podbc.connect(self.connectionstring) 
        db_cursor = conn.cursor() 
        results = []
        try:          
            db_cursor.execute(query, valueparams)
            for row in db_cursor:
                results.append(row)
            conn.commit()
        finally:
            db_cursor.close()
            conn.close()
        return results