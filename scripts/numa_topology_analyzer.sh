#!/bin/bash

# NUMA Topology Analyzer for V16000
# Optimizes memory locality for multi-socket systems

echo "========================================"
echo "NUMA Topology Analysis for V16000"
echo "========================================"
echo ""

# Check if NUMA tools are installed
if ! command -v numactl &> /dev/null; then
    echo "Installing NUMA tools..."
    sudo apt-get install -y numactl numa-tools libnuma-dev > /dev/null 2>&1
fi

# Display NUMA hardware info
echo "[System NUMA Configuration]"
echo ""

if [ -f /proc/cpuinfo ]; then
    NUMA_NODES=$(numactl --hardware | grep "available:" | awk '{print $2}')
    echo "Total NUMA Nodes: $NUMA_NODES"
    echo ""
fi

# Show node distances (critical for inter-node latency)
echo "[NUMA Node Distances (in hops - lower is better)]"
echo ""
numactl --hardware | grep -A 20 "distance matrix"
echo ""

# CPU to NUMA mapping
echo "[CPU to NUMA Node Mapping]"
echo ""
for node in $(seq 0 $(($NUMA_NODES - 1))); do
    CPUS=$(numactl --hardware | grep "node $node cpus:" | cut -d: -f2-)
    echo "NUMA Node $node: CPUs$CPUS"
done
echo ""

# Memory per node
echo "[Memory Distribution per NUMA Node]"
echo ""
numactl --hardware | grep "node.*memory"
echo ""

# Test memory locality performance
echo "[Memory Locality Performance Test]"
echo ""
echo "Testing inter-node latency..."
echo "Command: numactl --membind=0 ./v16000_engine (local memory)"
echo "Command: numactl --membind=1,2 ./v16000_engine (remote memory)"
echo ""

# Show recommended binding strategy
echo "[Optimization Recommendations]"
echo ""
echo "1. Pin threads to specific NUMA nodes:"
echo "   numactl --cpunodebind=0 --membind=0 ./v16000_engine"
echo ""
echo "2. For multi-threaded execution:"
echo "   numactl --cpunodebind=0-3 --membind=0 ./v16000_engine"
echo ""
echo "3. Monitor NUMA statistics:"
echo "   numastat -p PID  (shows page migrations)"
echo ""
echo "4. Check for NUMA imbalance:"
echo "   cat /proc/sys/vm/numa_stat"
echo ""

echo "========================================"
echo "For production, use numactl with:"
echo "--cpunodebind: Pin execution to specific NUMA nodes"
echo "--membind: Allocate memory from specific NUMA nodes"
echo "========================================"
