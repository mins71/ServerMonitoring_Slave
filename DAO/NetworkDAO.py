class NetworkDAO:

    def insertBytesInfo(self, DB, slave_name, timedata, interface, bytes_sent, bytes_recv, packet_sent, packet_recv):
        try:
            # cursor 만들기
            cursor = DB.connection.cursor()

            #sql문 작성 및 실행
            sql = f"INSERT INTO {slave_name}_network_bytes VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (timedata, interface, bytes_sent, bytes_recv, packet_sent, packet_recv))

            #트렉젝션 commit
            DB.connection.commit()

        except:
            raise Exception("Insert Network_Byte Infomation Error.")