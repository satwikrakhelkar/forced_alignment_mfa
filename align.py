import subprocess
import os


corpus_dir = "wav"
dictionary = "english_us_arpa"
acoustic_model = "english_us_arpa"
output_dir = "output"


clean_flag = "--clean"


command = [
    "python", "-m", "montreal_forced_aligner",
    "align",
    clean_flag,
    corpus_dir,
    dictionary,
    acoustic_model,
    output_dir
]


try:
    print("Running Montreal Forced Aligner...")
    subprocess.run(command, check=True)
    print("Alignment complete. Check the 'output/' folder for TextGrid files.")
except subprocess.CalledProcessError as e:
    print("Alignment failed. Check your paths and model setup.")
    print("Error:", e)
