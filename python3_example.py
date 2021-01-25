"""
Taken from https://github.com/jaekookang/p2fa_py3

Currently not working using a conda virtual environment
"""

from p2fa import align

# WAV_FILE_PATH = 'steve_jobs_example/steve_jobs.wav'
# TRANSCRIPT_FILE_PATH = 'steve_jobs_example/steve_jobs.txt'

# WAV_FILE_PATH = 'test/BREY00538.wav'
# TRANSCRIPT_FILE_PATH = 'test/BREY00538.txt'

WAV_FILE_PATH = 'beatles_example/beatles.wav'
TRANSCRIPT_FILE_PATH = 'beatles_example/beatles.txt'

phoneme_alignments, word_alignments = align.align(WAV_FILE_PATH, TRANSCRIPT_FILE_PATH)
