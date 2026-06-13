.PHONY: build profile numa-analyze black-swan-test clean help

# ARM Neoverse V2 Optimization Flags
CXX = g++
CFLAGS = -O3 -march=armv8.2-a+sve2 -mtune=neoverse-v2 \
         -ffast-math -funroll-loops -fvectorize -mcpu=neoverse-v2
LDFLAGS = -lpthread -lm

TARGET = v16000_engine
SOURCE = src/v16000_optimized.cpp

help:
	@echo "V16000 Execution Engine - Build Targets"
	@echo "========================================="
	@echo "make build         - Compile optimized engine"
	@echo "make profile       - Build and profile performance"
	@echo "make numa-analyze  - Run NUMA topology analysis"
	@echo "make black-swan    - Test Black Swan protocol"
	@echo "make clean         - Remove compiled binaries"
	@echo ""

build:
	@echo "[Building V16000 Engine for ARM Neoverse V2...]"
	$(CXX) $(CFLAGS) -o $(TARGET) $(SOURCE) $(LDFLAGS)
	@echo "✓ Build complete: ./$(TARGET)"

profile: build
	@echo ""
	@echo "[Running Performance Profile...]"
	@bash scripts/compile_and_profile.sh

numa-analyze:
	@echo "[NUMA Topology Analysis...]"
	@bash scripts/numa_topology_analyzer.sh

black-swan: build
	@echo ""
	@echo "[Running Black Swan Protocol Tests...]"
	@bash scripts/black_swan_test.sh

clean:
	@echo "Cleaning up..."
	@rm -f $(TARGET) $(TARGET)_debug perf.data perf.data.old
	@echo "✓ Clean complete"

all: build profile numa-analyze

.SILENT:
