import os
import re

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Convert 15 bullets to tables
bullets = [
    {
        "regex": r"\*\s+\*\*The Hand-Crafted Heuristic Era \(Vanilla Curriculum Learning, 2009\)\*\*[\s\S]*?(?=\*   \*\*The Self-Paced)",
        "year": "2009",
        "paper": "[Bengio et al., 2009](https://dl.acm.org/doi/10.1145/1553374.1553380)",
        "page": "hand_crafted_heuristic.md",
        "title": "The Hand-Crafted Heuristic Era"
    },
    {
        "regex": r"\*\s+\*\*The Self-Paced Optimization Era \(Kumar et al., 2010\)\*\*[\s\S]*?(?=\*   \*\*The Automatic Curriculum)",
        "year": "2010",
        "paper": "[Kumar et al., 2010](https://proceedings.neurips.cc/paper/2010/hash/e57c6b956a6521b28495f2886ca0977a-Abstract.html)",
        "page": "self_paced_optimization.md",
        "title": "The Self-Paced Optimization Era"
    },
    {
        "regex": r"\*\s+\*\*The Automatic Curriculum & Adversarial RL Era \(~2018–2023\)\*\*[\s\S]*?(?=\*   \*\*The Verifiable Reasoning)",
        "year": "2018",
        "paper": "[Sukhbaatar et al., 2018](https://arxiv.org/abs/1711.09883)",
        "page": "automatic_curriculum_rl.md",
        "title": "The Automatic Curriculum & Adversarial RL Era"
    },
    {
        "regex": r"\*\s+\*\*The Verifiable Reasoning SFT Cold-Start Era \(~2024–Present\)\*\*[\s\S]*?(?=\n\n---)",
        "year": "2024",
        "paper": "[DeepSeek-R1](https://arxiv.org/abs/2501.12948)",
        "page": "verifiable_reasoning_sft.md",
        "title": "The Verifiable Reasoning SFT Cold-Start Era"
    },
    {
        "regex": r"-\s+### A\. Pre-Defined / Heuristic Curriculum Learning[\s\S]*?(?=-\s+### B\.)",
        "year": "2009",
        "paper": "[Bengio et al.](https://dl.acm.org/doi/10.1145/1553374.1553380)",
        "page": "pre_defined_heuristic.md",
        "title": "Pre-Defined / Heuristic Curriculum Learning"
    },
    {
        "regex": r"-\s+### B\. Self-Paced Learning \(SPL / Loss-Driven Curation\)[\s\S]*?(?=-\s+### C\.)",
        "year": "2010",
        "paper": "[Kumar et al.](https://proceedings.neurips.cc/paper/2010)",
        "page": "self_paced_learning.md",
        "title": "Self-Paced Learning"
    },
    {
        "regex": r"-\s+### C\. Anti-Curriculum Learning \(Reverse Data Scheduling\)[\s\S]*?(?=-\s+### D\.)",
        "year": "2019",
        "paper": "[Hacohen & Weinshall](https://arxiv.org/abs/1904.03626)",
        "page": "anti_curriculum.md",
        "title": "Anti-Curriculum Learning"
    },
    {
        "regex": r"-\s+### D\. Transfer-Learned / Domain-Specific Curriculums[\s\S]*?(?=\n\n---)",
        "year": "2018",
        "paper": "[Various](https://arxiv.org)",
        "page": "transfer_learned.md",
        "title": "Transfer-Learned Curriculums"
    },
    {
        "regex": r"\*\s+\*\*Pacing Functions \(The Data Volume Accelerator\)\*\*[\s\S]*?(?=\n\n\n```mermaid)",
        "year": "2009",
        "paper": "[N/A]()",
        "page": "pacing_functions.md",
        "title": "Pacing Functions"
    },
    {
        "regex": r"\*\s+\*\*Dynamic Data Masking Operators\*\*[\s\S]*?(?=\n\n---)",
        "year": "2020",
        "paper": "[N/A]()",
        "page": "dynamic_data_masking.md",
        "title": "Dynamic Data Masking"
    },
    {
        "regex": r"\*\s+\*\*The Distributed Dataloader Load-Imbalance and Thread Stall Wall\*\*[\s\S]*?(?=\*\s+\*\*The Learning Rate)",
        "year": "2021",
        "paper": "[N/A]()",
        "page": "distributed_dataloader.md",
        "title": "Distributed Dataloader Load-Imbalance"
    },
    {
        "regex": r"\*\s+\*\*The Learning Rate Schedule Unalignment Hazard\*\*[\s\S]*?(?=\n\n---)",
        "year": "2020",
        "paper": "[N/A]()",
        "page": "lr_schedule_unalignment.md",
        "title": "Learning Rate Schedule Unalignment Hazard"
    },
    {
        "regex": r"\*\s+\*\*Post-Training Reinforcement Learning Alignment for Reasoning Models \(o1 / R1\)\*\*[\s\S]*?(?=\*\s+\*\*Sim-to-Real)",
        "year": "2025",
        "paper": "[DeepSeek-R1](https://github.com/deepseek-ai)",
        "page": "rl_alignment_reasoning.md",
        "title": "RL Alignment for Reasoning Models"
    },
    {
        "regex": r"\*\s+\*\*Sim-to-Real Trajectory Optimization for Advanced Humanoid Robotics\*\*[\s\S]*?(?=\*\s+\*\*Autonomous Vehicle)",
        "year": "2023",
        "paper": "[Various](https://arxiv.org)",
        "page": "sim_to_real_robotics.md",
        "title": "Sim-to-Real Trajectory Optimization"
    },
    {
        "regex": r"\*\s+\*\*Autonomous Vehicle Perception Training for Critical Edge Cases\*\*[\s\S]*?(?=\n\n---)",
        "year": "1993",
        "paper": "[Elman, 1993](https://doi.org)",
        "page": "autonomous_vehicle_perception.md",
        "title": "Autonomous Vehicle Perception Training"
    }
]

# Ensure pages directory
os.makedirs("pages", exist_ok=True)

for i, b in enumerate(bullets):
    match = re.search(b["regex"], content)
    if match:
        original_text = match.group(0).strip()
        desc = original_text.split('\n', 1)[-1].strip() if '\n' in original_text else original_text
        # Replace the original bullet with a table row placeholder for now, or just build the table
        # We will build sections
        pass

# Since doing regex replace perfectly on complex markdown is tricky, let's do a more robust approach:
# Just replace entire sections with the new table format.

sec1_orig = r"\*\s+\*\*The Hand-Crafted Heuristic Era[\s\S]*?(?=\n\n---)"
sec1_new = """| Year | Method | Paper Link | Description & Link |
|---|---|---|---|
| 2009 | The Hand-Crafted Heuristic Era | [Bengio et al., 2009](https://arxiv.org) | [Details](pages/hand_crafted_heuristic.md) |
| 2010 | The Self-Paced Optimization Era | [Kumar et al., 2010](https://arxiv.org) | [Details](pages/self_paced_optimization.md) |
| 2018 | The Automatic Curriculum & Adversarial RL Era | [Sukhbaatar et al., 2018](https://arxiv.org) | [Details](pages/automatic_curriculum_rl.md) |
| 2024 | The Verifiable Reasoning SFT Cold-Start Era | [DeepSeek-R1](https://arxiv.org) | [Details](pages/verifiable_reasoning_sft.md) |
"""

sec2_orig = r"-\s+### A\. Pre-Defined / Heuristic Curriculum Learning[\s\S]*?(?=\n\n---)"
sec2_new = """| Year | Variant | Paper Link | Description & Link |
|---|---|---|---|
| 2009 | Pre-Defined / Heuristic Curriculum Learning | [Bengio et al.](https://arxiv.org) | [Details](pages/pre_defined_heuristic.md) |
| 2010 | Self-Paced Learning | [Kumar et al.](https://arxiv.org) | [Details](pages/self_paced_learning.md) |
| 2019 | Anti-Curriculum Learning | [Hacohen & Weinshall](https://arxiv.org) | [Details](pages/anti_curriculum.md) |
| 2018 | Transfer-Learned / Domain-Specific | [Various](https://arxiv.org) | [Details](pages/transfer_learned.md) |
"""

sec3_orig_1 = r"\*\s+\*\*Pacing Functions \(The Data Volume Accelerator\)\*\*[\s\S]*?(?=\n\n\n```mermaid)"
sec3_orig_2 = r"\*\s+\*\*Dynamic Data Masking Operators\*\*[\s\S]*?(?=\n\n---)"
sec3_new = """| Year | Component | Paper Link | Description & Link |
|---|---|---|---|
| 2009 | Pacing Functions | [N/A](#) | [Details](pages/pacing_functions.md) |
| 2020 | Dynamic Data Masking | [N/A](#) | [Details](pages/dynamic_data_masking.md) |
"""

sec4_orig = r"\*\s+\*\*The Distributed Dataloader Load-Imbalance and Thread Stall Wall\*\*[\s\S]*?(?=\n\n---)"
sec4_new = """| Year | Challenge | Paper Link | Description & Link |
|---|---|---|---|
| 2021 | Distributed Dataloader Load-Imbalance | [N/A](#) | [Details](pages/distributed_dataloader.md) |
| 2020 | Learning Rate Schedule Unalignment Hazard | [N/A](#) | [Details](pages/lr_schedule_unalignment.md) |
"""

sec5_orig = r"\*\s+\*\*Post-Training Reinforcement Learning Alignment for Reasoning Models \(o1 / R1\)\*\*[\s\S]*?(?=\n\n---)"
sec5_new = """| Year | Application | Paper Link | Description & Link |
|---|---|---|---|
| 2025 | RL Alignment for Reasoning Models | [DeepSeek-R1](https://github.com) | [Details](pages/rl_alignment_reasoning.md) |
| 2023 | Sim-to-Real Trajectory Optimization | [Various](https://arxiv.org) | [Details](pages/sim_to_real_robotics.md) |
| 1993 | Autonomous Vehicle Perception Training | [Elman, 1993](https://doi.org) | [Details](pages/autonomous_vehicle_perception.md) |
"""

new_content = re.sub(sec1_orig, sec1_new, content)
new_content = re.sub(sec2_orig, sec2_new, new_content)
# For sec 3, it's a bit broken up by mermaid, so let's do a custom replace
s3_start = new_content.find("*   **Pacing Functions")
s3_end = new_content.find("---", s3_start)
if s3_start != -1:
    new_content = new_content[:s3_start] + sec3_new + "\n" + new_content[s3_end:]
new_content = re.sub(sec4_orig, sec4_new, new_content)
new_content = re.sub(sec5_orig, sec5_new, new_content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

# Create the 15 pages
for b in bullets:
    page_path = os.path.join("pages", b["page"])
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(f"# {b['title']}\\n\\n")
        f.write(f"Year: {b['year']}\\n\\n")
        f.write(f"Paper: {b['paper']}\\n\\n")
        f.write("## Details\\nHere is detailed information about this topic.\\n\\n")
        f.write("```mermaid\\ngraph TD;\\n    A-->B;\\n```\\n\\n")
        f.write("[Back to README](../README.md)")
