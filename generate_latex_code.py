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
                r"\includegraphics[width=\textwidth]{" + \
                f"fig/{f}" + \
                "}" + "\n" +\
                "\caption{" + "\n" +\
                f"{f_without_end.replace('_', ' ')}" + "\n"+  \
                r"\textbf{A.}" + "\n" +\
                r"\textbf{B.}" + "\n" +\
                r"} " + "\n" \
                r"\label{fig:" +\
                f"{f_without_end}" +\
                r"}" + "\n" +\
                "\end{figure}\n" +\
                "\clearpage\n"

        print()
        print(code)


if __name__ == "__main__":
    main()