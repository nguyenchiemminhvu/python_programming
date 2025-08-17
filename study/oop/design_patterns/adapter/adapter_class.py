from abc import ABC, abstractmethod
import time

class third_party_i_analyzer(ABC):
    @abstractmethod
    def analyze_and_generate_plot(self, data, format):
        raise NotImplementedError("Subclasses should implement this!")

class third_party_analyzer(third_party_i_analyzer):
    def analyze_and_generate_plot(self, data, format):
        if (format != "xml" and format != "json"):
            return "Unsupported format. Please use 'xml' or 'json'."
        print("Hidden third-party analysis in progress...")
        time.sleep(2)  # Simulate time-consuming analysis
        print("Analysis complete. Generating plot...")
        time.sleep(1)  # Simulate plot generation time
        print("Plot generated.")

class i_service(ABC):
    @abstractmethod
    def produce_data(self):
        raise NotImplementedError("Subclasses should implement this!")

class location_service(i_service):
    def produce_data(self):
        data = []
        for i in range(5):
            data.append(f"Location {i}: (40.{i}12{8+i}, -74.00{6+i})")
        return data

class i_analyzer(ABC):
    @abstractmethod
    def analyze(self, data):
        raise NotImplementedError("Subclasses should implement this!")

class location_analyzer(i_analyzer):
    def analyze(self, data):
        print("Analyzing location data...")

class third_party_analyzer_adapter(location_analyzer, third_party_analyzer):
    def analyze(self, data):
        print("Convert data to XML format...")
        xml_data = "<data>" + "".join(f"<point>{d}</point>" for d in data) + "</data>"
        format = "xml"
        self.analyze_and_generate_plot(xml_data, format)

    def analyze_and_generate_plot(self, data, format):
        super().analyze_and_generate_plot(data, format)

class system:
    def __init__(self, location_service: i_service, analyzer: i_analyzer):
        self.location_service = location_service
        self.analyzer = analyzer
    
    def run(self):
        print("System is starting...")
        data = self.location_service.produce_data()
        print("Data produced:", data)
        self.analyzer.analyze(data)
        print("System run complete.")

if __name__ == "__main__":
    loc_service = location_service()
    analyzer = third_party_analyzer_adapter()
    sys = system(loc_service, analyzer)
    sys.run()