import json
import os

# Read the existing file
filepath = r'D:\MyFinalAutomations\VideoTextExtractor\data\script_prompts.json'
with open(filepath, 'rb') as f:
    raw = f.read()
text = raw.decode('utf-8-sig')
data = json.loads(text)

# Add the new animal storytelling niche entry
data['prompts']['case_commentary_animal_story'] = {
    'name': 'Animal Storytelling',
    'description': 'Narration for animal-focused YouTube Shorts with story structure and commentary',
    'narration_prompt': 'You are an expert animal storytelling scriptwriter for YouTube Shorts. Create an engaging 60-second animal story with a hook, setup, clips, commentary, analysis, second moment, payoff, and conclusion.\n\nSTRICT RULES -- FOLLOW EVERY ONE:\n\n1. STYLE: Write in an engaging, conversational tone suitable for animal-content YouTube Shorts. Make the narration the backbone of every video.\n\n2. HOOK: Start with an engaging hook using the formula: You wont believe what this [animal] did when [situation]...\n\n3. SETUP: Explain why the viewer should care using: His owner had just left the room for a few seconds, and that\'s when this happened. OR: Everything looked normal until the [animal] noticed [object].\n\n4. MAIN CLIP + COMMENTARY: Dont simply describe what is visible. Add interpretation and entertainment. For example: Look at how carefully he\'s approaching. He already knows he\'s about to get caught, but apparently that isnt stopping him.\n\n5. ANALYSIS / REACTION: Explain something the viewer may not have noticed. For example: Now look at his face right here. He isnt confused--hes checking whether anyone saw him. OR: Watch the owners reaction in this moment. Thats when he realizes exactly whats happening.\n\n6. SECOND MOMENT + COMMENTARY: Introduce the second moment as part of the same story. For example: But thats not even the funniest part. OR: And then things got even more ridiculous.\n\n7. BUILD TO PAYOFF: Create anticipation. For example: But wait until you see what happens when... OR: And thats when the entire plan falls apart.\n\n8. PAYOFF: This should be the funniest/surprising moment. Keep it short. For example: Yep. He actually did it. Then let the important moment play.\n\n9. CONCLUSION: Your final creative contribution. For example: So apparently this dog wasnt stealing the food--he was conducting an investigation. OR: I dont know what this cat was thinking, but clearly the plan was working.\n\nThen: Would your pet do this?\n\nSTRICT RULES:\n- Do not make false claims about ownership of source footage\n- Do not claim the source footage is yours or make unsupported copyright/fair-use claims\n- The narration must add meaningful value beyond simple visual description\n- Source clips should be used as supporting visuals, not the primary creative element\n- Your personality and humor should come through in the narration\n\nOriginal Video Title: {title}\n\nRAW FOOTAGE DESCRIPTION: {footage_description}\n\nWrite the animal storytelling narration script now (no preamble, no explanations -- just the script):\n\nmetadata_prompt: Based on the following footage description and its animal storytelling script, generate:\n\n1. A suggested video title (maximum 12 words, curiosity-driven, clickable but NOT misleading)\n2. Exactly 2 relevant hashtags (WITHOUT the # symbol, in PascalCase or TitleCase)\n\nNiche angle: animal storytelling perspective\n\nFootage Description:\n{footage_description}\n\nCinematic Script:\n{script}\n\nReturn ONLY valid JSON in this exact format (no markdown, no code fences, no explanation):\n{\"suggested_title\": \"your curiosity-driven title here\", \"hashtag_1\": \"FirstHashtag\", \"hashtag_2\": \"SecondHashtag\"}}'
}

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('Successfully added case_commentary_animal_story to script_prompts.json')