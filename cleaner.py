import pandas as pd

def clean(filename, max_line):
    """filename(str): name of the txt file with the raw table"""
    """max_line(int): max number of glitches found in the raw table"""
    """sample call: clean("L1GDS-CALIB_STRAIN_Omicron_1135641617_1135728017.txt", 22)"""
    file = open(filename, "r")
    lines = file.readlines()
    values_raw = list()
    for l in lines:
        if l != '\n':
            l = l.strip()
            values_raw.append([token for token in l.split(" ") if token != ''])
    columns = list()
    values_clean = list()
    for v in values_raw:
        for num_str in [str(x) for x in range(max_line+1)]:
            if v[0] == num_str:
                v[0] = int(num_str)
                values_clean.append(v)
        if type(v[0]) == str:
            values_raw.remove(v)
            columns += [column for column in v if column != '\\']
    values_final = list()
    for num in range(max_line+1):
        fin = list()
        for v in values_clean:
            if v[0] == num:
                fin += v[1:]
        values_final.append(fin)

    df = pd.DataFrame(values_final, columns=columns)
    df.to_csv(filename.split(".txt")[0] + ".csv")


