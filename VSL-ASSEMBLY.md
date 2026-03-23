# VSL Video Assembly Instructions

## What You Have

✅ **15 Slide Images** (`slides/slide-00.png` through `slide-14.png`)  
✅ **VSL Audio** (`vsl-audio.mp3`, 1.35 MB, Chad's voice)  
✅ **VSL Script** (`vsl-script.txt`)

## Option 1: Use Descript (Easiest, 5 minutes)

1. **Open Descript** (free: https://www.descript.com)
2. **Create new project** → Video Project
3. **Import audio:** Drag `vsl-audio.mp3` into timeline
4. **Add slides:**
   - Click "Media" → "Import"
   - Select all 15 slides (slide-00.png to slide-14.png)
   - Drag them into timeline in order
5. **Adjust timing:**
   - Audio is ~4 minutes 30 seconds
   - Each slide should show ~18 seconds (270 seconds / 15 slides)
   - Descript will auto-adjust, or you can manually set duration
6. **Export:**
   - Click "Publish" → "Export" → "Video"
   - Resolution: 1080p
   - Format: MP4
   - Export!

**Time:** 5 minutes  
**Cost:** Free

---

## Option 2: Use CapCut (Free, 10 minutes)

1. **Download CapCut** (free: https://www.capcut.com)
2. **Create new project** → 16:9 ratio
3. **Import media:**
   - Click "Import" → Select all 15 slides + audio file
4. **Add to timeline:**
   - Drag audio to audio track
   - Drag slides to video track in order (slide-00 first, slide-14 last)
5. **Adjust slide duration:**
   - Select all slides
   - Set duration: 18 seconds each (or auto-fit to audio length)
6. **Export:**
   - Click "Export" → 1080p 60fps → Export
   - Save as `vsl-video.mp4`

**Time:** 10 minutes  
**Cost:** Free

---

## Option 3: Use Online Tool (No Download, 5 minutes)

**Kapwing** (https://www.kapwing.com/tools/add-audio-to-video)

1. Go to Kapwing
2. Upload all 15 slides
3. Upload vsl-audio.mp3
4. Arrange slides in sequence
5. Set each slide duration to ~18 seconds
6. Export MP4

**Time:** 5 minutes  
**Cost:** Free (with watermark), $16/month to remove watermark

---

## Option 4: Use ffmpeg (Command Line, Advanced)

If you have ffmpeg installed:

```bash
# Create concat list
cd slides
(for %i in (*.png) do @echo file '%i' & @echo duration 18) > concat.txt

# Create video
ffmpeg -f concat -safe 0 -i concat.txt -i ../vsl-audio.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest ../vsl-video.mp4
```

---

## Slides Content Summary

1. **Slide 00:** "YOU'RE SPENDING 10 HOURS / PER WEEK EDITING VIDEOS"
2. **Slide 01:** "HERE'S WHY YOU / CAN'T GROW FASTER"
3. **Slide 02:** "YOU'VE HEARD ABOUT / AI VIDEO EDITING"
4. **Slide 03:** "WHAT IF AI DID / 70% OF THE WORK?"
5. **Slide 04:** "THE 70/30 RULE / AI EDITING FRAMEWORK"
6. **Slide 05:** "6 POWERFUL MODULES / COMPLETE TRAINING SYSTEM"
7. **Slide 06:** "YOU DON'T NEED / EXPENSIVE SOFTWARE"
8. **Slide 07:** "YOUR FIRST 7 DAYS / RAPID TRANSFORMATION"
9. **Slide 08:** "THE RESULTS / EXPONENTIAL GROWTH"
10. **Slide 09:** "WHO THIS IS FOR / CONTENT CREATORS"
11. **Slide 10:** "WHAT'S INCLUDED / EVERYTHING YOU NEED"
12. **Slide 11:** "$297 ONE-TIME / OR 3 PAYMENTS OF $99"
13. **Slide 12:** "30-DAY GUARANTEE / ZERO RISK"
14. **Slide 13:** "THE CHOICE / IS YOURS"
15. **Slide 14:** "GET INSTANT ACCESS / ENROLL NOW"

---

## After Creating Video

1. **Upload to Vimeo/YouTube** (unlisted)
2. **Get embed code**
3. **Update sales page:**
   - Replace `[VSL VIDEO COMING IN STAGE 4]` placeholder
   - Add embed code in hero section
4. **Test playback** on sales page

---

## Recommended: Descript

**Why:** Free, fastest, perfect for this use case, same tool students will learn in the course.

**Next Steps:**
1. Download Descript
2. Follow "Option 1" above
3. Export as `vsl-video.mp4`
4. Upload to hosting (Vimeo recommended)
5. Embed on sales page

**Total time:** ~10 minutes including download
