import random

def get_qos_metrics():
    return {
        'latency': random.uniform(10, 100),        # ms
        'bandwidth': random.uniform(1, 100),       # Mbps
        'cpu_usage': random.uniform(10, 90),       # %
        'packet_loss': random.uniform(0, 5)        # %
    }