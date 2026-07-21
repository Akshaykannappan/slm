"""Dataset configuration dictionary mapping dataset names to source URLs and filenames."""
import os

# Base directory for raw datasets
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

DATASETS = {
    "shakespeare": {
        "url": "https://www.gutenberg.org/cache/epub/100/pg100.txt",
        "raw_filename": "shakespeare.txt",
        "description": "The Complete Works of William Shakespeare (Project Gutenberg)",
    }
}
