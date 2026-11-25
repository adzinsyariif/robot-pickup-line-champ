import os

LINE = "I ran 10,000 simulations of asking you out and you said yes in 9,999. Care to help me debug the last one?"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
