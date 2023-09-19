from DAO.PCListDAO import PCList

class Slave:
    def setSlaveName(self, DB):
        try:
            #slave이름 설정
            slave_name = "com1"

            #DB를 이용해 Slave이름 유효성 검사
            PCList_DAO = PCList()
            result = PCList_DAO.SelectPCList(DB, slave_name)

            if result is None:
                raise Exception("Unregistered Slave Name.")

            self.name = result[1]

        except Exception as e:
            raise e