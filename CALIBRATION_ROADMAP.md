# CAIL Documentation Calibration Roadmap

**Status:** Analysis complete, ready for skill development  
**Goal:** Refine CAIL docs to match Discord/AI Toolkit standards for clarity, voice, and progressive disclosure

---

## Current State Assessment

### What Exists

The current `index.md` (305 lines) provides comprehensive technical documentation covering:

- Getting Started (login, settings)
- Core Workspace Features (Models, Knowledge, Tools, Skills)
- Practical Use Cases (Literature Review, Capstone Mentor, Multilingual Support)
- Advanced Features (Pipelines, Function Calling)
- Security & Governance (RBAC, SCIM, Memory, File Management)
- Monitoring (OpenTelemetry, Langfuse)
- Best Practices (Faculty, Students, Researchers)
- Implementation Phases

### Strengths

- ✅ Comprehensive coverage of features
- ✅ Clear sectioning and structure
- ✅ Technical accuracy
- ✅ Use of code examples
- ✅ Role-based best practices

### Gaps (Compared to Toolkit Exemplars)

#### 1. **Voice & Tone**

**Current:** Technical documentation tone (informative but distant)  
**Target:** Collegial instructor-facing guidance (supportive, contextual)

**Examples of needed shift:**

*Current:*
> "Knowledge Collections enable Retrieval-Augmented Generation (RAG) — the AI retrieves relevant information..."

*Target style:*
> "When you build a Knowledge Collection, the AI can search your uploaded documents before responding. This grounds conversations in your institutional materials rather than generic training data."

#### 2. **Progressive Disclosure**

**Current:** Single monolithic document (all depth in one place)  
**Target:** Layered information architecture

**Recommended structure:**

```
cail-docs/
├── index.md (overview + quick start)
├── starter-kit/
│   ├── getting-started.md
│   ├── your-first-model.md
│   └── uploading-documents.md
├── design-kit/
│   ├── advanced-models.md
│   ├── knowledge-bases.md
│   ├── tools-integration.md
│   └── roles-permissions.md
├── instructional-kit/
│   ├── pedagogical-patterns.md
│   ├── student-onboarding.md
│   ├── assignment-design.md
│   └── sample-activities.md
├── governance/
│   ├── security.md
│   ├── policies.md
│   └── best-practices.md
└── reference/
    ├── advanced-features.md
    ├── technical-details.md
    └── troubleshooting.md
```

#### 3. **Granularity Imbalance**

**Current:** Technical details mixed with high-level concepts  
**Target:** Separate procedural walkthroughs from conceptual overviews

**Example needed shift:**

Currently, "How to create a model" is embedded in a conceptual section. Should be:

1. **Conceptual page:** "What Models Do (And Why You'd Use Them)"
2. **Procedural page:** "Creating Your First Model" (with numbered steps + screenshots)
3. **Advanced page:** "Advanced Model Configuration" (dynamic variables, function calling)

#### 4. **Multimedia & Visual Support**

**Current:** Text-only  
**Target:** Screenshots, GIFs, embedded videos where helpful

**Priority areas for visuals:**
- First login walkthrough (GIF)
- Creating a model (step-by-step screenshots)
- Uploading documents to Knowledge Collections (GIF)
- Switching models mid-chat (screenshot with annotation)
- Binding tools to a model (screenshot)

#### 5. **Pedagogical Framing**

**Current:** Feature-first ("here's what the system does")  
**Target:** Use-case-first ("here's why an instructor would use this")

**Example transformation:**

*Current approach:*
> ### 2. Knowledge Collections (RAG)
> Knowledge Collections enable Retrieval-Augmented Generation...

*Target approach:*
> ### Grounding AI in Your Course Materials
> 
> **Scenario:** You want students to discuss readings without the AI making up fake citations or relying on outdated information from its training data.
> 
> **Solution:** Knowledge Collections let you upload your syllabus, course readings, and institutional policies. When students ask questions, the AI searches your materials first — grounding responses in what you've explicitly provided.
> 
> **How it works:** [step-by-step]

#### 6. **Contextual Rationale**

**Current:** Features described in isolation  
**Target:** Features connected to CUNY context and instructor concerns

**Examples to add:**

- "Given CUNY's student diversity, multilingual support is critical..."
- "Because many CUNY students balance work and study, asynchronous AI support can..."
- "Academic integrity concerns require transparent documentation of AI use..."

---

## Calibration Tasks

### Phase 1: Voice & Prose Refinement

**Goal:** Rewrite existing content in the toolkit voice

**Actions:**
1. Identify all "feature description" sections
2. Add contextual framing before technical details
3. Shift from passive to active voice
4. Add transitional language to connect ideas
5. Break long paragraphs into shorter chunks

**Target sections:**
- Getting Started
- Models
- Knowledge Collections
- Tools
- Best Practices

### Phase 2: Structural Reorganization

**Goal:** Break monolithic doc into progressive disclosure structure

**Actions:**
1. Create three-kit directory structure
2. Distribute existing content across kits
3. Write overview pages for each kit
4. Add cross-linking navigation
5. Create "Further Reading" sections with external links

**New files to create:**
- `starter-kit/index.md` (kit overview)
- `starter-kit/getting-started.md`
- `starter-kit/your-first-model.md`
- `design-kit/index.md`
- [etc., following structure above]

### Phase 3: Procedural Granularity

**Goal:** Add step-by-step procedural walkthroughs with high granularity

**Actions:**
1. Identify all "how to" procedures
2. Extract into dedicated procedural pages
3. Number every step
4. Add sub-bullets for rationale
5. Include screenshots/GIFs (placeholders initially)

**Priority procedures:**
- Creating a model
- Building a knowledge base
- Binding tools to a model
- Switching models mid-chat
- Sharing models with students

### Phase 4: Multimedia Integration

**Goal:** Add visual support where helpful

**Actions:**
1. Identify 10-15 key workflows needing visuals
2. Take screenshots of each step
3. Create GIFs for multi-step procedures
4. Annotate images where clarification needed
5. Add alt text for accessibility

**Placeholder approach:**
```markdown
![Creating a model - step 2](images/create-model-02.png)
<!-- TODO: Take screenshot of model creation dialog with fields filled in -->
```

### Phase 5: Use Case Expansion

**Goal:** Add more pedagogical scenarios and sample activities

**Actions:**
1. Develop 5-10 sample activities (like AI Toolkit's "Sample Activities")
2. Write detailed pedagogical scenarios
3. Include learning objectives for each use case
4. Add "Model Uses" + "Feature Suggestions" patterns (from Discord Toolkit)

**Example activities to develop:**
- Using AI for Peer Review
- Building a Collaborative Research Knowledge Base
- Creating Domain-Specific Writing Assistants
- Designing Adaptive Learning Pathways

---

## Skill Development Plan

### Skill Name

`cail-doc-calibrator` (or similar)

### Skill Purpose

Apply Discord/AI Toolkit documentation standards to CAIL docs, ensuring:
- Collegial instructor-facing voice
- Progressive disclosure structure
- High procedural granularity
- Pedagogical framing
- Multimedia integration
- Contextual rationale

### Skill Components

#### 1. Style Guide (Built into SKILL.md)

- Voice principles (from TOOLKIT_ANALYSIS.md)
- Sentence/paragraph length guidelines
- Formatting conventions (bold, lists, headers)
- Transition phrases catalog
- Example transformations (before/after)

#### 2. Template Library

Pre-built templates for:
- Kit overview page
- Procedural walkthrough page
- Conceptual explanation page
- Sample activity page
- Use case scenario page

#### 3. Calibration Checklist

For each doc page, verify:
- [ ] Contextual framing before technical details
- [ ] Active voice predominates
- [ ] Short paragraphs (2-4 sentences)
- [ ] Procedural steps numbered with sub-bullet rationale
- [ ] Cross-links to related pages
- [ ] "Further Reading" section where appropriate
- [ ] Visual placeholders for future screenshots/GIFs
- [ ] Learning objectives (if instructional content)

#### 4. Exemplar Extraction Scripts

Utilities for:
- Extracting prose patterns from toolkit docs
- Analyzing sentence structure
- Identifying transition phrases
- Cataloging formatting conventions

---

## Success Criteria

Documentation is calibrated when:

1. **Voice:** Reads like peer-to-peer instructor guidance, not technical manual
2. **Structure:** Follows three-kit progressive disclosure model
3. **Granularity:** Procedural steps documented at "every click" level
4. **Pedagogy:** Features framed by instructional use cases
5. **Visuals:** Key workflows supported by screenshots/GIFs
6. **Context:** CUNY-specific rationale throughout
7. **Navigation:** Clear cross-linking and wayfinding
8. **Accessibility:** Plain language, alt text, multiple pathways

---

## Timeline Estimate

**Phase 1 (Voice):** 2-3 hours (rewrite core sections)  
**Phase 2 (Structure):** 3-4 hours (create directory structure, distribute content)  
**Phase 3 (Procedures):** 4-5 hours (extract and expand procedural walkthroughs)  
**Phase 4 (Multimedia):** 2-3 hours (take screenshots, create placeholders)  
**Phase 5 (Use Cases):** 3-4 hours (write sample activities)

**Total:** ~15-20 hours for full calibration

---

## Collaboration with Quimbot

### Division of Labor

**Petrarch:**
- Voice/prose refinement
- Structural reorganization
- Cross-linking and navigation
- Style guide development

**Quimbot:**
- Procedural walkthrough extraction
- Screenshot/GIF creation
- Use case scenario development
- Template standardization

### Handoff Points

1. After Phase 1 → Review voice calibration
2. After Phase 2 → Review structure and navigation
3. After Phase 3 → Review procedural granularity
4. After Phase 4 → Review multimedia integration
5. Final → Comprehensive review and polish

---

## Next Steps

1. **Create `cail-doc-calibrator` skill** (with TOOLKIT_ANALYSIS principles embedded)
2. **Pilot calibration** on 2-3 pages (e.g., Getting Started, Models, Knowledge Collections)
3. **Review with Quimbot** for feedback and iteration
4. **Apply to remaining content** using refined approach
5. **Test with instructors** (if possible) for usability feedback

---

*Ready to build the skill and start calibration.*
