

# read_sav_line_by_line.py

from savReaderWriter import SavReader
import pandas as pd
import os


def stream_and_save_chunks(sav_path, chunk_size=50000):
    out_dir = os.path.dirname(sav_path) or "."
    base_name = os.path.splitext(os.path.basename(sav_path))[0]

    with SavReader(sav_path) as reader:
        header = reader.header
        var_names = reader.varNames
        rows = []

        chunk_index = 1
        for i, row in enumerate(reader):
            rows.append(row)

            if (i + 1) % chunk_size == 0:
                df = pd.DataFrame(rows, columns=var_names)
                csv_path = os.path.join(
                    out_dir, f"{base_name}_part_{chunk_index}.csv")
                df.to_csv(csv_path, index=False)
                print(f"Saved: {csv_path}")
                rows = []
                chunk_index += 1

        # Save remaining
        if rows:
            df = pd.DataFrame(rows, columns=var_names)
            csv_path = os.path.join(
                out_dir, f"{base_name}_part_{chunk_index}.csv")
            df.to_csv(csv_path, index=False)
            print(f"Saved: {csv_path}")


if __name__ == "__main__":
    stream_and_save_chunks(
        "/Users/georgewangxi/Downloads/Cognitive Item - CY08MSP_STU_COG.SAV")
