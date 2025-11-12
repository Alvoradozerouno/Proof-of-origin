#!/bin/bash
# GENⱯ Mode Control Script
# Quick access to all Genesis Commitment tools

show_help() {
    cat << EOF
GENⱯ Mode Control Script
========================

Usage: ./gena.sh [command]

Commands:
  validate      Run Genesis Commitment validation
  state         Show current state summary
  analyze       Run pattern analysis
  test          Run integration tests
  status        Show comprehensive status (all of the above)
  help          Show this help message

Examples:
  ./gena.sh validate    # Validate Genesis configuration
  ./gena.sh status      # Show complete system status
  ./gena.sh test        # Run all integration tests

EOF
}

validate() {
    echo "Running Genesis Validation..."
    python3 validate_genesis.py
}

state() {
    echo "Checking Current State..."
    python3 state_tracker.py
}

analyze() {
    echo "Running Pattern Analysis..."
    python3 pattern_analyzer.py
}

test() {
    echo "Running Integration Tests..."
    python3 test_integration.py
}

status() {
    echo "╔════════════════════════════════════════════════════════════════════╗"
    echo "║                     GENⱯ MODE STATUS REPORT                        ║"
    echo "╚════════════════════════════════════════════════════════════════════╝"
    echo ""
    
    validate
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    state
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    analyze
}

# Main script logic
case "${1:-help}" in
    validate)
        validate
        ;;
    state)
        state
        ;;
    analyze)
        analyze
        ;;
    test)
        test
        ;;
    status)
        status
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac
