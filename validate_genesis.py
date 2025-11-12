#!/usr/bin/env python3
"""
Genesis Commitment Validator
Validates the integrity and compliance of the Genesis Commitment framework.
"""

import json
import hashlib
import subprocess
from datetime import datetime
from typing import Dict, List, Tuple


class GenesisValidator:
    """Validator for Genesis Commitment compliance."""
    
    def __init__(self, genesis_file: str = "genesis.json"):
        self.genesis_file = genesis_file
        self.genesis_config = None
        self.validation_results = []
    
    def load_genesis_config(self) -> bool:
        """Load the Genesis configuration file."""
        try:
            with open(self.genesis_file, 'r') as f:
                self.genesis_config = json.load(f)
            return True
        except Exception as e:
            self.add_result("ERROR", f"Failed to load genesis.json: {e}")
            return False
    
    def add_result(self, level: str, message: str):
        """Add a validation result."""
        self.validation_results.append({
            "level": level,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        })
    
    def validate_structure(self) -> bool:
        """Validate the structure of genesis.json."""
        required_fields = [
            "genesisTime", "initiator", "rootIdentityKey",
            "commitments", "stateManagement"
        ]
        
        for field in required_fields:
            if field not in self.genesis_config:
                self.add_result("ERROR", f"Missing required field: {field}")
                return False
        
        self.add_result("SUCCESS", "Genesis configuration structure is valid")
        return True
    
    def validate_commitments(self) -> bool:
        """Validate that all Genesis Commitments are properly configured."""
        commitments = self.genesis_config.get("commitments", {})
        required_commitments = [
            "immutableCommitHistory",
            "ethicalEvolution",
            "multiDimensionalSynthesis",
            "recursiveContextualAnalysis",
            "ownershipProtocol"
        ]
        
        all_valid = True
        for commitment in required_commitments:
            if commitment not in commitments:
                self.add_result("ERROR", f"Missing commitment: {commitment}")
                all_valid = False
            elif not commitments[commitment].get("enabled", False):
                self.add_result("WARNING", f"Commitment not enabled: {commitment}")
        
        if all_valid:
            self.add_result("SUCCESS", "All Genesis Commitments are configured")
        
        return all_valid
    
    def validate_immutable_history(self) -> bool:
        """Validate immutable commit history."""
        try:
            # Check if git repository exists
            result = subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Get commit count
            result = subprocess.run(
                ["git", "rev-list", "--all", "--count"],
                capture_output=True,
                text=True,
                check=True
            )
            commit_count = int(result.stdout.strip())
            
            self.add_result("SUCCESS", f"Immutable history validated: {commit_count} commits")
            return True
        except Exception as e:
            self.add_result("ERROR", f"Failed to validate commit history: {e}")
            return False
    
    def validate_ethical_guidelines(self) -> bool:
        """Validate ethical guidelines are defined."""
        ethical = self.genesis_config.get("commitments", {}).get("ethicalEvolution", {})
        guidelines = ethical.get("ethicalGuidelines", [])
        
        if len(guidelines) < 3:
            self.add_result("WARNING", "Less than 3 ethical guidelines defined")
            return False
        
        self.add_result("SUCCESS", f"{len(guidelines)} ethical guidelines defined")
        return True
    
    def validate_dimensions(self) -> bool:
        """Validate multi-dimensional synthesis dimensions."""
        synthesis = self.genesis_config.get("commitments", {}).get("multiDimensionalSynthesis", {})
        dimensions = synthesis.get("dimensions", [])
        
        if len(dimensions) < 3:
            self.add_result("WARNING", "Less than 3 dimensions defined for synthesis")
            return False
        
        self.add_result("SUCCESS", f"{len(dimensions)} dimensions configured for synthesis")
        return True
    
    def validate_genesis_identity(self) -> bool:
        """Validate Genesis identity parameters."""
        genesis_time = self.genesis_config.get("genesisTime")
        initiator = self.genesis_config.get("initiator")
        root_key = self.genesis_config.get("rootIdentityKey")
        
        if not all([genesis_time, initiator, root_key]):
            self.add_result("ERROR", "Incomplete genesis identity parameters")
            return False
        
        # Validate root key format
        if not root_key.startswith("ROOT-"):
            self.add_result("WARNING", "Root identity key doesn't follow expected format")
        
        self.add_result("SUCCESS", f"Genesis identity validated: {initiator}")
        return True
    
    def generate_report(self) -> str:
        """Generate a validation report."""
        report_lines = [
            "=" * 70,
            "GENESIS COMMITMENT VALIDATION REPORT",
            "=" * 70,
            f"Timestamp: {datetime.utcnow().isoformat()}",
            f"Genesis File: {self.genesis_file}",
            ""
        ]
        
        # Count results by level
        errors = sum(1 for r in self.validation_results if r["level"] == "ERROR")
        warnings = sum(1 for r in self.validation_results if r["level"] == "WARNING")
        successes = sum(1 for r in self.validation_results if r["level"] == "SUCCESS")
        
        report_lines.extend([
            "SUMMARY",
            "-" * 70,
            f"✓ Successes: {successes}",
            f"⚠ Warnings:  {warnings}",
            f"✗ Errors:    {errors}",
            "",
            "DETAILS",
            "-" * 70
        ])
        
        for result in self.validation_results:
            symbol = {
                "SUCCESS": "✓",
                "WARNING": "⚠",
                "ERROR": "✗"
            }.get(result["level"], "•")
            
            report_lines.append(f"{symbol} [{result['level']}] {result['message']}")
        
        report_lines.append("=" * 70)
        
        return "\n".join(report_lines)
    
    def run_validation(self) -> bool:
        """Run all validation checks."""
        print("Running Genesis Commitment validation...\n")
        
        if not self.load_genesis_config():
            return False
        
        # Run all validation checks
        checks = [
            self.validate_structure,
            self.validate_genesis_identity,
            self.validate_commitments,
            self.validate_immutable_history,
            self.validate_ethical_guidelines,
            self.validate_dimensions
        ]
        
        for check in checks:
            check()
        
        # Generate and print report
        report = self.generate_report()
        print(report)
        
        # Return True if no errors
        errors = sum(1 for r in self.validation_results if r["level"] == "ERROR")
        return errors == 0


def main():
    """Main entry point."""
    validator = GenesisValidator()
    success = validator.run_validation()
    
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
