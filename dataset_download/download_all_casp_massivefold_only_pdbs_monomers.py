
import csv
import os
import urllib.request
import sys

CSV_FILE = "casp_massivefold_files_only_pdbs_monomers.csv"
OUTPUT_DIR = "casp_massivefold_files_only_pdbs_monomers"

def download_with_progress(url, output_path):
    def show_progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = int(downloaded * 100 / total_size) if total_size > 0 else 0
        bar = '=' * (percent // 2) + ' ' * (50 - percent // 2)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()

    print(f"\nDownloading: {os.path.basename(output_path)}")
    urllib.request.urlretrieve(url, output_path, show_progress)
    print("\nDownload complete.")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row["File_name"]
            url = row["URL"]
            output_path = os.path.join(OUTPUT_DIR, filename)
            
            if os.path.exists(output_path):
                print(f"{filename} already downloaded, ignored.")
                continue
         
            try:
                download_with_progress(url, output_path)
            except Exception as e:
                print(f"\nError downloading {filename}: {e}")

if __name__ == "__main__":
    main()


