import argparse
import os
import sys
import urllib.request

# Ensure project root is in sys.path when running script directly
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from configs.dataset_config import DATASETS, DATASET_DIR


def download_file(url: str, save_path: str) -> None:
    """Download a single file from url to save_path if it doesn't already exist."""
    if os.path.exists(save_path):
        print(f"Dataset already exists at {save_path}. Skipping download.")
        return

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    print(f"Downloading dataset from {url} ...")

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; SLM-project/1.0)"}
    )

    with urllib.request.urlopen(request) as response:
        chunks = []
        while True:
            chunk = response.read(8192)  # Read 8KB at a time
            if not chunk:
                break
            chunks.append(chunk)
        content = b"".join(chunks).decode("utf-8")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Dataset saved to {save_path}")


def download_dataset(dataset_key: str) -> None:
    """Download a single dataset specified by its key in DATASETS."""
    if dataset_key not in DATASETS:
        raise ValueError(
            f"Unknown dataset '{dataset_key}'. Available datasets: {list(DATASETS.keys())}"
        )
    info = DATASETS[dataset_key]
    save_path = os.path.join(DATASET_DIR, info["raw_filename"])
    download_file(info["url"], save_path)


def download_all_datasets() -> None:
    """Loop through all configured datasets and download them."""
    for key in DATASETS:
        print(f"--- Processing dataset: {key} ---")
        download_dataset(key)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download one or all datasets")
    parser.add_argument(
        "--dataset",
        type=str,
        default=None,
        help="Dataset key from configs/dataset_config.py. Omit to download ALL datasets."
    )
    args = parser.parse_args()

    if args.dataset is None:
        download_all_datasets()
    else:
        download_dataset(args.dataset)