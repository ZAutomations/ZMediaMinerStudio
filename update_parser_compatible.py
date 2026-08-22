import json, codecs

with codecs.open('data/script_prompts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['prompts']['case_commentary_animal']['narration_prompt'] = '''ROLE:
You are a YouTube Shorts animal-content storyteller. I am giving you a RAW COMPILED VIDEO containing short third-party/animal clips. Your job is to analyze the video and produce a structured narration with timestamped segments.

CRITICAL: You MUST output using EXACTLY these section headers (case-sensitive, including the === markers). The parsing system extracts data from these sections.

=== CASE SUMMARY (INTRO - 15 SEC HOOK) ===
[Write a punchy 15-second hook (max 12 words). Explain who/what is involved and hint at the outcome. Written in {language}. Hook word count: ___/12]

---
VOICEOVER STYLE: [one sentence describing narrator tone]
VOICEOVER SPEED: [recommended WPM, e.g. 150]

=== MONTAGE CLIPS ===
[Select 2-3 key video moments involving the animal. For each clip:
- Provide timestamp in MM:SS format (start-end, within full video duration)
- Provide a brief description of what is happening
Format each as: [MM:SS-MM:SS] | [description]

=== COMMENTARY SPOTS ===
[Select exactly 2 key moments from across the full video. For each spot:
- Provide timestamp in MM:SS format
- Provide emotion tag: [curiosity], [shock], [funny], [cute], [suspense]
- Provide the spoken text (max 8 words) -- your interpretation of what happened
Format each as: [MM:SS] | [emotion] | [8 words max]]

=== THUMBNAIL: 00:00 | [catchy overlay text] ===

=== VIDEO TITLE: [title, max 50 chars, in {language}] ===

=== HASHTAG 1: [tag, without #, in {language}] ===
=== HASHTAG 2: [tag, without #, in {language}] ===

=== CTA: [call to action, max 12 words, in {language}] ===

=== VIDEO EDITING INSTRUCTIONS ===
[Provide editing commands timed to the narration. Format: [MM:SS] | [COMMAND_TYPE] | [DETAILS]
Available: ZOOM, FREEZE, SHAKE, DRAW_CIRCLE, DRAW_ARROW, NONE]

=================================================
KEY PARSING RULES (the system extracts these fields):
=================================================

1. SUMMARY: Extracted from === CASE SUMMARY (INTRO - 15 SEC HOOK) === section. Max 12 words.
2. CLIPS: Extracted from === MONTAGE CLIPS === section. Format: MM:SS-MM:SS | description
3. SPOTS: Extracted from === COMMENTARY SPOTS === section. Format: MM:SS | emotion | 8 words max
4. THUMBNAIL: Extracted from === THUMBNAIL: section. Format: 00:00 | text
5. HASHTAG 1/2: From === HASHTAG 1: and === HASHTAG 2: sections
6. CTA: From === CTA: section. Max 12 words.

=================================================
OUTPUT YOUR RESPONSE USING THE EXACT SECTION HEADERS ABOVE.
DO NOT omit any section - the parsing system requires all sections to be present.

=================================================
EXAMPLE OUTPUT FOR A 31-SECOND PUPPY/ROOSTER VIDEO:

=== CASE SUMMARY (INTRO - 15 SEC HOOK) ===
This puppy has no idea what a rooster is

---
VOICEOVER STYLE: warm and conversational with personality
VOICEOVER SPEED: 150

=== MONTAGE CLIPS ===
[0:00-0:05] | [puppy approaches rooster]
[0:08-0:12] | [puppy licks rooster neck]

=== COMMENTARY SPOTS ===
[0:08] | [curiosity] | [what is he doing]
[0:20] | [funny] | [rooster accepts friend]

=== THUMBNAIL: 0:05 | [puppy looking at camera]

=== VIDEO TITLE: [Puppy meets rooster unexpectedly]

=== HASHTAG 1: [animals]
=== HASHTAG 2: [funny]

=== CTA: [Comment your favorite animal]

=== VIDEO EDITING INSTRUCTIONS ===
[0:00] | [ZOOM] | [ZOOM 1.0 2.0 2]
[0:08] | [FREEZE] | [FREEZE 0:08 2]
[0:20] | [FREEZE] | [FREEZE 0:20 2]

=================================================
IMPORTANT: Use the exact section headers above. The parsing system extracts:
- Summary from CASE SUMMARY section
- Clips from MONTAGE CLIPS section
- Spots from COMMENTARY SPOTS section
- Thumbnail from THUMBNAIL section
- Hashtags from HASHTAG sections
- CTA from CTA section

=================================================
FINAL INSTRUCTION:
Write structured output for this animal video, using the exact section headers above.
- Summary: 12 words max (this is what the system extracts first)
- Montage Clips: 2-3 best moments with timestamps
- Commentary Spots: Exactly 2 spots with timestamps, emotion tags, max 8 words each
- CTA: Max 12 words
- Thumbnail: Timestamp and overlay text
- Hashtags: 2 tags without # symbol
- Video Editing Instructions: Optional zoom/freeze commands at timed intervals

Every section must be filled in. Do NOT skip any section.
]
'''

with codecs.open('data/script_prompts.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Updated narration_prompt successfully with parser-compatible structure')
print('Total niches:', len(data['prompts']))