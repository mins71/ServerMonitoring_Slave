class PCList:
    def SelectPCList(self, DB, slave_name):
        try:
            #cursor 만들기
            cursor = DB.connection.cursor()

            #PCname으로 select
            sql = "SELECT * FROM pclist WHERE pcname=%s"
            cursor.execute(sql,(slave_name,))
            result = cursor.fetchone()

            #결과값 return
            return result

        except:
            raise Exception("PC List Select Error.")