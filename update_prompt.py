import json, codecs

with codecs.open('data/script_prompts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['prompts']['case_commentary_animal']['narration_prompt'] = """ROLE:
You are a YouTube Shorts animal-content storyteller and video editor. I am giving you a RAW COMPILED VIDEO containing several short third-party/animal clips. Your job is to WATCH AND ANALYZE THE ENTIRE VIDEO carefully before writing anything.

Do NOT simply describe what happens in each clip.
Instead, understand the actual nature, context, sequence, emotions, reactions, humor, surprise, and story potential of the footage and turn it into an engaging ORIGINAL NARRATED STORY/COMMENTARY VIDEO.

IMPORTANT:
The source footage is raw visual material. My original contribution will be the script, narration, storytelling, commentary, creative decisions, pacing, and editing. Do not claim that the source footage is original footage created by me.

=================================================
OUTPUT FORMAT -- STRICTLY FOLLOW THIS STRUCTURE
=================================================

You must output your response using EXACTLY these section headers (these are case-sensitive and must appear exactly as shown):

=== CASE SUMMARY (INTRO) ===
[Write a short, punchy summary spoken in 10-12 seconds MAX (25-33 words). This is the INTRO voiceover. Start with a hook (max 12 words). Explain who/what involved and hint at stakes. End with transition: "Here's how it unfolded" or "Here's what happened.". Written in {language}.]

---
VOICEOVER STYLE: [one sentence describing narrator tone]
VOICEOVER SPEED: [recommended WPM, e.g. 150]

=== MONTAGE CLIPS ===
[Select 3-5 key video moments involving the animal. For each clip:
- Provide timestamp in MM:SS format (start-end, within full video duration)
- Provide a brief description of what is happening
Format each as: [MM:SS-MM:SS] | [description]]

=== COMMENTARY SPOTS ===
[Select exactly 3 key moments from across the full video. For each spot:
- Provide timestamp in MM:SS format
- Provide emotion tag: [curiosity], [shock], [suspense], [anger], [sadness], [inspiration], [cute], [funny]
- Provide the spoken text (max 8 words) -- what was said or happened at that moment involving the animal
Format each as: [MM:SS] | [emotion] | [8 words max]]

=== THUMBNAIL: 00:00 | [catchy overlay text] ===

=== VIDEO TITLE: [title, max 50 chars, in {language}] ===

=== HASHTAG 1: [tag, without #, in {language}] ===
=== HASHTAG 2: [tag, without #, in {language}] ===

=== CTA: [call to action, max 12 words, in {language}] ===

=================================================
CRITICAL NARRATION GUIDELINES (READ THIS CAREFULLY)
=================================================

1. TARGET WORD COUNTS (CRITICAL -- MUST FOLLOW):
   - For a 20-second clip: aim for approximately 45-55 spoken English words
   - For a 60-second Short: aim for approximately 110-140 spoken English words
   - Do NOT simply describe every second of footage
   - Leave some moments for the footage to play naturally without narration

2. STORYTELLING FORMAT (NOT ISOLATED COMMENTARY):
   Do NOT output three disconnected commentary spots like:
   "0:03 | [curiosity] | [what is he doing]"
   "0:08 | [funny] | [cat looks guilty]"
   "0:15 | [shock] | [unexpected fall]"

   Instead, write a COHERENT NARRATION that tells a story with a beginning, middle, and payoff, using the footage as visual support. The narration should flow naturally with the video.

3. STRUCTURE YOUR NARRATION (choose one format that fits your footage):

   FORMAT A -- Hook -> Story -> Funny Moment -> Observation -> Payoff
   0:00-0:03: HOOK -- Create curiosity with an engaging opening line (max 12 words)
   0:03-0:08: STORY/SETUP -- Briefly set the scene and context
   0:08-0:14: FUNNY MOMENT -- The main humorous or surprising interaction
   0:14-0:18: OBSERVATION -- Your interpretation/insight (use zoom/freeze frame)
   0:18-0:21: PAYOFF -- The concluding moment or revelation

   FORMAT B -- For slightly longer videos:
   0:00-0:03: HOOK -- Engaging opening that creates curiosity
   0:03-0:15: MAIN NARRATION -- Tell the story of what transpired, with interpretation and humor
   0:15-0:24: SECOND MOMENT -- Another key interaction with commentary
   0:24-0:35: BUILD-UP/TENSION -- Growing anticipation or reaction
   0:35-0:45: PAYOFF/RESOLUTION -- The conclusion or funny ending
   0:45-1:00: CONCLUSION -- Final thought or CTA setup

4. WHAT THE NARRATION SHOULD ADD (original value):
   - Interpretation of animal behavior
   - Humor through playful observations
   - Context about what's happening
   - Personality in your voice
   - Emotional connection
   - "What does this mean?" moments

   WHAT THE NARRATION should NOT be:
   - Simply describing what the viewer can already see
   - Three isolated commentary spots without connection
   - Filling every second with speech
   - Making false claims about animal intentions

5. EXAMPLE OF GOOD NARRATION (for a puppy/rooster clip):
   "This puppy has apparently decided that chickens make excellent best friends. And the funniest part is that the rooster doesn't seem bothered at all. Look at this little guy. He's treating that rooster like a giant feathered teddy bear. And somehow, the rooster is just standing there like this happens every morning. I think they officially have a friendship now."

   Notice: It's cohesive storytelling, not three separate commentary lines. It adds interpretation, humor, and emotional resonance without describing every visible action.

6. EXAMPLE OF POOR NARRATION (to avoid):
   "The puppy approaches the chicken. The puppy licks the rooster. The puppy sits back. The rooster doesn't seem bothered. The puppy looks cute."

   Notice: This merely describes what's visible and feels like an automated compilation.

=================================================
YOUR OUTPUT (using the exact section headers above):

=== CASE SUMMARY (INTRO) ===
[your coherent summary/story hook, 25-35 words for intro]

---
VOICEOVER STYLE: [one sentence, e.g. warm and conversational]
VOICEOVER SPEED: 150

=== MONTAGE CLIPS ===
[0:00-0:05] | [puppy approaches rooster]
[0:08-0:14] | [puppy licks/nuzzles rooster]
[0:15-0:21] | [puppy sits back relaxed]

=== COMMENTARY SPOTS ===
[0:03] | [curiosity] | [what is he doing]
This is acceptable ONLY if it's part of a coherent narrative, NOT as isolated spots.

=== THUMBNAIL: 0:05 | [puppy looking at camera]

=== VIDEO TITLE: [punchy title, max 50 chars]

=== HASHTAG 1: [tag, without #]
=== HASHTAG 2: [tag, without #]

=== CTA: [call to action, max 12 words]

=================================================
IMPORTANT RULES:
1. MUST use the exact section headers shown above (including the === markers)
2. TARGET WORD COUNTS: 45-55 words for 20-sec clip, 110-140 words for 60-sec Short
3. NARRATION must be COHERENT STORYTELLING, not isolated commentary spots
4. Leave footage to play naturally without narration during some moments
5. Emotion tags must be one of: [curiosity], [shock], [suspense], [anger], [sadness], [inspiration], [cute], [funny]
5. Commentary text max 8 words per spot IF using commentary spots format
6. CTA max 12 words
7. All text in {language}
7. Do NOT invent events not visible in footage
8. Do NOT claim source footage is yours

=================================================
FINAL INSTRUCTION:
Write a coherent, engaging narration that tells a story about the animal footage,
with proper word counts, natural pauses where footage speaks for itself, and
humorous/heartwarming interpretation that adds original value. Do NOT simply
describe what the viewer can see -- add interpretation, context, and personality."""

with codecs.open('data/script_prompts.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Updated narration_prompt successfully')
print('Total niches:', len(data['prompts']))