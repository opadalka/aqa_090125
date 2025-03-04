from pathlib import Path

csv_file1_path = Path(__file__).parent / "random-michaels.csv"
csv_file2_path = Path(__file__).parent / "random.csv"
csv_result_file_path = Path(__file__).parent / "result_Padalka.csv"
check_duplicates1 = set()

#Read from file1 and write duplicates in set()1 and write not duplicates in a separate file1
with open(csv_file1_path, 'r', encoding="utf8") as in_file1, open(csv_result_file_path, 'w', encoding="utf8") as out_file: 
    for line in in_file1:
        if line in check_duplicates1: 
            continue 
        check_duplicates1.add(line)
        out_file.write(line)
# Read from file2 and write duplicates in set()1 and write not duplicates in a separate file1
with open(csv_file2_path, 'r', encoding="utf8") as in_file2, open(csv_result_file_path, 'w', encoding="utf8") as out_file: 
    for line in in_file2:
        if line in check_duplicates1: 
            continue 
        check_duplicates1.add(line)
        out_file.write(line)