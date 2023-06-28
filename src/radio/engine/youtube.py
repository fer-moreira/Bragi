import yt_dlp
import json
import logging

logger = logging.getLogger("discord.py")


class YoutubeExtractor:
    def __init__(self) -> None:
        self.options = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "nocheckcertificate": True,
            "ignoreerrors": False,
            "logtostderr": False,
            "quiet": True,
            "no_warnings": True,
            "default_search": "auto",
            "source_address": "0.0.0.0",
        }
        self.extractor = yt_dlp.YoutubeDL(self.options)

    def get_info(self, target):
        try:
            info = self.extractor.extract_info(
                target,
                download=False
            )
            return info
        except Exception as r:
            return {}

    def get_formats(self, info):
        return info.get("formats", [])

    def get_audios(self, info):
        try:
            formats = self.get_formats(info)
            formats = [
                format
                for format in formats
                if "audio" in format.get("format")
            ]
            return formats
        except:
            return []

    def extract_song_data(self, target):
        info = self.get_info(target)
        
        audios = [
            audio 
            for audio in self.get_audios(info) 
            if audio.get("ext") == "mp4"
        ]
        
        if not audios:
            return {}
        
        if len(audios) > 0: 
            best_audio = audios[0]
        else: best_audio = audios

        return {
            "url"       : best_audio.get("url", None),
            "title"     : info.get("title", None),
            "thumbnail" : info.get("thumbnail", None)
        }
