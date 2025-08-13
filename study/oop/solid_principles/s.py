# Single responsibility principle
# A class should have one and only one reason to change, meaning that a class should only have one job or responsibility.

# bad example

class SystemMonitor:
    class Process:
        def __init__(self, name, cpu_usage, memory_usage, disk_usage, network_activity, timestamp):
            self.name = name
            self.cpu_usage = cpu_usage
            self.memory_usage = memory_usage
            self.disk_usage = disk_usage
            self.network_activity = network_activity
            self.timestamp = timestamp
        
    def __init__(self):
        self.processes = []
    
    def load_activity(self):
        self.processes.append(self.Process("Process1", 10, 10, 50, 20, "2023-10-01T12:00:00"))
        self.processes.append(self.Process("Process2", 20, 20, 100, 40, "2023-10-01T12:05:00"))
        self.processes.append(self.Process("Process3", 30, 30, 150, 60, "2023-10-01T12:10:00"))
    
    def identify_anomalies(self):
        anomalies = []
        for process in self.processes:
            if process.cpu_usage > 20 or process.memory_usage > 20:
                anomalies.append(process)
        return anomalies
    
    def send_notification(self, anomalies):
        for anomaly in anomalies:
            print(f"Alert: Anomaly detected in {anomaly.name} at {anomaly.timestamp}. CPU Usage: {anomaly.cpu_usage}%, Memory Usage: {anomaly.memory_usage}%")

sm = SystemMonitor()
sm.load_activity()
anomalies = sm.identify_anomalies()
sm.send_notification(anomalies)

# good practice

class SystemMonitorImproved:
    class Process:
        def __init__(self, name, cpu_usage, memory_usage, disk_usage, network_activity, timestamp):
            self.name = name
            self.cpu_usage = cpu_usage
            self.memory_usage = memory_usage
            self.disk_usage = disk_usage
            self.network_activity = network_activity
            self.timestamp = timestamp
    
    class ActivityWatcher:
        def __init__(self, monitor):
            self.monitor = monitor
        
        def load_activity(self):
            self.monitor.processes.append(self.monitor.Process("Process1", 10, 10, 50, 20, "2023-10-01T12:00:00"))
            self.monitor.processes.append(self.monitor.Process("Process2", 20, 20, 100, 40, "2023-10-01T12:05:00"))
            self.monitor.processes.append(self.monitor.Process("Process3", 30, 30, 150, 60, "2023-10-01T12:10:00"))
    
    class AnomalyDetector:
        def __init__(self, monitor):
            self.monitor = monitor
        
        def identify_anomalies(self, process):
            if process.cpu_usage > 20 or process.memory_usage > 20:
                return True
            return False
    
    class Notifier:
        def __init__(self, monitor):
            self.monitor = monitor
        
        def send_notification(self, anomalies):
            for anomaly in anomalies:
                print(f"Alert: Anomaly detected in {anomaly.name} at {anomaly.timestamp}. CPU Usage: {anomaly.cpu_usage}%, Memory Usage: {anomaly.memory_usage}%")

    def __init__(self):
        self.processes = []
    
    def working(self):
        watcher = self.ActivityWatcher(self)
        watcher.load_activity()
        
        detector = self.AnomalyDetector(self)
        anomalies = [process for process in self.processes if detector.identify_anomalies(process)]
        notifier = self.Notifier(self)
        notifier.send_notification(anomalies)

sm_improved = SystemMonitorImproved()
sm_improved.working()