import os
import time
import subprocess

print("🚀 Starting ZANKENE Mobile Engine & Tunnel...")

# Start Streamlit in background
streamlit_cmd = "streamlit run zankene/mobile_ui.py --server.port 8502 --server.headless true"
subprocess.Popen(streamlit_cmd, shell=True)

time.sleep(5)

# Start Tunnel and keep alive
ssh_cmd = "ssh -o ServerAliveInterval=30 -R 80:localhost:8502 nokey@localhost.run"
subprocess.run(ssh_cmd, shell=True)