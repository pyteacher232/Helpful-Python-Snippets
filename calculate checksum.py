import hashlib
import glob

def get_checksum(fname):

    md5_hash = hashlib.md5()
    with open(fname, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()


def compare_checksums(self, full_csv_fname):
    print(f"[compare_checksums] full_csv_fname: {full_csv_fname}")
    backup_csv_files = glob.glob(f"{self.backup_dir}\\EOD_partial_*.csv")
    backup_csv_files.sort()

    if len(backup_csv_files) > 0:
        prev_file_checksum = get_checksum(backup_csv_files[-1])
        curr_file_checksum = get_checksum(full_csv_fname)

        if prev_file_checksum == curr_file_checksum:
            print(f"\tDone.")
            return True
        else:
            print(f"\tDone.")
            return False
    else:
        print(f"\tDone.")
        return False