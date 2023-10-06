import schedule
import time
from UI.UI import UI
from Collector.HardwareCollector import HardwareCollector
from Collector.NetworkCollector import NetworkCollector
from Scheduler.Scheduler import Schedular


class Main:

    def run(self):
        #UI생성
        ui = UI()

        #프로그램 실행을 위한 UI실행
        self.DB, self.slave = ui.StartDaemon()

        #스케줄러 및 Collector 생성
        schedular = Schedular()
        HWcollector = HardwareCollector()
        NWcollector = NetworkCollector()

        #하드웨어 관련 정보 수집 스케줄러 설정
        schedular.SetEvery5Sec(HWcollector.pushCPUInfo, self.DB, self.slave.name) #CPU사용량 수집 스케줄러 설정
        schedular.SetEvery5Sec(HWcollector.pushMemInfo, self.DB, self.slave.name) #메모리사용량 수집 스케줄러 설정
        schedular.SetEvery5Sec(HWcollector.pushDiskInfo, self.DB, self.slave.name) #디스크사용량 수집 스케줄러 설정

        #네트워크 관련 정보 수집 스케줄러 설정
        schedular.SetEvery5Sec(NWcollector.pushNetworkBytes, self.DB, self.slave.name) #네트워크사용량 수집 스케줄러 설정
        schedular.SetEvery5Sec(NWcollector.pushNetworConnections, self.DB, self.slave.name)#세션수립상태 수집 스케줄러 설정

        # 시스템 에러정보 수집

        # 시스템 로그정보 수집

        #스케쥴시작
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    main = Main()
    main.run()