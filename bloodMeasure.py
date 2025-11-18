import adc_plot as plot
from mcp3021_driver import MCP3021
from time import time, sleep

experiment_time = 10

if __name__ == "__main__":
    adc = MCP3021(5, verbose = True)
    try:
        start_anchor = time()
        with open("calibrations_160.csv", 'w') as f:
            t = 0
            while time() - start_anchor < experiment_time:
                print(t, adc.get_voltage(), sep=',', file=f)
                t += 0.001
                sleep(0.001)
    finally:
        adc.deinit()