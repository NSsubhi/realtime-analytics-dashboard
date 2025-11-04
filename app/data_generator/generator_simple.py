"""
Simplified Data Generator
Sends events directly to API
"""

import requests
import random
import time
from datetime import datetime
from typing import Optional

class DataGenerator:
    def __init__(self, api_url: str = "http://localhost:8000"):
        self.api_url = api_url
        self.running = False
    
    def generate_event(self) -> dict:
        """Generate a random event"""
        event_types = ["click", "purchase", "view", "login", "logout", "signup"]
        users = [f"user_{i}" for i in range(1, 101)]
        
        return {
            "type": random.choice(event_types),
            "user_id": random.choice(users),
            "timestamp": datetime.now().isoformat(),
            "metadata": {
                "value": random.randint(10, 1000),
                "page": f"/page_{random.randint(1, 10)}",
                "device": random.choice(["mobile", "desktop", "tablet"])
            }
        }
    
    def start(self, interval: float = 1.0, duration: Optional[int] = None):
        """Start generating events"""
        self.running = True
        start_time = time.time()
        count = 0
        
        print(f"Starting data generator... Sending to {self.api_url}")
        
        try:
            while self.running:
                event = self.generate_event()
                try:
                    response = requests.post(
                        f"{self.api_url}/api/events",
                        json=event,
                        timeout=2
                    )
                    if response.status_code == 200:
                        count += 1
                        if count % 10 == 0:
                            print(f"Sent {count} events...")
                    else:
                        print(f"Error: {response.status_code}")
                except requests.exceptions.ConnectionError:
                    print(f"⚠️ Cannot connect to API at {self.api_url}")
                    print("Make sure the backend is running!")
                    break
                except Exception as e:
                    print(f"Error sending event: {e}")
                
                if duration and (time.time() - start_time) > duration:
                    break
                
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStopping generator...")
        finally:
            self.running = False
            print(f"\n✅ Sent {count} events total")
    
    def stop(self):
        """Stop generating events"""
        self.running = False

if __name__ == "__main__":
    import sys
    api_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    generator = DataGenerator(api_url)
    generator.start(interval=0.5)

