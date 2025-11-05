import subprocess
import os
import sys

# Define paths
corpus_dir = "wav"
dictionary_path = "english_us_arpa"
acoustic_model_path = "english_us_arpa"
output_dir = "output"

# Optional clean flag
clean_flag = "--clean"

# Build the command
command = [
    "mfa",  # Use 'mfa' if MFA is installed via pip and added to PATH
    "align",
    corpus_dir,
    dictionary_path,
    acoustic_model_path,
    output_dir,
    clean_flag
]

# Run the command
try:
    print("Running Montreal Forced Aligner...")
    subprocess.run(command, check=True)
    print(f"✅ Alignment complete. Check the '{output_dir}/' folder for TextGrid files.")
except subprocess.CalledProcessError as e:
    print("❌ Alignment failed. Check your paths and model setup.")
    print("Error:", e)
    sys.exit(1)
except FileNotFoundError:
    print("❌ MFA executable not found. Make sure MFA is installed and added to your PATH.")
    sys.exit(1)
