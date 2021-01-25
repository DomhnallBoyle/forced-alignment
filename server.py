import argparse
import cherrypy
import json
import os
import shutil

from align import align

IP = '0.0.0.0'
PORT = 5005
CONFIG = {
    'global': {
        'server.socket_host': IP,
        'server.socket_port': PORT,
        'server.max_request_body_size': 0,  # no limit
        'server.socket_timeout': 60
    }
}
CURRENT_DIRECTORY = os.path.dirname(__file__)
TEMP_UPLOAD_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'temp_upload')


class ForcedAlignment(object):

    def __init__(self):
        self._setup_directories()

    def _setup_directories(self):
        if os.path.exists(TEMP_UPLOAD_DIRECTORY):
            shutil.rmtree(TEMP_UPLOAD_DIRECTORY)

        os.makedirs(TEMP_UPLOAD_DIRECTORY)

    @cherrypy.expose
    def index(self):
        return """
            <html>
                <title>Forced Alignment</title>
                <h2>Forced Alignment Upload:</h2>
                <p>Upload .wav audio and .txt transcript files</p>
                    
                <form action="upload" method="post" enctype="multipart/form-data">
                    Audio: <input type="file" name="audio"/><br/>
                    Transcript: <input type="file" name="transcript"/><br/><br/>
                    <input type="submit"/>
                </form>
            </html>
        """

    @cherrypy.expose
    def upload(self, audio, transcript):
        if not audio.file or not transcript.file:
            return json.dumps({'error': 'No audio or transcript file given.'})

        audio_file_path = self._read_file_stream(audio)
        transcript_file_path = self._read_file_stream(transcript)

        try:
            return align(wav_file_path=audio_file_path, transcript_file_path=transcript_file_path)
        except Exception as e:
            return json.dumps({'error': e})

    def _read_file_stream(self, file):
        upload_file_path = os.path.join(TEMP_UPLOAD_DIRECTORY, file.filename)

        with open(upload_file_path, 'wb') as out:
            while True:
                data = file.file.read(8192)

                if not data:
                    break

                out.write(data)

        return upload_file_path


def main(args):
    ip = args.ip
    port = args.port

    if ip != IP:
        CONFIG['global']['server.socket_host'] = ip

    if port != PORT:
        CONFIG['global']['server.socket_port'] = port

    cherrypy.quickstart(ForcedAlignment(), '/', CONFIG)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default=IP)
    parser.add_argument('--port', type=int, default=PORT)

    args = parser.parse_args()

    main(args)
