# Getting Started with the AI Lab Sandbox

Your first steps into the CUNY AI Lab Sandbox — from logging in to having your first conversation with an AI model.

---

## What You'll Find Here

The AI Lab Sandbox gives you access to a shared AI platform that works differently from consumer chatbots like ChatGPT. Instead of one-size-fits-all conversations, you can create custom AI agents, ground them in your course materials, and share configurations with students or colleagues. This guide walks you through your first login and initial exploration.

---

## Why This Matters

As a CUNY instructor or researcher, you likely face constraints that consumer AI tools don't address. Your students may come from diverse linguistic and cultural backgrounds. Your courses have specific learning outcomes. Your research may draw on specialized literature. The Sandbox lets you adapt AI to these realities. Your pedagogy drives the configuration, not the other way around.

The platform also keeps your work and your students' data within CUNY infrastructure. No third-party tracking. No training on student submissions. AI model providers operate under zero-retention agreements: prompts and responses are not stored or used for model training. Your chat conversations are stored within Open WebUI for persistence purposes only and are accessible only to you and system administrators. Just a shared tool that you control.

---

## First Login

### What You Need

- CUNY credentials (the same login you use for other CUNY services)
- A web browser (Chrome, Firefox, Safari, or Edge)
- About 10 minutes to explore

### Step by Step

1. **Navigate to** [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu)
   - Bookmark this page. You'll be back often.

2. **Click "Sign In"** at the top right
   - The Sandbox uses CUNY's authentication system, so you'll be redirected to the standard CUNY login page

3. **Enter your CUNY credentials** and complete any two-factor authentication if prompted
   - Same process as accessing CUNY email or Blackboard

4. **You'll land on the main chat interface**
   - Clean layout. Chat input at the bottom. Model selector at the top. Sidebar on the left with workspace features.

![First login walkthrough](images/first-login.gif)
<!-- TODO: Record GIF showing login flow through CUNY auth to landing page -->

**Voila!** You're in. Now let's have a conversation.

---

## Your First Conversation

### Try This

In the chat input at the bottom of the screen, type something simple:

> "Explain the concept of scaffolding in education, suitable for graduate students in a teaching methods course."

Press Enter (or click the send button). The AI responds. That's it. You just had your first Sandbox conversation.

**What just happened?** You sent a message to whichever AI model is currently selected (look at the top of the screen to see which one). The model generated a response based on your prompt. Simple enough.

**But here's where it gets interesting:** Notice the model name at the top? Click it. A dropdown appears showing other available models. Each one has different strengths. Some are better at writing. Some excel at reasoning. Some understand images. Some run faster. You can switch models mid-conversation to leverage different capabilities for different parts of your work.

---

## Exploring the Interface

Before you start building, take a moment to understand the layout.

### The Sidebar (Left)

- **Chats** — Your conversation history. Each chat is saved automatically.
- **Workspace** — Where you'll create AI models, build knowledge bases, and configure tools (we'll get to this in the Design Kit)
- **Admin Panel** — Instance-wide settings (if you have admin access)

### The Top Bar

- **Model selector** — Switch between available models
- **Settings icon** (gear) — Your personal preferences
- **Profile avatar** — Account settings and logout

### The Chat Area

- **Conversation thread** — Messages appear here
- **Input box** — Where you type
- **Upload button** (paperclip) — Attach files, images, or documents to your message
- **Tools button** (plus sign) — Add capabilities like web search to the current chat

![Interface overview with labeled sections](images/interface-overview.png)
<!-- TODO: Screenshot of main interface with annotations pointing to sidebar, model selector, input area -->

---

## Customizing Your Experience

### Settings You Might Want to Adjust

1. Click your **profile avatar** (top right)
2. Select **Settings**
3. You'll see several tabs. Here's what matters for getting started:

**General Tab:**
- **Default Model** — Choose which AI model loads when you start a new chat
  - Recommendation: Start with a general-purpose model like GPT-4 or Claude Sonnet
- **Interface Theme** — Light, dark, or auto (matches your system settings)
  - Dark mode reduces eye strain during long writing sessions
- **Chat Input Mode** — Desktop defaults to Enter to send, Shift+Enter for new line
  - If you prefer multiline input, flip this setting

**Account Tab:**
- **Profile Picture** — Optional, but helps when collaborating with colleagues
- **Display Name** — How your name appears to others when you share models or knowledge bases

**Advanced Tab:**
- **Temperature** — Controls how creative or focused the AI model's responses are
  - Lower (0.3-0.5): More focused, consistent, deterministic
  - Higher (0.7-1.0): More creative, varied, exploratory
  - Default (0.7) works well for most teaching and research tasks

![Settings panel with key options highlighted](images/settings-overview.png)
<!-- TODO: Screenshot of settings panel with annotations on default model and temperature -->

### Save and Return to Chat

Once you've adjusted your preferences:

1. Scroll to the bottom of the Settings panel
2. Click **Save**
   - Your settings persist across sessions
3. Click the **X** or press Escape to close Settings
4. You're back to the chat interface, ready to work

---

## What's Next?

You've logged in, had a conversation, and customized your workspace. That's the foundation. From here, you can either keep chatting to explore what the default models can do, or you can move into the Design Kit to start building custom configurations.

### If You Want to Keep Exploring

- Try different AI models by clicking the model name at the top
- Upload a document (PDF, Markdown, plain text) and ask questions about it
- Experiment with different prompts and see how responses change

### If You're Ready to Build

Head to the **Design Kit** section of this documentation. There you'll learn to:
- Create custom AI models with specific behaviors
- Build knowledge bases from your course materials
- Bind tools that extend what the AI can do

---

## Tips for Getting Started

**Start small.** You don't need to build complex configurations on day one. Chat with the default AI models. See what works. See what doesn't. Let that guide what you build later.

**Save interesting conversations.** Click the chat title in the sidebar to rename it. This makes it easier to find later when you want to revisit a useful interaction.

**Don't worry about breaking things.** The Sandbox is a shared tool, but your personal workspace is yours. Create AI models. Delete them. Experiment. You can't break the instance for others.

**Ask for help.** If you get stuck, reach out to the AI Lab team or check the community channels. CUNY faculty and researchers are building with this platform every day, and the community is generous with support.

---

## Additional Resources

- **Open WebUI Documentation** — [Official technical docs](https://docs.openwebui.com/) for deeper technical details
- **CUNY AI Lab** — [AI Lab homepage](https://ailab.gc.cuny.edu/) for workshops, office hours, and community events
- **Teach@CUNY Resources** — [Teaching with AI toolkit](https://aitoolkit.commons.gc.cuny.edu/) for pedagogical guidance on AI in the classroom

---

**[Continue to Models →](models.md)**
