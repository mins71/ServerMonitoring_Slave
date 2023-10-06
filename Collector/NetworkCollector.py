import psutil
from time import time
from DAO.NetworkDAO import NetworkDAO
class NetworkCollector:

    def __init__(self):
        self.hwDAO = NetworkDAO()

    def getNetworkBytes(self):
        return time(), psutil.net_io_counters(pernic=True)

    def getNetworkConnections(self):
        # 현재 열린 소켓의 연결 정보 가져오기
        return time(), psutil.net_connections(kind='inet')

    def pushNetworkBytes(self, *args):
        timedata, bytes_datas = self.getNetworkBytes()
        for interface, data in bytes_datas.items():
            self.hwDAO.insertBytesInfo(args[0][0], args[0][1], timedata, interface, data.bytes_sent, data.bytes_recv, data.packets_sent, data.packets_recv)

    def pushNetworConnections(self, *args):
        timedata, connections = self.getNetworkConnections()

        for conn in connections:
            if len(conn.laddr) == 0:
                local_ip = ''
                local_port = ''
            else:
                local_ip = conn.laddr.ip
                local_port = conn.laddr.ip

            if len(conn.raddr) == 0:
                remote_ip = ''
                remote_port = ''
            else:
                remote_ip = conn.raddr.ip
                remote_port = conn.raddr.port

            self.hwDAO.insertConnectionInfo(args[0][0], args[0][1], timedata, local_ip, local_port, remote_ip, remote_port, conn.status)