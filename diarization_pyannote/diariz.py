"""
MIT License

Copyright (c) 2020 CNRS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pyannote.audio import Pipeline

AUDIO_PATH = "" # Replace with your input file
DIARIZ_PATH = "" # Replace with your output file

print("Getting pipeline...")
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token="---token---") # Replace with your token

print("Getting diarization from pipeline...")
diarization = pipeline(AUDIO_PATH)

print("Produce diarization file...")
text = ""
for turn, _, speaker in diarization.itertracks(yield_label=True):
    text += f'{speaker}:{turn.start}:{turn.end}\n'
    
with open(file=DIARIZ_PATH, encoding='utf-8', mode='w') as w_file:
    w_file.write(text)