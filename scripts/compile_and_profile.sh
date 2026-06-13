#!/bin/bash

# V16000 Compilation & Profiling Script
# ARM Neoverse V2 - Sub-2ms Latency Target

set -e

echo "========================================"
echo "V16000 Execution Engine - Build & Profile"
echo "========================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Compilation flags for ARM Neoverse V2
echo -e "${YELLOW}[1/4] Compiling for ARM Neoverse V2...${NC}"
COMPILE_FLAGS="-O3 -march=armv8.2-a+sve2 -mtune=neoverse-v2 -ffast-math -funroll-loops -fvectorize -mcpu=neoverse-v2"

g++ $COMPILE_FLAGS -o v16000_engine src/v16000_optimized.cpp -lpthread -lm

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Compilation successful!${NC}"
else
    echo -e "${RED}✗ Compilation failed!${NC}"
    exit 1
fi

echo -e "${YELLOW}[2/4] Checking CPU features...${NC}"

# Check for SVE2 support
if grep -q "sve2" /proc/cpuinfo; then
    echo -e "${GREEN}✓ SVE2 support detected${NC}"
else
    echo -e "${YELLOW}! SVE2 not detected, will use NEON fallback${NC}"
fi

# Check for NEON
if grep -q "neon" /proc/cpuinfo; then
    echo -e "${GREEN}✓ NEON support detected${NC}"
else
    echo -e "${RED}✗ NEON support missing!${NC}"
fi

echo -e "${YELLOW}[3/4] Running performance profiling...${NC}"

# Profile with perf
echo "Performance Metrics:"
echo "-------------------"
perf stat -e cycles,instructions,cache-references,cache-misses,L1-dcache-load-misses,branch-misses,task-clock ./v16000_engine

echo ""
echo -e "${YELLOW}[4/4] Advanced profiling (if running as root)...${NC}"

# Advanced profiling (requires sudo/root)
if [ "$EUID" -eq 0 ]; then
    echo "CPU Cycles & Cache Performance:"
    perf record -e cycles,LLC-loads,LLC-load-misses,L1-dcache-loads -F 1000 -o perf.data ./v16000_engine > /dev/null 2>&1
    perf report -i perf.data --stdio | head -50
    rm -f perf.data
else
    echo -e "${YELLOW}Skipping root-required profiling. Run with sudo for detailed cache analysis.${NC}"
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Build & Profile Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Next steps:"
echo "1. Check latency: time ./v16000_engine"
echo "2. Profile with: perf stat -e task-clock ./v16000_engine"
echo "3. Analyze hotspots: perf top -p \$(pgrep v16000_engine)"
