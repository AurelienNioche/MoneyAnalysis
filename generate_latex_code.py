from os import listdir
from os.path import isfile, join


def main():
    my_path = "fig/sup"

    onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    onlyfiles.sort()

    for f in onlyfiles:

        f_without_end = f.split(".")[0]

        code = r"\begin{figure}[htpb]" + "\n" +\
                "\centering" + "\n" +\
                "\includegraphics[width=\textwidth]{" + \
                f"fig/{f}" + \
                "}" + "\n" +\
                "\caption{" + "\n" +\
                f"{f_without_end}" + \
                r"\textbf{A.}" + "\n" +\
                r"\textbf{B.}" + "\n" +\
                r"} " \
                r"\label{fig:" + "\n" +\
                f"{f_without_end}" + "\n" +\
                r"}" + "\n" +\
                "\end{figure}"

        print()
        print(code)


if __name__ == "__main__":
    main()