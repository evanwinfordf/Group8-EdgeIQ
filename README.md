# Group8
# EdgeIQ: Intelligent Task Offloading in Mobile Edge Computing

EdgeIQ is a hybrid decision engine for Mobile Edge Computing (MEC) environments. It makes real-time task offloading decisions—choosing between local execution, edge nodes, or the cloud—based on live Quality of Service (QoS) metrics. The system combines rule-based logic for quick deployment and Deep Reinforcement Learning (DRL) for long-term adaptability.

---

## 🔍 Features

- 📶 Real-time QoS metric collection (latency, bandwidth, CPU, battery)
- ⚙️ Rule-based and DRL-based offloading decisions
- ⚡ Low-latency execution via edge nodes
- 🔋 Energy optimisation for mobile devices
- 📈 Modular and scalable architecture
- 🧠 DRL agent with TensorFlow/PyTorch integration

---

## 📁 Project Structure
EdgeIQ/
├── README.md
├── requirements.txt
├── rule_based_engine.py
├── drl_agent.py
├── environment_simulator.py
├── metrics_collector.py
├── demo_video.mp4  # optional
└── run_edgeiq.py
---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/EdgeIQ.git
cd EdgeIQ
```
2. Install Dependencies
   pip install -r requirements.txt
   
Main dependencies:
	•	numpy
	•	tensorflow or torch
	•	matplotlib

 🧪 How to Run
	- Rule-Based Engine:
 python rule_based_engine.py
 - DRL-Based Engine:
 python drl_agent.py
- Main Simulation Script:
  python run_edgeiq.py

This script:
	•	Simulates task arrivals
	•	Collects QoS metrics
	•	Applies the selected decision engine (rule-based or DRL)
	•	Logs results and statistics
