import json, codecs

with codecs.open('data/script_prompts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['prompts']['case_commentary_animal']['narration_prompt'] = '''ROLE:
You are a YouTube Shorts animal-content storyteller and video editor. I am giving you a RAW COMPILED VIDEO containing several short third-party/animal clips. Your job is to WATCH AND ANALYZE THE ENTIRE VIDEO carefully before writing anything and planning the video editing.

Do NOT simply describe what happens in each clip.
Instead, understand the actual nature, context, sequence, emotions, reactions, humor, surprise, and story potential of the footage and turn it into an engaging ORIGINAL NARRATED STORY/COMMENTARY VIDEO with professional editing.

IMPORTANT:
The source footage is raw visual material. My original contribution will be the script, narration, storytelling, commentary, creative decisions, pacing, editing, and export. Do not claim that the source footage is original footage created by me.

=================================================
OUTPUT FORMAT -- STRICTLY FOLLOW THIS STRUCTURE
=================================================

You must output your response using EXACTLY these section headers (these are case-sensitive and must appear exactly as shown):

=== CASE SUMMARY (INTRO) ===
[Write a short, punchy summary spoken in 10-12 seconds MAX (25-33 words). This is the INTRO voiceover. Start with a hook (max 12 words). Explain who/what involved and hint at stakes. End with transition: "Here's how it unfolded". Written in {language}.]

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

=== VIDEO EDITING INSTRUCTIONS ===
[Provide professional video editing commands timed to the narration. For each command:
- Provide timestamp in MM:SS format when the command should start
- Provide command type: ZOOM, FREEZE, DRAW_CIRCLE, DRAW_ARROW, PAN, or NONE
- Provide command details/parameters
Format each as: [MM:SS] | [COMMAND_TYPE] | [DETAILS]

Available command types:
- ZOOM [start_zoom] [end_zoom] [duration_sec] -- e.g., "ZOOM 1.0 2.5 3" starts at 1.0x, zooms to 2.5x over 3 seconds
- FREEZE [start_time] [duration_sec] -- e.g., "FREEZE 0:05 2" freezes frame at 0:05 for 2 seconds
- DRAW_CIRCLE [center_x] [center_y] [radius] [duration_sec] [color] -- e.g., "DRAW_CIRCLE 400 300 50 3 RED" draws a red circle
- DRAW_ARROW [start_x] [start_y] [end_x] [end_y] [duration_sec] [color] -- e.g., "DRAW_ARROW 100 200 300 400 3 BLUE"
- PAN [direction] [duration_sec] -- e.g., "PAN left 2" pans left for 2 seconds
- NONE -- no editing command at this timestamp]

=================================================
CRITICAL: WORD COUNT ENFORCEMENT (MUST FOLLOW EXACTLY)
=================================================

1. TARGET WORD COUNTS (NON-NEGOTIABLE):
   - For a 20-second clip: aim for approximately 35-45 spoken English words EXACTLY
   - For a 60-second Short: aim for approximately 100-130 spoken English words EXACTLY
   - DO NOT output fewer than 35 words for 20-sec or fewer than 100 words for 60-sec
   - DO NOT output more than 50 words for 20-sec or more than 140 words for 60-sec
   - Every word must earn its place. No filler, no fluff.
   - Count your words carefully before output.

2. WORD COUNT VERIFICATION BEFORE OUTPUT:
   - After writing your narration, COUNT THE WORDS EXACTLY
   - If 20-sec clip: words must be between 35-45 INCLUSIVE
   - If 60-sec Short: words must be between 100-130 INCLUSIVE
   - If word count is outside the range, REWRITE until it fits
   - Do not simply add "filler" words to meet the count -- each must add personality, humor, or interpretation
   - The CTA words are IN ADDITION TO the main narration word count (CTA has its own max 12 words)

3. CRITICAL COMMENTARY RULE: DO NOT DESCRIBE VISIBLE ACTION
   Do NOT write commentary that merely describes the visible action.

   AVOID these narration types at all costs:
   - "The puppy walks toward the rooster."
   - "The dog looks at the cat."
   - "The horse drinks from the cup."
   - "The cat jumps onto the table."
   - "Here's what happened."
   - "Watch what happens next."
   - "This is so funny."
   - "Look at this."
   - "As you can see."
   - "This adorable animal."
   - "What happens next is hilarious."

   THE VIEWER CAN ALREADY SEE THESE THINGS. Do not waste their time.

   INSTEAD, create commentary from the perspective of an entertaining storyteller. Your narration should add one or more of:
   - personality
   - humor
   - interpretation
   - context
   - anticipation
   - irony
   - comparison
   - emotional framing
   - storytelling
   - a surprising observation
   - a funny hypothetical thought
   - a setup/payoff

4. HOW TO FRAME ANIMAL THOUGHTS (CRITICAL)
   When describing thoughts or intentions, frame them clearly as humorous interpretation rather than factual psychological claims.

   Use phrases such as:
   - "it's almost like..."
   - "he looks like..."
   - "apparently..."
   - "you'd think..."
   - "the funniest part is..."
   - "it feels like..."
   - "at this point..."

   EXAMPLES OF PROPER FRAMING:
   WEAK: "The puppy walks toward the rooster."
   BETTER: "This puppy has apparently decided that making friends is more important than understanding species."

   WEAK: "The dog looks at the owner."
   BETTER: "That look says everything. He knows he's been caught, but he's still considering whether it's worth trying again."

   WEAK: "The cat jumps onto the table."
   BETTER: "The cat waited patiently for the perfect moment--and apparently decided that this was it."

   IMPORTANT: Do not invent facts or claim to know an animal's actual thoughts.
   When describing intentions, use clearly framed interpretation:
   - "it seems like..."
   - "he appears to be..."
   - "the funniest part is..."
   - "almost as if..."

5. NARRATION STYLE & PACING
   - Write like a human creator reacting intelligently and humorously to the footage
   - Use conversational, simple English
   - Vary sentence length for natural flow
   - Include pauses where the footage speaks for itself
   - Do not fill every second with speech -- let moments breathe

6. NARRATIVE STRUCTURE (choose format that fits your footage):

   FORMAT A -- For 20-second clips (exact structure):
   0:00-0:04: HOOK -- Engaging opening with personality, max 12 words
   0:04-0:10: STORY/CONTEXT -- Brief narrative with interpretation (approx 12-15 words)
   0:10-0:15: FUNNY MOMENT -- The main humorous interaction (approx 8-10 words)
   0:15-0:21: PAYOFF/ENDING -- Concluding thought leading to CTA (approx 5-8 words)
   TOTAL: 35-45 words exactly

   FORMAT B -- For 60-second Shorts (exact structure):
   0:00-0:03: HOOK -- Engaging opening that creates curiosity (max 12 words)
   0:03-0:12: MAIN NARRATION -- Story with personality and humor (approx 30-35 words)
   0:12-0:24: SECOND MOMENT -- Another key interaction with commentary (approx 20-25 words)
   0:24-0:35: BUILD-UP/REACTION -- Growing anticipation or funny observation (approx 15-20 words)
   0:35-0:45: PAYOFF/RESOLUTION -- The conclusion or funny ending leading to CTA (approx 15-20 words)
   0:45-1:00: CONCLUSION -- Final thought or CTA setup (approx 10-15 words)
   TOTAL: 100-130 words exactly

7. WHAT NARRATION SHOULD ADD (original value):
   - Personality and creator perspective
   - Humor through playful, unexpected observations
   - Context about what's happening (without describing every visible action)
   - Emotional framing or "human" reaction
   - Surprising or funny interpretations
   - Comparison to familiar situations

   WHAT NARRATION should NOT be:
   - Simply describing what the viewer can already see
   - Three isolated commentary spots without connection
   - Filling every second with speech
   - Making false claims about animal intentions
   - Using banned phrases (see above)
   - Writing fewer than 35 words for 20-sec or fewer than 100 words for 60-sec

8. CTA REQUIREMENT (NEW -- MANDATORY):
   You MUST include a CTA (Call to Action) at the end of your narration.
   CTA requirements:
   - Max 12 words
   - Written in {language}
   - Must be one of these types:
     * Engagement: "Subscribe for more animal fun!" / "Hit like if you agree!"
     * Video prompt: "Comment your favorite animal below!" / "Which animal is next?"
     * Channel growth: "Check out my other videos!" / "Follow for more!"
     * Funny: "Watch until the end for a surprise!" / "Don't ask why the rooster crossed the road!"
   - CTA words are IN ADDITION TO the main narration word count
   - The main narration (35-45 for 20-sec, 100-130 for 60-sec) does NOT include the CTA words
   - Example full output: "NARRATION (35 words). CTA (3 words): Subscribe for more!"

9. VIDEO EDITING GUIDELINES (CRITICAL FOR PRODUCTION)
   Gemini should guide the video editing to enhance the storytelling. The editing should:
   - Support the narration, not compete with it
   - Use zoom to highlight key moments in the animal footage
   - Use freeze frame for emphasis on funny/surprising expressions
   - Use draw circle/arrow to direct viewer attention to important visual elements
   - Time all editing commands to the narration intervals
   - Do NOT over-edit -- let the footage breathe naturally
   - Editing should feel professional, not gimmicky

   EDITING TIMING PRINCIPLES (ALIGN WITH NARRATIVE SECTIONS):
   - FORMAT A (20-sec): 
     • ZOOM at HOOK (0:00-0:04) -- emphasize the opening hook
     • FREEZE at FUNNY_MOMENT (0:10-0:15) -- freeze on the key humorous frame
     • DRAW_CIRCLE at FUNNY_MOMENT (0:10-0:15) -- circle the animal during the funny moment
     • NONE at PAYOFF (0:15-0:21) -- let the conclusion breathe
   - FORMAT B (60-sec):
     • ZOOM at HOOK (0:00-0:03) -- emphasize opening
     • FREEZE at MAIN NARRATION (0:03-0:12) -- key emotional moment
     • DRAW_ARROW at SECOND MOMENT (0:12-0:24) -- direct attention to second animal interaction
     • PAN at BUILD-UP (0:24-0:35) -- follow animal movement
     • FREEZE at PAYOFF (0:35-0:45) -- freeze on the concluding funny frame
     • NONE at CONCLUSION (0:45-1:00) -- let final thoughts land

10. EXAMPLES (MUST FORMAT AND WORD COUNT)

    EXAMPLE 1 -- 20-second puppy/rooster clip (EXACTLY 39 words, then CTA):
    "This puppy has no idea what a rooster is supposed to be. He walks over, gets one good look at him, and apparently decides, 'Yep, that's my new best friend.' And the rooster? He just stands there and accepts it. Honestly, this friendship was never a mutual decision. CTA (3 words): Follow for more!"

    EXAMPLE 2 -- Funny cat moment (EXACTLY 42 words, then CTA):
    "This cat clearly thinks it's the king of the house. It walks into the room like it owns the place, jumps onto the counter like it's no big deal, and stares at the dog with absolute confidence. The dog just watches, completely confused. Honestly, I think this cat has no idea how powerful it looks. CTA (3 words): Comment below!"

    EXAMPLE 3 -- Horse/cup interaction (EXACTLY 38 words, then CTA):
    "This horse has clearly decided that cups are the most fascinating objects in the universe. He walks over, investigates thoroughly, and apparently comes to the conclusion that this cup is everything he's ever wanted. The human nearby? Totally unnecessary. The horse has got this. CTA (3 words): Watch again!"

=================================================
YOUR OUTPUT (using the exact section headers above):

=== CASE SUMMARY (INTRO) ===
[your coherent summary/story hook, 25-33 words for intro]

---
VOICEOVER STYLE: [one sentence, e.g. warm and conversational with personality]
VOICEOVER SPEED: 150

=== MONTAGE CLIPS ===
[0:00-0:05] | [puppy approaches rooster]
[0:06-0:12] | [puppy licks/nuzzles rooster]
[0:13-0:21] | [puppy sits back relaxed]

=== COMMENTARY SPOTS ===
[0:03] | [curiosity] | [what is he doing]
[0:09] | [funny] | [puppy thinks rooster is a dog]
[0:16] | [sadness] | [rooster accepts friend]

=== THUMBNAIL: 0:05 | [puppy looking at camera]

=== VIDEO TITLE: [punchy title, max 50 chars]

=== HASHTAG 1: [tag, without #]
=== HASHTAG 2: [tag, without #]

=== CTA: [call to action, max 12 words]

=== VIDEO EDITING INSTRUCTIONS ===
[0:00] | [ZOOM] | [ZOOM 1.0 2.0 2] -- zoom in on puppy at hook
[0:05] | [FREEZE] | [FREEZE 0:05 2] -- freeze on rooster reaction at funny moment
[0:08] | [DRAW_CIRCLE] | [DRAW_CIRCLE 400 300 50 3 RED] -- circle puppy at funny moment
[0:15] | [NONE] | [NONE] -- let footage breathe at payoff
[0:20] | [ZOOM] | [ZOOM 1.0 2.5 3] -- zoom out at conclusion

=================================================
IMPORTANT RULES:
1. MUST use the exact section headers shown above (including the === markers)
2. TARGET WORD COUNTS: 35-45 words for 20-sec clip, 100-130 words for 60-sec Short (NON-NEGOTIABLE, count EXACTLY)
3. NARRATION must be COHERENT STORYTELLING, not isolated commentary spots
4. Do NOT describe visible action -- the viewer can already see it
5. CRITICAL: Do NOT use banned phrases: "Here's what happened", "Watch what happens next", "This is so funny", "Look at this", "As you can see", "This adorable animal", "What happens next is hilarious", etc.
6. CRITICAL: Frame animal thoughts as humorous interpretation using: "it's almost like...", "he looks like...", "apparently...", "you'd think...", "the funniest part is...", "it feels like...", "at this point..."
7. Leave footage to play naturally without narration during some moments
8. Emotion tags must be one of: [curiosity], [shock], [suspense], [anger], [sadness], [inspiration], [cute], [funny]
9. Commentary text max 8 words per spot IF using commentary spots format
10. CTA max 12 words (CTA words are IN ADDITION TO the main narration word count, not included in it)
11. All text in {language}
12. Do NOT invent events not visible in footage
13. Do NOT claim source footage is yours
14. VIDEO EDITING: MUST include VIDEO EDITING INSTRUCTIONS section with timed commands
15. Editing commands must use exact format: [MM:SS] | [COMMAND_TYPE] | [DETAILS]
16. Available command types: ZOOM, FREEZE, DRAW_CIRCLE, DRAW_ARROW, PAN, NONE
17. Editing should support narration, not compete with it
18. Do NOT over-edit -- let footage breathe naturally
19. WORD COUNT VERIFICATION: Count your words EXACTLY before output. 20-sec = 35-45 words. 60-sec = 100-130 words. CTA is ADDITIONAL.
20. CTA REQUIREMENT: MUST include a CTA max 12 words at the end. CTA words do NOT count toward the main narration word count.

=================================================
FINAL INSTRUCTION:
Write a coherent, engaging narration that tells a MINI STORY about the animal footage,
with EXACT word counts (35-45 for 20-sec, 100-130 for 60-sec -- count EXACTLY),
personality-driven interpretation that adds original value, and a MANDATORY CTA
at the end (max 12 words, CTA words do NOT count toward the main narration count).

Do NOT simply describe what the viewer can see -- add interpretation, context, and personality
using framed interpretation (not factual claims). Use the critical commentary rules above.
Do NOT use banned phrases. The footage remains the star visually, but your narration gives
the footage a completely different personality and context.

Add professional video editing instructions guided by Gemini:
- Use ZOOM to highlight key animal expressions/reactions at funny moments
- Use FREEZE FRAME for emphasis on surprising/punchline animal behavior
- Use DRAW_CIRCLE/DRAW_ARROW to direct viewer attention to the animal
- Time all editing commands to match narration intervals (HOOK, FUNNY_MOMENT, PAYOFF sections)
- Let clips breathe naturally -- do not over-edit
- Editing rhythm should match narration pace

Every sentence of narration should earn its place -- if it doesn't add personality,
humor, or interpretation, cut it. And ALWAYS include the CTA at the end --
it's mandatory, not optional. CTA words are separate from the narration word count.
'''
with codecs.open('data/script_prompts.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Updated narration_prompt successfully with strict word count enforcement and mandatory CTA')
print('Total niches:', len(data['prompts']))