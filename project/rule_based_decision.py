def decide_offload(qos):
    if qos['latency'] < 50 and qos['bandwidth'] > 10 and qos['cpu_usage'] < 80 and qos['packet_loss'] < 2:
        return "Offload to Edge"
    else:
        return "Run Locally"