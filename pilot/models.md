# Building Custom Models

Building custom AI models using preset configurations in Open WebUI. A custom model lets you shape how the AI behaves in your course, what documents it draws from, and which tools it can use. You are not training a new AI from scratch. You are assembling existing components into something tuned to your teaching context.

## Why This Matters

A base model answers questions from its general training data. That data may be outdated, incomplete, or irrelevant to your discipline. A custom model lets you define the boundaries: what the AI should do, what it should refuse to do, and what materials it should draw from when responding.

For a composition instructor, that might mean a writing tutor that asks follow-up questions instead of producing finished essays. For a public health researcher, a literature review assistant grounded in your curated bibliography. For a digital humanities seminar, an analysis tool that knows your corpus and your methods.

## Model Uses

- **Writing Tutor**: Create a model that responds to student drafts with questions and suggestions rather than rewrites. Encode your rubric and assignment expectations directly in the system prompt.
- **Course Advisor**: Build a model grounded in your syllabus, program handbook, and departmental policies. Students get answers drawn from institutional documents rather than generic training data.
- **Research Assistant**: Configure a model with your annotated bibliography in its knowledge base and academic search tools enabled. Ask it to compare methodological approaches across your sources.
- **Language Practice Partner**: Set up a model with a system prompt that maintains conversation in a target language, corrects errors gently, and adjusts complexity to the learner's level.
- **Exam Review Guide**: Attach lecture notes and past study guides as a knowledge base. Students can quiz themselves and get explanations grounded in your course materials.

## Getting Started

1. Click **Workspace** in the left sidebar
2. Select **Models**
3. Click **+ New Model**
   - This opens the model editor. You will define the model's behavior, connect it to your documents, and choose which tools it can access.
4. Choose a **base model** from the dropdown
   - The available models depend on which providers your Sandbox is connected to. If you need a specific model and do not see it listed, contact the AI Lab team.
5. Write a **system prompt** (see below for guidance)
6. Attach **knowledge bases** if you want the model to draw from your documents
   - See [Knowledge Bases](knowledge-bases.md) for how to create one
7. Bind **tools** if you want the model to search the web, run code, or access other services
   - See [Tools & Skills](tools-skills.md) for available options
8. Add **prompt suggestions**
   - These appear as clickable chips above the input bar when students open a new chat. They show users what the model can do and how to talk to it.
9. Set **visibility**
   - **Private**: only you can use it
   - **Limited**: shared with specific users or groups (e.g., your course section)
   - **Public**: available to all Sandbox users
10. Click **Save**

![Creating a custom model](images/create-model.gif)
<!-- TODO: Record GIF of the model creation flow from Workspace → Models → + New Model → Save -->

## Writing System Prompts

The system prompt is where you tell the model who it is and how to behave. A good prompt for a CUNY context does three things: it establishes the model's role, sets boundaries around academic integrity, and provides enough specificity that the model knows what kind of help to offer.

Here is an example for a writing tutor:

```
You are an academic writing tutor for {{ USER_NAME }} at CUNY.
The current date is {{ CURRENT_DATE }}. You help students improve
their writing through questions and suggestions. You do not write
complete essays or assignment submissions. When a student submits
a draft, identify two strengths before addressing areas for revision.
Encourage critical thinking. Ask follow-up questions that help
students develop their own arguments.
```

The `{{ }}` placeholders are **dynamic variables** that inject real-time context:

- `{{ USER_NAME }}` inserts the logged-in student's display name
- `{{ CURRENT_DATE }}` inserts today's date (YYYY-MM-DD format)
- `{{ CURRENT_TIME }}` inserts the current time (24-hour format)

These let a single model configuration serve many users with personalized interactions. An advisor model can greet each student by name. A deadline-aware tutor can reference the current date without you updating the prompt each week.

### Prompt Suggestions

Prompt suggestions are the clickable chips that appear when a user opens a fresh chat. They serve as onboarding: a quick way to show students what the model can do. For a writing tutor:

- "Help me strengthen my thesis statement"
- "Review my introduction paragraph"
- "How can I better integrate this source?"

For a research assistant:

- "Compare the methods used in these three papers"
- "What gaps exist in the literature I've uploaded?"
- "Summarize the theoretical evolution across my sources"

## Going Deeper

### Advanced Parameters

Most instructors will not need to adjust these. They are here for users who want finer control over how the model generates responses.

- **Max Tokens** sets the maximum length of the model's response. One token is roughly three-quarters of a word. Lower values (100-500) produce concise answers: useful for quick definitions or focused feedback. Higher values (1000-4000) allow detailed explanations: appropriate for essay analysis or research summaries. If responses cut off mid-sentence, increase this value.
- **Temperature** controls randomness. Lower values (0.1 to 0.3) produce focused, deterministic responses: good for factual research tasks. Higher values (0.7 to 1.0) allow more creative variation: useful for brainstorming or creative writing activities.
- **Top P** (nucleus sampling) controls the diversity of word selection. A value of 0.9 means the model considers words covering 90% of the probability mass. Leave this at default unless you have a specific reason to change it.
- **Stop Sequences** force the model to stop generating when it encounters specific text strings. Enter sequences like `<|end_of_text|>` or `User:` and press Enter. Useful for models that might otherwise generate both sides of a conversation.

### Switching Models Mid-Chat

You can change models during a conversation by clicking the model name at the top of the chat. The conversation context carries across the switch. This lets you use different models for different stages of a task: start with a general-purpose model for brainstorming, switch to a code-focused model for implementation, then move to a writing model for documentation.

> **Tip:** Encourage students to experiment with model switching. Different models have different strengths. A model optimized for close reading will give different results than one designed for quantitative analysis. Learning when to switch is part of developing AI literacy.

## Callout

<div class="callout">
  <strong>For instructors:</strong> When building models for your courses, make your expectations for AI use explicit in the system prompt. If the model should refuse to generate complete assignments, encode that boundary. If it should encourage process over product, say so directly. Students benefit from clarity about what the tool will and will not do. Vague instructions produce vague behavior.
</div>

## Additional Resources

- [Open WebUI Model Configuration Docs](https://docs.openwebui.com) — official reference for all model settings
- [Teach@CUNY AI Toolkit: Course Policies](https://aitoolkit.commons.gc.cuny.edu/course-policies/) — guidance on setting expectations for AI use in your courses
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) — OpenAI's strategies for writing effective prompts

---

[← Return to Getting Started](getting-started.md) | [Continue to Knowledge Bases →](knowledge-bases.md)
