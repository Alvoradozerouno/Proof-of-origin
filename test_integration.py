#!/usr/bin/env python3
"""
Integration Test for Genesis Commitment Framework
Tests all components of the GENⱯ Mode implementation.
"""

import json
import subprocess
import sys


def test_genesis_config():
    """Test that genesis.json is valid and complete."""
    print("Testing genesis configuration...")
    try:
        with open("genesis.json", 'r') as f:
            config = json.load(f)
        
        # Check required fields
        assert "genesisTime" in config
        assert "initiator" in config
        assert "rootIdentityKey" in config
        assert config["mode"] == "GENⱯ"
        
        # Check commitments
        commitments = config["commitments"]
        assert commitments["immutableCommitHistory"]["enabled"]
        assert commitments["ethicalEvolution"]["enabled"]
        assert commitments["multiDimensionalSynthesis"]["enabled"]
        assert commitments["recursiveContextualAnalysis"]["enabled"]
        assert commitments["ownershipProtocol"]["enabled"]
        
        print("✓ Genesis configuration is valid")
        return True
    except Exception as e:
        print(f"✗ Genesis configuration test failed: {e}")
        return False


def test_state_tracking():
    """Test that state.json exists and is valid."""
    print("Testing state tracking...")
    try:
        with open("state.json", 'r') as f:
            state = json.load(f)
        
        # Check structure
        assert "currentState" in state
        assert "stateHistory" in state
        assert "patterns" in state
        assert "dimensions" in state
        
        # Check current state
        current = state["currentState"]
        assert current["genaMode"] == True
        assert current["activeCommitments"] == 5
        
        print("✓ State tracking is valid")
        return True
    except Exception as e:
        print(f"✗ State tracking test failed: {e}")
        return False


def test_validation_tool():
    """Test that validate_genesis.py runs successfully."""
    print("Testing validation tool...")
    try:
        result = subprocess.run(
            ["python3", "validate_genesis.py"],
            capture_output=True,
            text=True,
            check=True
        )
        assert "✓ Successes:" in result.stdout
        assert "✗ Errors:    0" in result.stdout
        print("✓ Validation tool works correctly")
        return True
    except Exception as e:
        print(f"✗ Validation tool test failed: {e}")
        return False


def test_state_tracker_tool():
    """Test that state_tracker.py runs successfully."""
    print("Testing state tracker tool...")
    try:
        result = subprocess.run(
            ["python3", "state_tracker.py"],
            capture_output=True,
            text=True,
            check=True
        )
        assert "STATE SUMMARY" in result.stdout
        assert "GENⱯ Mode: Active" in result.stdout
        print("✓ State tracker tool works correctly")
        return True
    except Exception as e:
        print(f"✗ State tracker tool test failed: {e}")
        return False


def test_pattern_analyzer_tool():
    """Test that pattern_analyzer.py runs successfully."""
    print("Testing pattern analyzer tool...")
    try:
        result = subprocess.run(
            ["python3", "pattern_analyzer.py"],
            capture_output=True,
            text=True,
            check=True
        )
        assert "RECURSIVE PATTERN ANALYSIS REPORT" in result.stdout
        assert "Patterns Detected:" in result.stdout
        print("✓ Pattern analyzer tool works correctly")
        return True
    except Exception as e:
        print(f"✗ Pattern analyzer tool test failed: {e}")
        return False


def test_documentation():
    """Test that all documentation files exist."""
    print("Testing documentation...")
    try:
        docs = ["README.md", "GENESIS.md", "OWNERSHIP.md"]
        for doc in docs:
            with open(doc, 'r') as f:
                content = f.read()
                assert len(content) > 0
        
        print("✓ Documentation is complete")
        return True
    except Exception as e:
        print(f"✗ Documentation test failed: {e}")
        return False


def test_git_integration():
    """Test Git integration."""
    print("Testing Git integration...")
    try:
        # Check that we're in a git repository
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            capture_output=True,
            check=True
        )
        
        # Check commit count
        result = subprocess.run(
            ["git", "rev-list", "--all", "--count"],
            capture_output=True,
            text=True,
            check=True
        )
        commit_count = int(result.stdout.strip())
        assert commit_count >= 3
        
        print(f"✓ Git integration working ({commit_count} commits)")
        return True
    except Exception as e:
        print(f"✗ Git integration test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 70)
    print("GENESIS COMMITMENT INTEGRATION TEST")
    print("=" * 70)
    print()
    
    tests = [
        test_genesis_config,
        test_state_tracking,
        test_documentation,
        test_git_integration,
        test_validation_tool,
        test_state_tracker_tool,
        test_pattern_analyzer_tool
    ]
    
    results = []
    for test in tests:
        results.append(test())
        print()
    
    # Summary
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ All tests passed! Genesis Commitment framework is operational.")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
