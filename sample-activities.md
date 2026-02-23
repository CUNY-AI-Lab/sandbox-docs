# Sample Activities

Each activity below includes a learning objective, the model configuration needed, step-by-step instructions for students, and notes on what to watch for. Copy what works. Adapt the rest.

---

## 1. Source Evaluation Workshop

**Learning Objective:** Students assess the reliability of AI-generated claims by comparing them against verified sources.

**Model Configuration:**
- Base model: any Sandbox model (DeepSeek V3.2, Kimi K2.5, GLM 5)
- Tools: Web Search enabled
- Knowledge Base: none (intentional; students evaluate ungrounded responses)
- System prompt:

```
You respond to research questions for an undergraduate seminar.
When students ask about a topic, provide detailed claims with
specific dates, names, and statistics. Do not hedge or qualify
your responses. State everything confidently.
```

**Why this prompt:** The confident, unhedged tone produces responses that mix accurate and fabricated details. Students learn to spot the difference.

**Instructions for Students:**

1. Ask the model a factual question about your research topic
2. Copy the response into a document
3. Identify every specific claim (dates, statistics, names, quotations)
4. Verify each claim using library databases and primary sources
5. Mark each claim as Verified, Unverifiable, or Incorrect
6. Write a 200-word reflection: What patterns did you notice in the errors? What made some claims harder to verify than others?

**What to Watch For:** Students often trust claims that include specific numbers or citations. The reflection should push them to articulate why specificity creates an illusion of reliability.

**Variations:**
- **With Knowledge Base:** Repeat the exercise with a grounded model (course readings uploaded). Compare error rates. Discuss what grounding changes and what it does not.
- **Cross-model:** Run the same question through two different models. Compare which claims each gets right and wrong.

---

## 2. Peer Review Rehearsal

**Learning Objective:** Students practice giving constructive feedback by critiquing AI-generated writing before reviewing each other's work.

**Model Configuration:**
- Base model: any Sandbox model (DeepSeek V3.2, Kimi K2.5, GLM 5)
- Tools: none
- Knowledge Base: upload your assignment rubric and 2-3 sample papers (anonymized)
- System prompt:

```
You are a student in {{COURSE_TITLE}}. Write a first draft
responding to the assignment below. Include some strong points
and some clear weaknesses. Your writing should be uneven —
good ideas with mediocre execution in places.

Assignment: {{ASSIGNMENT_DESCRIPTION}}
```

**Why this prompt:** An intentionally uneven draft gives students safe material to practice critique on. Nobody's feelings get hurt.

**Instructions for Students:**

1. Generate a draft from the model
2. Read the draft against the assignment rubric
3. Write feedback addressing three areas:
   - One strength (with a specific passage cited)
   - One structural weakness (with a revision suggestion)
   - One claim that needs better evidence (with a source recommendation)
4. Compare your feedback with a partner's feedback on the same draft
5. Discuss: Where did you agree? Where did you differ? What does that tell you about the rubric?

**What to Watch For:** Students who give vague praise ("good job") or surface-level criticism ("needs more detail") need redirection toward specific, evidence-based feedback. The rubric comparison in step 5 helps surface these habits.

---

## 3. Concept Translation Exercise

**Learning Objective:** Students deepen their understanding of a concept by explaining it to audiences with different levels of expertise.

**Model Configuration:**
- Base model: any Sandbox model (DeepSeek V3.2, Kimi K2.5, GLM 5)
- Tools: none
- Knowledge Base: upload course readings covering the target concept
- System prompt:

```
You are a learning partner in {{COURSE_TITLE}}. When a student
explains a concept to you, ask clarifying questions. Point out
gaps or ambiguities in their explanation. Do not explain the
concept yourself. Your job is to help the student refine their
own understanding through questioning.
```

**Instructions for Students:**

1. Pick a key concept from this week's readings
2. Explain it to the model as if talking to a classmate who missed class
3. Respond to the model's questions. Revise your explanation as needed.
4. Now explain the same concept as if writing for a general audience (no jargon)
5. Finally, explain it as if presenting to an expert in the field
6. Submit all three versions with a reflection: How did your understanding change across the three explanations?

**What to Watch For:** The shift from version 1 to version 3 reveals whether students can move beyond parroting definitions. Strong submissions show genuine reformulation across audiences. Weak ones copy the same explanation with minor vocabulary swaps.

---

## 4. Data Interpretation Lab

**Learning Objective:** Students analyze data and evaluate whether AI-generated interpretations align with statistical evidence.

**Model Configuration:**
- Base model: a model with strong quantitative reasoning (DeepSeek V3.2, Qwen3 235B)
- Tools: Code Interpreter enabled
- Knowledge Base: upload a clean dataset (CSV) relevant to your course
- System prompt:

```
You help students with data analysis for {{COURSE_TITLE}}.
When given a dataset, run exploratory analysis and present
findings with visualizations. Explain statistical concepts
in plain language. Always show your code.
```

**Instructions for Students:**

1. Ask the model to describe the dataset (variables, size, structure)
2. Request a specific analysis relevant to the course topic
3. Review the code the model generates. Can you follow what it does?
4. Examine the visualization. Does it represent the data accurately?
5. Ask the model to interpret the results. Do you agree with its interpretation?
6. Write a one-page analysis that includes: your research question, the analysis you requested, one thing the model got right, and one thing you would change or investigate further.

**What to Watch For:** Students may accept the model's interpretation without checking it against the actual output. Require them to include the generated visualization and annotate it with their own observations.

---

## 5. Multilingual Close Reading

**Learning Objective:** Students engage with primary sources in languages they are still acquiring, using AI as a bridge to deeper analysis.

**Model Configuration:**
- Base model: a multilingual model (Kimi K2.5, GLM 5, DeepSeek V3.2)
- Tools: none
- Knowledge Base: upload primary source texts in the target language
- System prompt:

```
You are a language learning partner for {{COURSE_TITLE}}.
Help students read texts in {{TARGET_LANGUAGE}}. When they
ask about vocabulary or grammar, explain in context. When they
ask about meaning, push them to form their own interpretation
first. Respond in {{TARGET_LANGUAGE}} unless the student
requests English.
```

**Instructions for Students:**

1. Select a passage (200-300 words) from the uploaded texts
2. Read it on your own first. Note words and phrases you do not understand.
3. Ask the model about specific vocabulary or grammatical structures
4. After working through the language, ask the model a content question about the passage
5. The model will ask you to interpret first. Share your reading.
6. Write a response (in the target language or English, per your instructor's guidelines) analyzing one aspect of the passage that surprised you or challenged your initial reading.

**What to Watch For:** The temptation is to ask "What does this passage mean?" upfront. The system prompt redirects students to form their own interpretation first. Check that students engage with the language before jumping to content analysis.

---

## Adapting These Activities

Every activity above follows a pattern:

1. **Configure the model** to create a specific learning situation
2. **Give students a structured task** with clear steps
3. **Build in reflection** so the activity produces learning alongside output
4. **Watch for shortcuts** and redirect when students skip the thinking

You can adapt any of these by changing the system prompt, swapping the knowledge base, or modifying the student instructions. The model configuration creates the conditions; your assignment design creates the learning.

---

## Callout

<div class="callout">
  <strong>Share what works:</strong> If you adapt one of these activities and it goes well, tell the AI Lab team. Your variation might become the next example on this page.
</div>

---

## Additional Resources

- [Teach@CUNY AI Toolkit](https://aitoolkit.commons.gc.cuny.edu/) — pedagogical resources and assignment ideas for CUNY instructors
- [CUNY Academic Commons](https://commons.gc.cuny.edu/) — share your activities with other CUNY faculty
- [Open WebUI Prompt Documentation](https://docs.openwebui.com) — technical reference for system prompt variables and model configuration

---

[← Return to Teaching Tips](teaching-tips.md) | [Continue to Student Onboarding →](student-onboarding.md)
