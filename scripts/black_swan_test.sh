#!/bin/bash

# Black Swan Protocol Test Suite
# Tests nano-lot activation under volatility spikes

echo "========================================"
echo "Black Swan Protocol Test Suite"
echo "========================================"
echo ""

# Compile with debug symbols for testing
echo "[Compiling with debug symbols...]"
g++ -O2 -g -march=armv8.2-a+sve2 -mtune=neoverse-v2 \
    -DDEBUG_BLACK_SWAN=1 \
    -o v16000_engine_debug src/v16000_optimized.cpp -lpthread -lm

echo "✓ Debug build complete"
echo ""

echo "[Running Black Swan Volatility Test]"
echo ""
echo "Scenario 1: Normal market conditions"
./v16000_engine_debug <<< "normal"

echo ""
echo "Scenario 2: High volatility spike (>2.5%)"
echo "Expected: Nano-lot mode activation, 1000x volume reduction"
./v16000_engine_debug <<< "high_volatility"

echo ""
echo "Scenario 3: Flash crash simulation"
echo "Expected: Emergency nano-lot throttling"
./v16000_engine_debug <<< "flash_crash"

echo ""
echo "========================================"
echo "Black Swan Protocol Tests Complete"
echo "========================================"
echo ""
echo "Key Metrics to Monitor:"
echo "- Nano-lot Activations: Should increase during volatility"
echo "- Executed Volume: Should drop 1000x in nano-lot mode"
echo "- Execution Latency: Should remain <2ms even under stress"
echo "- Core Temperature: Should stay <85°C"
