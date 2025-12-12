# SlideFlowAI---AI-powered-slide-intelligence

> **Transform ideas into polished presentations instantly.** SlideFlowAI leverages agentic AI workflows to convert raw text into professional, structured PowerPoint presentations in seconds.

**Powered by:** Streamlit • python-pptx • n8n • Google Gemini • Automation-First Design

## 🌟 Overview

Slide Genius is a **production-ready automation tool** that bridges natural language and presentation creation. Simply describe your topic, audience, and style—the system handles slide structure, formatting, bullet optimization, and PPTX generation without manual intervention.

**Perfect for:**
- Content creators & educators (rapid curriculum design)
- Business professionals (pitch decks, reports, training materials)
- Data scientists & researchers (findings presentation)
- Anyone who values time over template hunting

## ⚡ Core Capabilities

| Feature | Details |
|---------|---------|
| **Single-Prompt Generation** | Describe once → Get polished 8-12 slide deck |
| **Intelligent Structure** | Auto-generates Title, Agenda, Content, Summary slides |
| **Audience-Aware Content** | Tailors tone & complexity (students, executives, technical teams) |
| **Bullet Optimization** | Converts paragraphs to crisp bullets (max 5 per slide) |
| **Speaker Notes** | Adds detailed notes for presenter reference |
| **Download-Ready** | Professional .pptx file, fully editable |
| **No Manual Design** | Zero slide tweaking needed—ready to present immediately |

## 🔧 Technology Stack

```
Frontend          │ Streamlit (responsive web UI)
Backend Logic     │ Python 3.8+
Presentation Gen  │ python-pptx (programmatic slide creation)
Orchestration     │ n8n (workflow automation & webhooks)
AI Engine         │ Google Gemini (agentic LLM)
Code Generation   │ Agentic Prompt → Python Code → Execution
```

## 🏗️ Architecture Flow

```
┌──────────────────────────────────────────────────────────┐
│  1. USER INPUT                                           │
│  Streamlit UI: Topic description + Audience type         │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│  2. WEBHOOK TRIGGER (n8n)                                │
│  POST /webhook-test/{webhook_id} with prompt             │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│  3. AGENTIC LLM (Google Gemini)                          │
│  • Analyzes topic & structure                            │
│  • Generates clean Python code                           │ 
│  • Ensures layout compliance (no overlaps, max 5 bullets)│
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│  4. CODE GENERATION & EXECUTION                          │
│  • Save generated code → app1.py                         │
│  • Execute: python app1.py                               │
│  • Output: presentation.pptx                             │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│  5. WEBHOOK RESPONSE                                     │
│  Return generated code + status to Streamlit             │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│  6. DOWNLOAD & PRESENT                                   │
│  User downloads .pptx → Edit/Present as needed           │
└──────────────────────────────────────────────────────────┘
```

## 📋 Project Structure

```
SlideFlow-AI/
├── app.py                          # Streamlit frontend + n8n integration
├── app1.py                         # Generated python-pptx template
├── PPT-generator.json              # n8n workflow export (nodes config)
├── req.txt                         # Python dependencies
├── README.md                       # This file
├── generated/                      # Output folder (presentations saved here)
└── docs/                           # Setup & customization guides (optional)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- pip package manager
- n8n instance (cloud or self-hosted) with active webhook
- Google Gemini API key (or alternative LLM)

### Installation (5 minutes)

**1. Clone & Setup**
```bash
git clone https://github.com/Ruchii151/SlideFlow-AI.git
cd SlideFlow-AI
pip install -r req.txt
```

**2. Configure n8n Workflow**
- Log into your n8n instance
- Go to **Workflows** → **Import**
- Upload `PPT-generator.json`
- Configure Google Gemini credentials (add API key)
- Activate workflow & copy **Webhook URL**

**3. Update Streamlit Config**
Open `app.py` and update line ~60:
```python
WEBHOOK_URL = "https://your-n8n-instance.app.n8n.cloud/webhook-test/YOUR_WEBHOOK_ID"
```

**4. Set Output Path** (line ~150)
```python
pptx_output_path = "generated/presentation.pptx"  # Adjust if needed
```

**5. Run Streamlit App**
```bash
streamlit run app.py
```
Opens at `http://localhost:8501`

## 💡 Usage Examples

### Example 1: College Presentation
```
Topic: Machine Learning Basics
Audience: First-year CS students
Style: Casual, visual examples, simple math
Slides needed: 8

Output: Title → Agenda → What is ML? → Types (Supervised/Unsupervised/RL) 
        → Real-world examples → Key challenges → Summary
```

### Example 2: Corporate Pitch Deck
```
Topic: SaaS Product Launch
Audience: VCs & corporate investors
Style: Formal, data-driven, business metrics
Slides needed: 12

Output: Title → Problem statement → Market size → Solution overview 
        → Product demo → Competitive advantage → Pricing model → Traction → Ask
```

### Example 3: Training Material
```
Topic: Python OOP Concepts
Audience: Mid-level developers
Style: Code examples, best practices
Slides needed: 10

Output: Title → Class fundamentals → Inheritance → Polymorphism 
        → Encapsulation → Design patterns → Q&A
```

## ⚙️ n8n Workflow Configuration

**Key Nodes in `PPT-generator.json`:**

| Node | Purpose | Config |
|------|---------|--------|
| **Webhook** | Receives POST from Streamlit | HTTP Method: POST, Response Mode: "Using Respond to Webhook" |
| **Google Gemini Chat Model** | LLM backend (supports o1, GPT, Claude alternatives) | Add your API credentials |
| **AI Agent** | Agentic orchestrator generating python-pptx code | Custom system prompt for slide rules |
| **Respond to Webhook** | Sends generated code back to Streamlit | Returns JSON with `output` field |

**Critical Prompt Rules (embedded in AI Agent):**
- Output ONLY Python code (no markdown wrapping)
- Max 5 bullets per slide
- Auto-split sections into multiple slides if needed
- Use Calibri font, 44pt titles, 20-22pt body
- Add speaker notes to every slide
- Save as: `presentation.pptx`

## 🎯 Best Practices

### Input Optimization
✅ **Do:**
- Specify slide count ("8-slide presentation")
- Mention audience explicitly ("for MBA students")
- List key sections ("intro, features, pricing, CTA")
- Describe tone ("formal", "storytelling", "data-heavy")

❌ **Don't:**
- Vague prompts ("make a presentation")
- Expect custom branding (generic professional style only)
- Request complex animations (static slides only)
- Mix conflicting tones in one deck

### Customization After Generation
The output `.pptx` is fully editable:
1. Download from Streamlit
2. Open in PowerPoint, Google Slides, or LibreOffice
3. Add logos, brand colors, custom fonts
4. Adjust speaker notes
5. Insert images/charts as needed

## 📧 Support & Feedback

Have questions or found a bug? 
- **Email:** pruchita565@gmail.com
- **Twitter:** [ruchita_patil15](https://x.com/ruchita_patil15)
- **LinkedIn:** www.linkedin.com/in/patil-ruchita

**Made with ❤️ to make presentations effortless.**

⭐ If Slide Genius saved you time, please star this repo!
