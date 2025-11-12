#!/usr/bin/env python3
"""
Recursive Pattern Analyzer for GENⱯ Mode
Performs recursive contextual analysis to detect emergent patterns.
"""

import json
import subprocess
from datetime import datetime
from typing import Dict, List, Tuple, Any
from collections import defaultdict


class PatternAnalyzer:
    """Analyzes repository for emergent patterns through recursive analysis."""
    
    def __init__(self, max_depth: int = 5):
        self.max_depth = max_depth
        self.patterns = []
        self.analysis_cache = {}
    
    def analyze_commit_patterns(self, depth: int = 0) -> List[Dict]:
        """Recursively analyze commit patterns."""
        if depth >= self.max_depth:
            return []
        
        try:
            # Get commit history
            result = subprocess.run(
                ["git", "log", "--all", "--format=%H|%an|%ae|%at|%s"],
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    parts = line.split('|')
                    if len(parts) >= 5:
                        commits.append({
                            "hash": parts[0],
                            "author": parts[1],
                            "email": parts[2],
                            "timestamp": int(parts[3]),
                            "message": parts[4]
                        })
            
            # Analyze patterns
            patterns = []
            
            # Pattern 1: Commit frequency
            if len(commits) > 1:
                patterns.append({
                    "type": "commit_frequency",
                    "description": f"Repository has {len(commits)} commits",
                    "depth": depth,
                    "confidence": 1.0
                })
            
            # Pattern 2: Author diversity
            authors = set(c["author"] for c in commits)
            if len(authors) > 0:
                patterns.append({
                    "type": "author_diversity",
                    "description": f"{len(authors)} unique author(s) detected",
                    "depth": depth,
                    "confidence": 1.0
                })
            
            # Pattern 3: Message patterns
            message_keywords = defaultdict(int)
            for commit in commits:
                words = commit["message"].lower().split()
                for word in words:
                    if len(word) > 3:
                        message_keywords[word] += 1
            
            if message_keywords:
                top_keywords = sorted(message_keywords.items(), 
                                    key=lambda x: x[1], reverse=True)[:5]
                patterns.append({
                    "type": "message_patterns",
                    "description": f"Top keywords: {', '.join(k for k, v in top_keywords)}",
                    "depth": depth,
                    "confidence": 0.8
                })
            
            # Recursive analysis
            if depth < self.max_depth - 1:
                sub_patterns = self.analyze_commit_patterns(depth + 1)
                patterns.extend(sub_patterns)
            
            return patterns
            
        except Exception as e:
            print(f"Error analyzing commit patterns: {e}")
            return []
    
    def analyze_file_patterns(self, depth: int = 0) -> List[Dict]:
        """Recursively analyze file patterns."""
        if depth >= self.max_depth:
            return []
        
        try:
            # Get tracked files
            result = subprocess.run(
                ["git", "ls-files"],
                capture_output=True,
                text=True,
                check=True
            )
            
            files = [f for f in result.stdout.strip().split('\n') if f]
            
            patterns = []
            
            # Pattern 1: File types
            file_types = defaultdict(int)
            for file in files:
                if '.' in file:
                    ext = file.split('.')[-1]
                    file_types[ext] += 1
            
            if file_types:
                patterns.append({
                    "type": "file_types",
                    "description": f"File types: {dict(file_types)}",
                    "depth": depth,
                    "confidence": 1.0
                })
            
            # Pattern 2: Directory structure
            directories = set()
            for file in files:
                if '/' in file:
                    directories.add(file.rsplit('/', 1)[0])
            
            if directories:
                patterns.append({
                    "type": "directory_structure",
                    "description": f"{len(directories)} directories detected",
                    "depth": depth,
                    "confidence": 1.0
                })
            
            return patterns
            
        except Exception as e:
            print(f"Error analyzing file patterns: {e}")
            return []
    
    def analyze_ethical_patterns(self) -> List[Dict]:
        """Analyze patterns related to ethical compliance."""
        patterns = []
        
        try:
            # Check for documentation
            result = subprocess.run(
                ["git", "ls-files", "*.md"],
                capture_output=True,
                text=True,
                check=True
            )
            
            docs = [f for f in result.stdout.strip().split('\n') if f]
            
            if docs:
                patterns.append({
                    "type": "ethical_documentation",
                    "description": f"Documentation files present: {len(docs)}",
                    "depth": 0,
                    "confidence": 0.9
                })
            
            # Check for genesis files
            genesis_files = ["genesis.json", "GENESIS.md"]
            for gfile in genesis_files:
                try:
                    with open(gfile, 'r') as f:
                        patterns.append({
                            "type": "ethical_framework",
                            "description": f"Genesis framework file found: {gfile}",
                            "depth": 0,
                            "confidence": 1.0
                        })
                except FileNotFoundError:
                    pass
            
        except Exception as e:
            print(f"Error analyzing ethical patterns: {e}")
        
        return patterns
    
    def analyze_all(self) -> List[Dict]:
        """Run all pattern analyses."""
        all_patterns = []
        
        print("Analyzing commit patterns...")
        all_patterns.extend(self.analyze_commit_patterns())
        
        print("Analyzing file patterns...")
        all_patterns.extend(self.analyze_file_patterns())
        
        print("Analyzing ethical patterns...")
        all_patterns.extend(self.analyze_ethical_patterns())
        
        self.patterns = all_patterns
        return all_patterns
    
    def generate_report(self) -> str:
        """Generate a pattern analysis report."""
        report_lines = [
            "=" * 70,
            "RECURSIVE PATTERN ANALYSIS REPORT",
            "=" * 70,
            f"Timestamp: {datetime.utcnow().isoformat()}",
            f"Max Recursive Depth: {self.max_depth}",
            f"Patterns Detected: {len(self.patterns)}",
            "",
            "DETECTED PATTERNS",
            "-" * 70
        ]
        
        # Group patterns by type
        patterns_by_type = defaultdict(list)
        for pattern in self.patterns:
            patterns_by_type[pattern["type"]].append(pattern)
        
        for ptype, patterns in sorted(patterns_by_type.items()):
            report_lines.append(f"\n{ptype.upper().replace('_', ' ')}:")
            for pattern in patterns:
                depth_indicator = "  " * pattern["depth"]
                confidence = pattern["confidence"] * 100
                report_lines.append(
                    f"{depth_indicator}• {pattern['description']} "
                    f"(confidence: {confidence:.0f}%, depth: {pattern['depth']})"
                )
        
        report_lines.append("")
        report_lines.append("=" * 70)
        
        return "\n".join(report_lines)


def main():
    """Main entry point."""
    analyzer = PatternAnalyzer()
    
    print("Starting recursive pattern analysis...\n")
    analyzer.analyze_all()
    
    report = analyzer.generate_report()
    print(report)


if __name__ == "__main__":
    main()
