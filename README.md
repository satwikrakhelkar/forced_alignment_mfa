Forced Alignment with Montreal Forced Aligner (MFA)

Objective:
This project implements a complete forced alignment pipeline using Montreal Forced Aligner (MFA).
It automatically aligns speech audio with its transcript at the word and phoneme level,
producing TextGrid files for phonetic analysis.

Environment Setup:
- OS: Windows 11
- Environment: Conda (PythonProject13)
- Tools: MFA, Praat, PyCharm

Folder Structure:
forced-alignment-mfa/
├── align.py
├── alignment_analysis.csv
├── Assignment1.pdf
├── wav/
│   ├── *.wav
│   ├── *.lab
├── output/
│   ├── *.TextGrid

Model Setup:
Run these commands in terminal to download models:
mfa model download dictionary english_us_arpa
mfa model download acoustic english_us_arpa

Alignment Script (align.py):
-----------------------------
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

Alignment Quality Summary:
--------------------------
File                               	Duration	Phone Dev	SNR  	Speech Log-Likelihood
F2BJRLP1                           	25.31    	3.89      	8.11 	-45.95
F2BJRLP2                           	28.65    	3.59      	7.89 	-45.83
F2BJRLP3                           	30.71    	3.66      	10.33	-46.88
ISLE_SESS0131_BLOCKD02_01_sprt1    	4.13     	2.72      	11.85	-52.37
ISLE_SESS0131_BLOCKD02_02_sprt1    	3.88     	2.53      	12.36	-50.91
ISLE_SESS0131_BLOCKD02_03_sprt1    	4.50     	3.88      	11.44	-53.55

Inspecting TextGrid Files:
Open each TextGrid file in Praat using:
- Open > Read from file…
- Select matching .wav and .TextGrid
- Click “View and Edit with Sound”

Report:
See Assignment1.pdf for:
- Project summary
- Sample alignment breakdown
- Alignment quality analysis
- Screenshots and conclusions

Submission Checklist:
- [x] Scripts and setup instructions
- [x] TextGrid outputs
- [x] Alignment analysis CSV
- [x] PDF report
- [x] Public GitHub repository

Status:
All assignment requirements satisfied.
Ready for submission and evaluation.
