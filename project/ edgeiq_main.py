import time
import pandas as pd
from qos_simulator import get_qos_metrics
from rule_based_decision import decide_offload

log_data = []

for i in range(10):  # Simulate 10 decisions
    qos = get_qos_metrics()
    decision = decide_offload(qos)
    qos['decision'] = decision
    log_data.append(qos)
    print(f"[{i+1}] Decision: {decision} | QoS: {qos}")
    time.sleep(1)

# Save to CSV log
df = pd.DataFrame(log_data)
df.to_csv("logs/edgeiq_log.csv", index=False)