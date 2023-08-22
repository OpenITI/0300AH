import os

for fn in os.listdir("."):
    if fn.startswith("0298HadiIlaHaqqYahya.") and os.path.isdir(fn):
        folder_path = os.path.join(".", fn)
        for filename in os.listdir(folder_path):
            if filename.startswith("0298HadiIlaHaqqYahya."):
                fp = os.path.join(folder_path, filename)
                new_fp = os.path.join(folder_path, filename.replace("HadiIlaHaqq", "HadiIlaHaqqYahya"))
                os.rename(fp, new_fp)

for fn in os.listdir("."):
    if fn.startswith("0298HadiIlaHaqqYahya."):
        os.rename(fn, fn.replace("HadiIlaHaqq", "HadiIlaHaqqYahya"))
