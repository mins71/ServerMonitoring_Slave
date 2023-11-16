class WarningDAO:
    def insertWarning(self, DB, slave_name, timedata, type, messeage):
        try:
            # cursor 만들기
            cursor = DB.connection.cursor()

            # sql문 작성 및 실행
            sql = f"INSERT INTO warning VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (timedata, slave_name, type, messeage))

            # 트렉젝션 commit
            DB.connection.commit()

        except:
            raise Exception("Insert Warning Error.")