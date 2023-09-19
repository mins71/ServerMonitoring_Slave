from DAO.DBconn import DBConn
from Function.Slave import Slave

class UI:
    def StartDaemon(self):
        try:
            # 시작문구출력
            print("Start Monitoring Daemon.")

            #서버 연결
            DB = DBConn()
            DB.getConn()

            #slave이름 설정
            slave = Slave()
            slave.setSlaveName(DB)

            #준비완료 문구 출력 및 DB, slave 객체 반환
            print("Daemon is ready to run.")
            return DB, slave

        except Exception as e:
            #오류알림
            print("Daemon Start Failed.")
            print(f'Error : {e}')
            print("Exit the Program.")

            #오류처리 및 프로그램종료
            DB.closeConn()
            exit(-1)