from abc import ABC, abstractmethod
import time
import threading
from typing import Any, Dict, List, Optional

class snapshot(ABC):
    def __init__(self, name: str, timestamp: float):
        self._name = name
        self._timestamp = timestamp

    def get_name(self):
        return self._name

    def get_snapshot_time(self):
        return self._timestamp

class editor_snapshot(snapshot):
    def __init__(self, name: str, content: str):
        super().__init__(name, time.time())
        self._content = content

class originator(ABC):
    @abstractmethod
    def create_snapshot(self) -> snapshot:
        pass
    
    @abstractmethod
    def restore_snapshot(self, snapshot: snapshot) -> None:
        pass

class text_editor(originator):
    def __init__(self):
        self._content = ""
        self._snapshots: List[snapshot] = []

    def write(self, text: str) -> None:
        self._content += text

    def create_snapshot(self):
        snap = editor_snapshot(f"Snapshot {len(self._snapshots) + 1}", self._content)
        print(f"Creating snapshot: {snap.get_name()} at {snap.get_snapshot_time()}")
        self._snapshots.append(snap)

    def restore_snapshot(self, snapshot: snapshot) -> None:
        if isinstance(snapshot, editor_snapshot):
            self._content = snapshot._content
            print(f"Restored to {snapshot.get_name()} at {snapshot.get_snapshot_time()}")
        else:
            raise ValueError("Invalid snapshot type")

class application:
    def __init__(self):
        self._editor = text_editor()
        self._running = True
        self._thread = threading.Thread(target=self._run)
        self._thread.daemon = True
        self._thread.start()
    
    def _run(self):
        while self._running:
            time.sleep(5)
            self._editor.create_snapshot()

if __name__ == "__main__":
    app = application()
    
    while (True):
        try:
            text = input("Enter text (or 'exit' to quit): ")
            if text.lower() == 'exit':
                break
            if text.lower() == 'ctrl z':
                if app._editor._snapshots:
                    last_snapshot = app._editor._snapshots.pop()
                    app._editor.restore_snapshot(last_snapshot)
                else:
                    print("No snapshots to restore.")
                continue
            app._editor.write(text)
            print(f"Current content: {app._editor._content}")
        except KeyboardInterrupt:
            print()
            print("\nExiting application...")
            break

    app._running = False