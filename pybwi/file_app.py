import os
import subprocess
from tempfile import NamedTemporaryFile, TemporaryDirectory

from pydantic import BaseModel, Field

from opyrator.components.types import FileContent


class AudioSeparationInput(BaseModel):
    video_file: FileContent = Field(..., mime_type="video/mp4")


class AudioSeparationOutput(BaseModel):
    vocals_file: FileContent = Field(
        ...,
        mime_type="audio/mp3",
        description="The vocals (singing voice) extracted from the audio file.",
    )
    # accompaniment_file: FileContent = Field(
    #     ...,
    #     mime_type="audio/wav",
    #     description="The non-voice parts etracted from the audio file.",
    # )


def separate_audio(input: AudioSeparationInput) -> AudioSeparationOutput:
    """Separation of a music file to vocals (singing voice) and accompaniment.

    To try it out, you can use this example audio file: [audio_example.mp3](https://github.com/deezer/spleeter/raw/master/audio_example.mp3).
    """

    if subprocess.run(
          'which ffmpeg',shell=True).returncode != 0:
            raise Exception("FFMPEG is not installed")

    with NamedTemporaryFile(suffix=".mp3", mode="w+b") as local_video_file:
        print(f"Type of {type(input.video_file)} ({input.video_file.__class__.__bases__})")
        local_video_file.write(input.video_file.as_bytes())
        local_video_file.seek(0)
        #  Will delete on context exit
        print(f"File is: {local_video_file.name}")
        with TemporaryDirectory() as tmp_dir:
            vocals_file = os.path.join(tmp_dir, "sample.mp3")

            subprocess.run(
            f'ffmpeg -v error -i {local_video_file.name} -map 0:a  {vocals_file}'
            ,                shell=True,
            )


            with open(vocals_file, "rb") as f:
                vocals_bytes = f.read()

            return AudioSeparationOutput(
                vocals_file=vocals_bytes
            )
