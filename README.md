# Group8
# EdgeIQ: Intelligent Task Offloading in Mobile Edge Computing Environments

EdgeIQ is a hybrid task offloading system designed for Mobile Edge Computing (MEC). It supports latency-sensitive applications by dynamically deciding whether to execute tasks locally, offload them to a nearby edge server, or send them to the cloud. The project currently includes a rule-based decision engine, with plans to integrate a Deep Reinforcement Learning (DRL) module.

---

## 📁 Project Structure
EdgeIQ/
├── qos_simulator.py            # Simulates real-time QoS metrics
├── rule_based_decision.py     # Rule-based offloading decision logic
├── edgeiq_main.py             # Main execution loop and logging
└── logs/
└── edgeiq_log.csv         # Log file storing decisions and metrics
---

## 🧠 Features

- Real-time simulation of network QoS metrics (latency, bandwidth, CPU usage, packet loss)
- Rule-based decision-making system
- Modular and extensible codebase
- CSV logging for later performance analysis
- Future-ready for DRL agent integration

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Ubuntu 22.04 (recommended to run inside VirtualBox)
- Pip (Python package manager)

### Install Dependencies

```bash```
pip3 install pandas

▶️ How to Run:
1. Clone or copy the repository into your Ubuntu VM:
git clone https://github.com/your-repo/EdgeIQ.git
cd EdgeIQ
2. Execute the main script:
python3 edgeiq_main.py
3.	Output:
   - Console: Displays real-time decisions
   - File: logs/edgeiq_log.csv stores all decisions and QoS data for analysis
     
🧪 Simulation Logic

Each simulation cycle:
	•	Generates random latency, bandwidth, CPU usage, and packet loss
	•	Applies decision rules:
	•	Process locally if latency < 30 ms and CPU < 60%
	•	Offload to edge if bandwidth > 20 Mbps and edge CPU < 70%
	•	Otherwise, queue or send to cloud (currently symbolic)
 
📜 License

MIT License
