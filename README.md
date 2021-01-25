# Forced Alignment Wrapper

HTTP Server wrapped around a forced-alignment toolkit

Run the HTTP server:
```
docker build -t forced_alignment --build-arg IP=0.0.0.0 --build-arg PORT=5000 .
docker run -p 5000:5000 forced_alignment
```

Using Prosody Lab Phonetic Aligner:
```
docker run -v /shared:/shared -it --entrypoint bash forced_alignment
git clone http://github.com/prosodylab/Prosodylab-Aligner
pip3 install -r requirements.txt
python3 -m aligner --help
```
