class HardwareDAO:
    def insertCPUInfo(self, DB, slave_name, timedata, cpu_percent):
        try:
            # cursor 만들기
            cursor = DB.connection.cursor()

            #sql문 작성 및 실행
            sql = f"INSERT INTO {slave_name}_cpu VALUES (%s, %s)"
            cursor.execute(sql, (timedata, cpu_percent))

            #트렉젝션 commit
            DB.connection.commit()

        except:
            raise Exception("Insert CPU Infomation Error.")

    def insertMemInfo(self, DB, slave_name, timedata, total_memory, used_memory, free_memory, memory_percent):
        try:
            # cursor 만들기
            cursor = DB.connection.cursor()

            # sql문 작성 및 실행
            sql = f"INSERT INTO {slave_name}_mem VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (timedata, total_memory, used_memory, free_memory, memory_percent))

            # 트렉젝션 commit
            DB.connection.commit()

        except:
            raise Exception("Insert Memory Infomation Error.")

    def insertDiskInfo(self, DB, slave_name, timedata, total_space, used_space, free_space, used_percentage):
        try:
            # cursor 만들기
            cursor = DB.connection.cursor()

            # sql문 작성 및 실행
            sql = f"INSERT INTO {slave_name}_disk VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (timedata, total_space, used_space, free_space, used_percentage))

            # 트렉젝션 commit
            DB.connection.commit()
        except:
            raise  Exception("Insert Disk Information Error")