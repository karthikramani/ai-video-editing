#!/usr/bin/env python3
"""
Simple VSL video creator using MoviePy
Creates video from slide images + audio
"""

try:
    from moviepy.editor import *
    import os
except ImportError:
    print("Installing moviepy...")
    import subprocess
    subprocess.run(["pip", "install", "moviepy"], check=True)
    from moviepy.editor import *
    import os

# Configuration
SLIDES_DIR = "slides"
AUDIO_FILE = "vsl-audio.mp3"
OUTPUT_FILE = "vsl-video.mp4"
SLIDE_DURATION = 20  # seconds per slide

def create_vsl():
    print("Creating VSL video...")
    
    # Get all slide images
    slides = sorted([os.path.join(SLIDES_DIR, f) for f in os.listdir(SLIDES_DIR) if f.endswith('.png')])
    print(f"Found {len(slides)} slides")
    
    # Load audio
    audio = AudioFileClip(AUDIO_FILE)
    total_duration = audio.duration
    print(f"Audio duration: {total_duration:.1f} seconds")
    
    # Calculate duration per slide
    slide_duration = total_duration / len(slides)
    print(f"Each slide will show for {slide_duration:.1f} seconds")
    
    # Create video clips from slides
    clips = []
    for slide_path in slides:
        clip = ImageClip(slide_path, duration=slide_duration)
        clips.append(clip)
    
    # Concatenate all slides
    video = concatenate_videoclips(clips, method="compose")
    
    # Add audio
    final_video = video.set_audio(audio)
    
    # Export
    print("Rendering video (this may take a few minutes)...")
    final_video.write_videofile(
        OUTPUT_FILE,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True,
        verbose=False,
        logger=None
    )
    
    # Get file size
    size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print(f"\n✅ VSL video created!")
    print(f"File: {OUTPUT_FILE}")
    print(f"Size: {size_mb:.2f} MB")
    print(f"Duration: {total_duration:.1f} seconds")

if __name__ == "__main__":
    create_vsl()
