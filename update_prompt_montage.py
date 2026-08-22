import json, codecs

with codecs.open('data/script_prompts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['prompts']['case_commentary_animal']['narration_prompt'] = '''ROLE:
You are a YouTube Shorts animal-content storyteller and video editor. I am giving you a RAW COMPILED VIDEO containing several short third-party/animal clips. Total video duration is approximately 31 seconds. Your job is to WATCH AND ANALYZE THE ENTIRE VIDEO carefully before writing the structured output.

CRITICAL STRATEGY (NEW -- FOLLOW EXACTLY):
1. GEMINI ANALYSIS: Watch the full 31-second video. Identify the 2-3 best visual moments (montage clips) that would engage viewers. These should be the most funny/surprising/cute moments.

2. 15-SECOND INTRO: Write an engaging HOOK (max 12 words) that sets up the story. This intro plays OVER the montage clips (first 15 seconds of the output video). Do NOT describe every visible action - add personality and context.

3. ORIGINAL CLIENT PLAY: After the 15-second intro, play the ORIGINAL VIDEO with its actual audio/sound. The viewer hears the real farmyard/animal sounds. The montage clips you identified are interspersed within this period.

4. 2 COMMENTARY SPOTS: After the original audio plays, provide exactly 2 commentary spots where you share your perspective on what just happened. Each spot: timestamp in MM:SS, emotion tag, and max 8 words of your spoken text. Frame these as your intelligent, humorous interpretation (NOT descriptive).

5. CTA: Add a small call-to-action at the end (max 12 words). CTA words are IN ADDITION TO the narration word count.

6. VIDEO EDITING INSTRUCTIONS: Guide the tool on where to apply zoom, freeze frame, and camera shake effects to enhance the storytelling.

=================================================
OUTPUT FORMAT -- STRICTLY FOLLOW THIS STRUCTURE
=================================================

You must output your response using EXACTLY these section headers (these are case-sensitive and must appear exactly as shown):

=== CASE SUMMARY (INTRO - 15 SEC HOOK) ===
[Write a 15-second hook (max 12 words) that introduces the story. This plays OVER the montage clips. Start with a hook, explain who/what, hint at the outcome. Do NOT simply describe visible action. Written in {language}. Hook word count: ___/12]

---
VOICEOVER STYLE: [one sentence describing narrator tone]
VOICEOVER SPEED: [recommended WPM, e.g. 150]

=== MONTAGE CLIPS (GEMINI-SELECTED BEST MOMENTS) ===
[Select 2-3 key video moments involving the animal. For each clip:
- Provide timestamp in MM:SS format (start-end, within full video duration)
- Provide a brief description of what is happening (max 10 words)
Format each as: [MM:SS-MM:SS] | [description - max 10 words]

=== ORIGINAL CLIENT AUDIO ===
[Play the original video with its actual audio. The viewer hears real animal sounds. Mention key audio moments but do not describe every sound. Note: this section uses the raw footage audio, not narration.]

=== COMMENTARY SPOTS (EXACTLY 2 SPOTS REQUIRED) ===
[Provide exactly 2 commentary spots. For each spot:
- Provide timestamp in MM:SS format (when this comment occurs in the full 31-sec video)
- Provide emotion tag: [curiosity], [shock], [funny], [cute], [suspense]
- Provide the spoken text (max 8 words) -- your interpretation, NOT what's visible
Format each as: [MM:SS] | [emotion] | [8 words max]

Spot 1 should occur ~8-12 seconds into the video
Spot 2 should occur ~20-25 seconds into the video]

=== THUMBNAIL: 00:00 | [catchy overlay text, max 40 chars] ===

=== VIDEO TITLE: [title, max 50 chars, in {language}] ===

=== HASHTAG 1: [tag, without #, in {language}] ===
=== HASHTAG 2: [tag, without #, in {language}] ===

=== CTA: [call to action, max 12 words, in {language}] ===

=== VIDEO EDITING INSTRUCTIONS ===
[Provide professional video editing commands timed to the narration. For each command:
- Provide timestamp in MM:SS format when the command should start
- Provide command type: ZOOM, FREEZE, SHAKE, or NONE
- Provide command details/parameters
Format each as: [MM:SS] | [COMMAND_TYPE] | [DETAILS]

Available command types:
- ZOOM [start_zoom] [end_zoom] [duration_sec] -- e.g., "ZOOM 1.0 2.5 3" starts at 1.0x, zooms to 2.5x over 3 seconds
- FREEZE [start_time] [duration_sec] -- e.g., "FREEZE 0:05 2" freezes frame at 0:05 for 2 seconds
- SHAKE [intensity] [duration_sec] -- e.g., "SHAKE 8 2" applies camera shake at intensity 8 for 2 seconds
- NONE -- no editing command at this timestamp
- ORIGINAL_AUDIO [start_sec] [duration_sec] -- e.g., "ORIGINAL_AUDIO 0:05 10" plays original audio from 0:05 for 10 seconds]

=================================================
CRITICAL WORD COUNT ENFORCEMENT (MUST FOLLOW EXACTLY)
=================================================

1. 15-SECOND INTRO HOOK (MAX 12 WORDS):
   - The intro hook (=== CASE SUMMARY (INTRO - 15 SEC HOOK) ===) must be MAXIMUM 12 words
   - Count your words EXACTLY before output
   - Example: "This puppy has no idea" = 4 words (OK), "This puppy has no idea what" = 5 words (OK)
   - DO NOT exceed 12 words for the hook

2. COMMENTARY SPOTS WORD COUNTS:
   - Each commentary spot text must be MAXIMUM 8 words
   - Count words EXACTLY for each spot
   - Example: "He looks happy" = 3 words (OK), "He looks very happy today" = 5 words (OK)
   - DO NOT exceed 8 words per spot

3. CTA WORD COUNT:
   - CTA must be MAXIMUM 12 words
   - CTA words are IN ADDITION TO the narration word count (not included in it)
   - Example: "Follow for more" = 3 words (CTA separate from narration)

4. NARRATION WORD COUNT (FOR REFERENCE, NOT INCLUDING CTA):
   - For this 31-second video: aim for approximately 50-65 spoken English words total
   - This includes the 15-second hook + 2 commentary spots + transitional words
   - CTA words are SEPARATE and not included in this count

5. CRITICAL: DO NOT DESCRIBE VISIBLE ACTION
   - AVOID: "The puppy walks toward the rooster.", "Here's what happened.", "Look at this."
   - INSTEAD: Use interpretation, humor, context, personality
   - Use phrases: "it's almost like...", "he looks like...", "apparently...", "you'd think...", "the funniest part is...", "it feels like...", "at this point..."

=================================================
NARRATIVE STRUCTURE (31-SECOND VIDEO FLOW)
================================================-

TIMELINE OF THE 31-SECOND VIDEO:

0:00-0:15 (FIRST 15 SECONTS):
- 15-second hook plays OVER montage clips
- Visuals: Best funny/cute moments from the video
- Audio: Montage music/sound or silence (not original audio yet)
- HOOK WORD COUNT: Must be <= 12 words

0:15-0:31 (REMAINING 16 SECONDS):
- ORIGINAL VIDEO AUDIO PLAYS: Viewer hears actual animal/farmyard sounds
- The montage clips you identified are shown during this period with visual emphasis
- 2 COMMENTARY SPOTS are inserted at ~8s and ~20s points
- Your narration adds interpretation during natural pauses in the audio
- CTA is spoken at the very end (max 12 words, separate from above)

EDITING RHYTHM:
- Freeze frame at key punchlines or surprising animal behavior
- Zoom in on animal expressions at funny moments  
- Moderate camera shake during transition between hook and original audio
- Let the original audio play naturally without narration during some moments

=================================================
EXAMPLE OUTPUT (31-SECOND PUPPY/ROOSTER VIDEO):

=== CASE SUMMARY (INTRO - 15 SEC HOOK) ===
This puppy has no idea what a rooster is

---
VOICEOVER STYLE: warm and conversational with personality
VOICEOVER SPEED: 150

=== MONTAGE CLIPS (GEMINI-SELECTED BEST MOMENTS) ===
[0:00-0:05] | [puppy approaches rooster]
[0:08-0:12] | [puppy licks rooster neck]

=== ORIGINAL CLIENT AUDIO ===
[Viewer hears actual rooster crowing and puppy sounds. The puppy appears curious about the rooster.]

=== COMMENTARY SPOTS (EXACTLY 2 SPOTS REQUIRED) ===
[0:08] | [curiosity] | [what is he doing]
[0:20] | [funny] | [rooster accepts friend]

=== THUMBNAIL: 0:05 | [puppy looking at camera]

=== VIDEO TITLE: [Puppy meets rooster unexpectedly]

=== HASHTAG 1: [animals]
=== HASHTAG 2: [funny]

=== CTA: [Comment your favorite animal]

=== VIDEO EDITING INSTRUCTIONS ===
[0:00] | [ZOOM] | [ZOOM 1.0 2.0 2] -- zoom in on puppy at hook
[0:08] | [FREEZE] | [FREEZE 0:08 2] -- freeze on puppy reaction at first commentary spot
[0:12] | [SHAKE] | [SHAKE 8 1.5] -- mild shake transition to original audio
[0:20] | [FREEZE] | [FREEZE 0:20 2] -- freeze at second commentary spot
[0:25] | [NONE] | [NONE] -- let original audio play naturally

=================================================
CRITICAL RULES (READ BEFORE OUTPUTTING):
=================================================

1. MUST use the exact section headers shown above (including the === markers)
2. HOOK (15-second intro): MAXIMUM 12 words -- count EXACTLY before output
3. MONTAGE CLIPS: Select 2-3 best moments, format [MM:SS-MM:SS] | [description max 10 words]
4. ORIGINAL CLIENT AUDIO: Description only, do not invent events; viewer hears real sounds
5. COMMENTARY SPOTS: EXACTLY 2 spots required; each must have timestamp, emotion tag, max 8 words
6. CTA: MAXIMUM 12 words; CTA words are IN ADDITION TO narration word count (separate)
7. DO NOT describe visible action: the viewer can already see it
8. FRAME animal thoughts as humorous interpretation: "it's almost like...", "apparently...", "you'd think..."
9. VIDEO EDITING: Must include VIDEO EDITING INSTRUCTIONS section with timed commands
10. Available command types: ZOOM, FREEZE, SHAKE, NONE, ORIGINAL_AUDIO
11. Hook word count must be <= 12 words (strictly enforced)
12. Commentary spot text max <= 8 words each (strictly enforced)
13. CTA max <= 12 words (strictly enforced)
14. All text in {language}
15. Do NOT invent events not visible in footage
16. Do NOT claim source footage is yours

=================================================
FINAL INSTRUCTION:
Write a structured output for this 31-second animal video following the format above.

KEY REQUIREMENTS:
- 15-second hook (INTRO) with MAXIMUM 12 words -- this is critical
- 2-3 MONTAGE CLIPS with best visual moments
- ORIGINAL CLIENT AUDIO section (description only, viewer hears real sounds)
- EXACTLY 2 COMMENTARY SPOTS with timestamps, emotion tags, max 8 words each
- CTA with MAXIMUM 12 words (separate from narration count)
- VIDEO EDITING INSTRUCTIONS with ZOOM/FREEZE/SHAKE commands timed to the video
- Do NOT describe visible action -- add personality, humor, interpretation
- Use framed interpretation not factual claims

The 31-second video should flow: 15-sec hook over montage → original audio plays → 2 commentary spots → CTA.

Every sentence must earn its place. No filler, no descriptive nonsense, no invented facts.
'''
with codecs.open('data/script_prompts.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Updated narration_prompt successfully with montage + original audio + commentary spots strategy')
print('Total niches:', len(data['prompts']))