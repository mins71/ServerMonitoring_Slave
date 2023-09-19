import psutil
from time import time
from DAO.HardwareDAO import HardwareDAO

class HardwareCollector:

    def __init__(self):
        self.hwDAO = HardwareDAO()

    def getCPUInfo(self):
        timedata = time()
        cpu_percent = psutil.cpu_percent(interval=1)
        return timedata, cpu_percent

    def getMemInfo(self):
        timedata = time()
        memory = psutil.virtual_memory()
        TotalMemory = memory.total
        UsedMemory = memory.used
        FreeMemory = memory.free
        MemoryPercent = int((UsedMemory / TotalMemory) * 100)
        return timedata, TotalMemory, UsedMemory, FreeMemory, MemoryPercent

    def getDiskInfo(self):
        timedata = time()
        disk_usage = psutil.disk_usage('/')
        TotalSpace = disk_usage.total
        UsedSpace = disk_usage.used
        FreeSpace = disk_usage.free
        UsagePercentage = disk_usage.percent
        return timedata, TotalSpace, UsedSpace, FreeSpace, UsagePercentage

    def pushCPUInfo(self, *args):
        timedata, cpu_percent = self.getCPUInfo()
        self.hwDAO.insertCPUInfo(args[0][0], args[0][1], timedata, cpu_percent)

    def pushMemInfo(self, *args):
        timedata, total_memory, used_memory, free_memory, memory_percent = self.getMemInfo()
        self.hwDAO.insertMemInfo(args[0][0], args[0][1], timedata, total_memory, used_memory, free_memory, memory_percent)

    def pushDiskInfo(self, *args):
        timedata, total_space, used_space, free_space, used_percentage = self.getDiskInfo()
        self.hwDAO.insertDiskInfo(args[0][0], args[0][1], timedata, total_space, used_space, free_space, used_percentage)