import psutil
from time import time
from DAO.NetworkDAO import NetworkDAO
class NetworkCollector:

    def __init__(self):
        self.hwDAO = NetworkDAO()

    def getNetworkBytes(self):
        return time(), psutil.net_io_counters(pernic=True)

    def pushNetworkBytes(self, *args):
        timedata, bytes_datas = self.getNetworkBytes()
        for interface, data in bytes_datas.items():
            self.hwDAO.insertBytesInfo(args[0][0], args[0][1], timedata, interface, data.bytes_sent, data.bytes_recv, data.packets_sent, data.packets_recv)