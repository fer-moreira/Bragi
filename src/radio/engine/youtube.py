import yt_dlp
import json

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
            return self.extractor.extract_info(
                target, 
                download=False
            )
        except Exception as r:
            return {}

    def get_formats(self, target):
        return self.get_info(target).get("formats", [])
    
    def get_audios(self, target):
        try:
            formats = self.get_formats(target)
            
            formats = [
                format 
                for format in formats
                if format.get("resolution", "none") == "audio only"
            ]
            
            return formats
        except:
            return []

    def extract_bestaudio_url(self, target):
        try:
            audios = self.get_audios(target)
            best_audio = None
            
            if audios and len(audios) > 0:
                best_audio = audios[0]
                
            return best_audio["url"]
        except:
            raise
