import csv

if __name__ == '__main__':
    file_name = "dataset.csv"
    with open(file_name, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        out = open(file_name.split('.')[0] + "_vectors.txt", "w")

        # load all docs into in-mem list
        # where each element is a list of [doc_id,line]
        docs = []

        # transfer content of a file into a list of lines
        lines = [line for line in csv_reader]

        for line in lines:
            for i in range(len(line)):
                if (i>0):
                    out.write(line[i] + '\t')
            out.write('\n')

    csv_file.close()