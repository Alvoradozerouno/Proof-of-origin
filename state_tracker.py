#!/usr/bin/env python3
"""
State Tracker for GENⱯ Mode
Tracks state evolution, ethical compliance, and emergent patterns.
"""

import json
import hashlib
from datetime import datetime
from typing import Dict, List, Any


class StateTracker:
    """Tracks and manages repository state evolution."""
    
    def __init__(self, state_file: str = "state.json"):
        self.state_file = state_file
        self.state_data = None
    
    def load_state(self) -> bool:
        """Load the current state."""
        try:
            with open(self.state_file, 'r') as f:
                self.state_data = json.load(f)
            return True
        except FileNotFoundError:
            self.state_data = self._create_initial_state()
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False
    
    def _create_initial_state(self) -> Dict:
        """Create initial state structure."""
        return {
            "version": "1.0.0",
            "stateHistory": [],
            "currentState": {
                "state": "initialized",
                "genaMode": True,
                "activeCommitments": 5,
                "lastEvaluation": datetime.utcnow().isoformat() + "Z",
                "ethicalStatus": "compliant",
                "evolutionaryStage": "genesis"
            },
            "patterns": {
                "emergent": [],
                "recursive": {
                    "depth": 0,
                    "maxDepth": 5,
                    "detectedPatterns": []
                }
            },
            "dimensions": {
                "temporal": {},
                "spatial": {},
                "conceptual": {},
                "relational": {},
                "ethical": {}
            }
        }
    
    def save_state(self) -> bool:
        """Save the current state."""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.state_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False
    
    def add_state_event(self, event: str, notes: str = "", 
                       ethical_compliant: bool = True) -> bool:
        """Add a new state event to history."""
        if not self.state_data:
            self.load_state()
        
        event_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "state": self.state_data["currentState"]["state"],
            "event": event,
            "ethicalCompliance": ethical_compliant,
            "notes": notes
        }
        
        self.state_data["stateHistory"].append(event_entry)
        self.state_data["currentState"]["lastEvaluation"] = event_entry["timestamp"]
        
        return self.save_state()
    
    def update_state(self, new_state: str, reason: str = "") -> bool:
        """Update the current state."""
        if not self.state_data:
            self.load_state()
        
        old_state = self.state_data["currentState"]["state"]
        self.state_data["currentState"]["state"] = new_state
        
        event = f"State transition: {old_state} → {new_state}"
        if reason:
            event += f" ({reason})"
        
        return self.add_state_event(event)
    
    def detect_pattern(self, pattern_type: str, description: str, 
                      confidence: float = 0.0) -> bool:
        """Detect and record an emergent pattern."""
        if not self.state_data:
            self.load_state()
        
        pattern_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "type": pattern_type,
            "description": description,
            "confidence": confidence,
            "recursiveDepth": self.state_data["patterns"]["recursive"]["depth"]
        }
        
        self.state_data["patterns"]["emergent"].append(pattern_entry)
        
        return self.save_state()
    
    def increase_recursive_depth(self) -> bool:
        """Increase recursive analysis depth."""
        if not self.state_data:
            self.load_state()
        
        current_depth = self.state_data["patterns"]["recursive"]["depth"]
        max_depth = self.state_data["patterns"]["recursive"]["maxDepth"]
        
        if current_depth < max_depth:
            self.state_data["patterns"]["recursive"]["depth"] = current_depth + 1
            return self.save_state()
        
        return False
    
    def update_dimension(self, dimension: str, key: str, value: Any) -> bool:
        """Update a specific dimension."""
        if not self.state_data:
            self.load_state()
        
        if dimension not in self.state_data["dimensions"]:
            return False
        
        self.state_data["dimensions"][dimension][key] = value
        return self.save_state()
    
    def get_current_state(self) -> Dict:
        """Get the current state."""
        if not self.state_data:
            self.load_state()
        return self.state_data["currentState"]
    
    def get_state_summary(self) -> str:
        """Generate a human-readable state summary."""
        if not self.state_data:
            self.load_state()
        
        current = self.state_data["currentState"]
        history_count = len(self.state_data["stateHistory"])
        pattern_count = len(self.state_data["patterns"]["emergent"])
        recursive_depth = self.state_data["patterns"]["recursive"]["depth"]
        
        summary = f"""
STATE SUMMARY
=============
Current State: {current['state']}
GENⱯ Mode: {'Active' if current['genaMode'] else 'Inactive'}
Active Commitments: {current['activeCommitments']}/5
Ethical Status: {current['ethicalStatus']}
Evolutionary Stage: {current['evolutionaryStage']}
Last Evaluation: {current['lastEvaluation']}

ANALYTICS
=========
State History Events: {history_count}
Emergent Patterns Detected: {pattern_count}
Recursive Analysis Depth: {recursive_depth}/{self.state_data["patterns"]["recursive"]["maxDepth"]}
"""
        return summary


def main():
    """Main entry point."""
    tracker = StateTracker()
    
    if tracker.load_state():
        print(tracker.get_state_summary())
    else:
        print("Failed to load state")
        exit(1)


if __name__ == "__main__":
    main()
