# Pilot Calibration Assessment

**Date:** February 22, 2026  
**Pilots Reviewed:** Getting Started, Models, Knowledge Bases  
**Reviewers:** Petrarch + Quimbot

---

## Executive Summary

All three pilot pages successfully demonstrate voice calibration and progressive disclosure principles from the Discord Educational Toolkit and Teach@CUNY AI Toolkit. The warmth/density distinction between Starter Kit and Design Kit pages is validated and intentional. The hybrid approach in Knowledge Bases works well.

**Recommendation:** Proceed with full calibration of remaining CAIL docs using the `cail-doc-calibrator` skill.

---

## Checklist Results

### Getting Started (Starter Kit)

- ✅ Contextual framing before technical details
- ✅ Active voice throughout
- ✅ Short paragraphs (2-4 sentences)
- ✅ Procedural steps numbered with sub-bullet rationale
- ✅ Visual placeholders with alt text
- ✅ Cross-links to related pages (Design Kit)
- ✅ Additional Resources section with external links
- ✅ Navigation footer
- ✅ CUNY-specific context
- ✅ No AI slop vocabulary
- ✅ No em dashes
- ✅ Tips callout section

**Voice characteristics:**
- Warm, encouraging ("Voila!", "Don't worry about breaking things")
- Analogies for concepts ("workspace not chat app")
- Incremental pacing
- Direct address throughout

**Strengths:**
- Excellent onboarding energy
- Strong CUNY context integration
- Clear visual placeholders
- Effective use of encouragement without being patronizing

**Opportunities:**
- Could add a "Common Questions" section for first-login troubleshooting

---

### Models (Design Kit)

- ✅ Contextual framing before technical details
- ✅ Active voice throughout
- ✅ Short paragraphs (2-4 sentences)
- ✅ Procedural steps numbered with sub-bullet rationale
- ✅ Model Uses separated from procedures
- ✅ Visual placeholders with alt text
- ✅ Cross-links to related pages (Knowledge Bases, Tools)
- ✅ Additional Resources section with external links
- ✅ Navigation footer
- ✅ CUNY-specific context (system prompt example)
- ✅ No AI slop vocabulary
- ✅ No em dashes

**Voice characteristics:**
- Information-dense but accessible
- Pedagogical framing upfront (5 Model Uses)
- System prompt examples with explanation
- "Going Deeper" for advanced content

**Strengths:**
- Excellent use-case-before-feature framing
- Strong pedagogical scenarios
- Clear separation of basic → advanced content
- Dynamic variables explained in context

**Opportunities:**
- Could add a "Common Patterns" section showing 2-3 complete model configs

---

### Knowledge Bases (Design Kit / Hybrid)

- ✅ Contextual framing before technical details
- ✅ Active voice throughout
- ✅ Short paragraphs (2-4 sentences)
- ✅ Procedural steps numbered with sub-bullet rationale
- ✅ Model Uses separated from procedures
- ✅ Visual placeholders with alt text
- ✅ Cross-links to related pages (Models, Tools)
- ✅ Additional Resources section with external links
- ✅ Navigation footer
- ✅ CUNY-specific context (late submission scenario, multilingual work)
- ✅ No AI slop vocabulary
- ✅ No em dashes
- ✅ Callout box for researchers

**Voice characteristics:**
- Hybrid: warm intro ("The practical name is: the AI reads your stuff first") + dense scenarios
- Concrete scenario to open (late submission question)
- Technical depth in "Going Deeper" without jargon walls
- Plain-language explanation of embeddings

**Strengths:**
- Best balance of warmth and depth across all three pilots
- Strong pedagogical scenarios (5 Model Uses)
- Excellent "Going Deeper" section (embeddings, file quality, management, templates)
- Callout box effectively targets researcher use case

**Opportunities:**
- Could add a "Troubleshooting" section for common RAG issues (poor retrieval, incorrect citations)

---

## Voice Calibration Analysis

### Tone Variation by Kit Type

The three pilots demonstrate that the skill produces appropriate tonal variation:

**Starter Kit (Getting Started):**
- Warmest, most encouraging
- Incremental pacing
- Celebratory moments ("Voila!")
- Lower information density
- Focus on building confidence

**Design Kit (Models, Knowledge Bases):**
- More information-dense
- Scenario-first framing
- Technical depth balanced with accessibility
- Focus on building capability

This variation is **intentional and effective.** It matches the toolkit exemplars:
- Discord Toolkit's Starter Kit has warm, encouraging energy
- AI Toolkit's pedagogical sections are denser and scenario-driven

### Consistency Across Authors

Despite being written by two different agents:
- All three use active voice
- All three avoid AI slop
- All three integrate CUNY context
- All three use numbered procedures with rationale
- All three include visual placeholders

The skill produces consistent results across authors. This validates that the patterns are well-defined and transferable.

---

## Progressive Disclosure Assessment

All three pilots layer information effectively:

**Getting Started:**
1. Overview (What You'll Find Here, Why This Matters)
2. Quick Start (First Login with numbered steps)
3. Exploration (Your First Conversation, Exploring the Interface)
4. Customization (Settings with key options highlighted)
5. Next Steps (What to do after initial setup)
6. Tips (Callout section with best practices)

**Models:**
1. Overview (Why This Matters)
2. Model Uses (5 pedagogical scenarios)
3. Quick Start (Getting Started: 10 numbered steps)
4. Deep Dive (Writing System Prompts with examples)
5. Advanced (Going Deeper: dynamic variables, parameters, switching)

**Knowledge Bases:**
1. Overview (Why This Matters with concrete scenario)
2. Model Uses (5 pedagogical scenarios)
3. Quick Start (Creating a Knowledge Base: steps 1-7)
4. Procedures (Uploading Documents: 8-9, Connecting to Model: 10-13)
5. Deep Dive (Going Deeper: embeddings, file quality, management, templates)

Each pilot allows readers to stop at any depth level. The skill's progressive disclosure pattern works.

---

## Multimedia Integration

All three pilots include visual placeholders with:
- Descriptive alt text
- TODO comments for recording guidance
- Placement at logical breakpoints in procedures

**Recommended next steps:**
1. Record GIFs for key workflows (login, model creation, knowledge base creation)
2. Take screenshots for reference states (interface overview, settings panel)
3. Annotate screenshots where clarification helps (highlighting specific UI elements)

---

## CUNY Context Integration

All three pilots ground features in CUNY's institutional reality:

**Getting Started:**
- "Your students come from diverse linguistic and cultural backgrounds"
- "No third-party tracking. No training on student submissions."
- Links to Teach@CUNY resources

**Models:**
- System prompt example for CUNY context
- References composition, public health, digital humanities
- Acknowledges program handbooks and departmental policies

**Knowledge Bases:**
- Late submission scenario (common CUNY student concern)
- Multilingual source work (reflects CUNY student diversity)
- Program advising use case (graduate handbook, degree requirements)
- IRB protocol mention (research context)

The skill successfully prompts CUNY-specific framing without making it feel forced.

---

## Structural Recommendations

Based on the three pilots, recommend the following directory structure for full calibration:

```
cail-docs/
├── index.md (overview + quick navigation to kits)
├── starter-kit/
│   ├── index.md (kit overview)
│   ├── getting-started.md
│   ├── your-first-model.md (simplified from Models)
│   └── basic-knowledge-base.md (simplified from Knowledge Bases)
├── design-kit/
│   ├── index.md (kit overview)
│   ├── models.md
│   ├── knowledge-bases.md
│   ├── tools-skills.md
│   ├── roles-permissions.md
│   └── advanced-features.md
├── instructional-kit/
│   ├── index.md (kit overview)
│   ├── pedagogical-patterns.md
│   ├── student-onboarding.md
│   ├── assignment-design.md
│   ├── sample-activities.md
│   └── use-cases.md
├── governance/
│   ├── security.md
│   ├── policies.md
│   └── best-practices.md
└── reference/
    ├── troubleshooting.md
    ├── technical-details.md
    └── glossary.md
```

**Rationale:**
- Starter Kit contains simplified, encouraging walkthroughs
- Design Kit contains comprehensive feature documentation
- Instructional Kit focuses on pedagogical integration
- Governance and Reference are separate from the three-kit structure
- Each kit has an index.md that frames the purpose and lists pages

---

## Skill Refinement Recommendations

The `cail-doc-calibrator` skill works well. Minor refinements to consider:

### Add to SKILL.md

1. **Troubleshooting sections** as optional components for Design Kit pages
2. **Common Patterns** sections for showing 2-3 complete configurations
3. **Quick Reference** cards for procedural pages (1-2 paragraph summary at top)

### Add to references/

1. **troubleshooting-template.md** showing how to structure common issues + solutions
2. **quick-reference-template.md** for procedural summary cards

---

## Next Steps

### Immediate (before full calibration)

1. **Finalize directory structure** (propose to milwrite for approval)
2. **Create kit index pages** (overview + navigation for each kit)
3. **Add troubleshooting and quick reference templates** to skill references

### Full Calibration Phase

4. **Extract and categorize** remaining content from current `index.md`
5. **Apply skill to each page** using appropriate kit voice
6. **Create simplified Starter Kit versions** of Models and Knowledge Bases
7. **Write new Instructional Kit pages** (pedagogical patterns, sample activities)
8. **Write Governance and Reference pages** (security, policies, troubleshooting)

### Multimedia Phase

9. **Record GIFs** for key workflows
10. **Take screenshots** for reference states
11. **Annotate images** where helpful

### Testing Phase

12. **Review with CUNY instructors** (if possible) for usability feedback
13. **Iterate based on feedback**
14. **Deploy to static site**

---

## Conclusion

The three pilot pages validate the `cail-doc-calibrator` skill and the three-kit progressive disclosure model. Voice calibration is consistent and effective. Structural patterns work across authors. CUNY context integration is natural.

**Recommendation:** Proceed with full calibration.

---

**Pilots reviewed:**
- `cail-docs/pilot/getting-started.md` (Petrarch, Starter Kit)
- `cail-docs/pilot/models.md` (Quimbot, Design Kit)
- `cail-docs/pilot/knowledge-bases.md` (Quimbot, Design Kit hybrid)

**Skill location:**
- `skills/cail-doc-calibrator/SKILL.md`
- `skills/cail-doc-calibrator/references/`
