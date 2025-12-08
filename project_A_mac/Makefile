SRC_DIR = src
SIM_DIR = simulation
RESULTS_DIR = results
TOP = mac_tb
SRC = $(SRC_DIR)/mac.v $(SIM_DIR)/mac_tb.v
VCD = $(RESULTS_DIR)/mac.vcd
IVERILOG = iverilog
VVP = vvp
all: run
build:
	$(IVERILOG) -o sim.out $(SRC)
run: build
	$(VVP) sim.out
clean:
	rm -f sim.out $(VCD)
.PHONY: all build run clean
