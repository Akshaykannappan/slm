import urllib.request
import os

URL = "https://www.gutenberg.org/cache/epub/100/pg100.txt"

def download_dataset():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, "..", "dataset", "shakespeare.txt")

    if os.path.exists(dataset_path):
        print(f"Dataset already exists at {dataset_path}. Skipping download.")
        return

    print(f"Downloading dataset from {URL} ...")

    request = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; SLM-project/1.0)"}
    )

    with urllib.request.urlopen(request) as response:
        chunks = []
        while True:
            chunk = response.read(8192)  # read 8KB at a time
            if not chunk:
                break
            chunks.append(chunk)
        content = b"".join(chunks).decode("utf-8")

    with open(dataset_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Dataset saved to {dataset_path}")

if __name__ == "__main__":
    download_dataset()