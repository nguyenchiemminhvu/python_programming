import time

class data_analyzer:
    def __init__(self, callback=None):
        self.callback = callback

    def analyze(self, data):
        print("analyze data in progress...")
        time.sleep(1)  # Simulate time-consuming analysis
        print("analyzed data:", data)
        if self.callback:
            self.callback()

def on_data_analyzed():
    print("Data analysis complete.")

if __name__ == "__main__":
    analyzer = data_analyzer(callback=on_data_analyzed)
    analyzer.analyze("Sample data")