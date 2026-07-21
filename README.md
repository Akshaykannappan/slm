# Small Language Model (SLM)

A clean, modular repository for training and serving a custom transformer-based Small Language Model from scratch.

## Progress Summary

- **Overall Completion:** 1 / 84 steps complete (1.19%)
- **Current Step:** Phase 1 — Data & Tokenization: Step 2. Dataset Collection
- For the full step-by-step roadmap and details, see [PROGRESS.md](file:///Users/akshay/Documents/SLM/PROGRESS.md).

## Project Structure


```text
SLM/
├── configs/              # Hyperparameter configurations (model dimensions, LR, batch size)
├── data/                 # Dataset loading, cleaning, and tokenization
├── models/               # Transformer architecture components (attention, embeddings, blocks)
├── training/             # Training loops, optimizers, and checkpoint management
├── inference/            # Generation, sampling strategies (greedy, top-p, top-k), and decoding
├── tests/                # Unit tests mapping to the code structure
│   ├── test_data/
│   ├── test_models/
│   ├── test_training/
│   └── test_inference/
├── dataset/              # Raw and processed text data (git-ignored)
└── checkpoints/          # Saved model weights and optimizer states (git-ignored)
```

## Getting Started

### Prerequisites

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

### Next Steps

1. Configure hyperparameters in `configs/`.
2. Implement data preprocessing in `data/` and put raw files in `dataset/`.
3. Build the transformer architecture inside `models/`.
4. Run training script from `training/`.
5. Run evaluations and inference from `inference/`.
