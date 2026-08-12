import streamlit as st

st.set_page_config(
    page_title="Abdullah Mehmood | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html {
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0,255,255,.08), transparent 30%),
        radial-gradient(circle at 90% 80%, rgba(123,97,255,.10), transparent 30%),
        #050816;
    color: white;
}

header,
#MainMenu,
footer {
    visibility: hidden;
}

* {
    font-family: 'Inter', sans-serif;
    box-sizing: border-box;
}

/* ================= NAVBAR ================= */

.navbar {
    width: 92%;
    max-width: 1200px;
    margin: 20px auto 40px;
    padding: 16px 25px;

    display: flex;
    justify-content: space-between;
    align-items: center;

    background: rgba(8,13,35,.80);
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 18px;

    backdrop-filter: blur(20px);

    box-shadow: 0 15px 50px rgba(0,0,0,.35);
}

.logo {
    color: #00ffff;
    font-size: 22px;
    font-weight: 800;
    text-shadow: 0 0 15px rgba(0,255,255,.7);
}

.nav-links {
    display: flex;
    gap: 25px;
}

.nav-links a {
    color: #aab4d4;
    text-decoration: none;
    font-size: 14px;
    transition: .3s;
}

.nav-links a:hover {
    color: #00ffff;
}

/* ================= HERO ================= */

.hero {
    width: 90%;
    max-width: 1200px;
    min-height: 620px;
    margin: auto;

    display: grid;
    grid-template-columns: 1.1fr .9fr;
    gap: 60px;
    align-items: center;
}

.badge {
    display: inline-block;
    padding: 8px 15px;
    border: 1px solid rgba(0,255,255,.3);
    border-radius: 30px;
    color: #00ffff;
    background: rgba(0,255,255,.05);
    font-size: 12px;
    letter-spacing: 1px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    50% {
        box-shadow: 0 0 30px rgba(0,255,255,.25);
    }
}

.hero h1 {
    font-size: clamp(45px,6vw,75px);
    line-height: 1.05;
    margin: 25px 0;
}

.gradient {
    background: linear-gradient(
        90deg,
        #00ffff,
        #7b61ff,
        #ff4ecd
    );

    background-size: 200% auto;

    -webkit-background-clip: text;
    background-clip: text;

    color: transparent;

    animation: gradient 4s linear infinite;
}

@keyframes gradient {
    to {
        background-position: 200% center;
    }
}

.hero-text {
    color: #9ca7c7;
    font-size: 18px;
    line-height: 1.8;
    max-width: 680px;
}

.typing {
    color: #00ffff;
    font-weight: 700;
}

/* ================= BUTTONS ================= */

.buttons {
    margin-top: 30px;
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;
    padding: 14px 22px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    transition: .3s;
}

.primary {
    color: #001014;
    background: #00ffff;
    box-shadow: 0 0 25px rgba(0,255,255,.3);
}

.secondary {
    color: white;
    background: rgba(255,255,255,.05);
    border: 1px solid rgba(255,255,255,.15);
}

.btn:hover {
    transform: translateY(-5px);
}

/* ================= PROFILE ================= */

.profile {
    max-width: 390px;
    margin: auto;
    padding: 35px;

    border-radius: 30px;

    background: linear-gradient(
        145deg,
        rgba(255,255,255,.08),
        rgba(255,255,255,.02)
    );

    border: 1px solid rgba(255,255,255,.12);

    backdrop-filter: blur(20px);

    box-shadow: 0 30px 80px rgba(0,0,0,.5);

    transition: .4s;
}

.profile:hover {
    transform: translateY(-10px);
}

.avatar {
    width: 125px;
    height: 125px;
    margin: auto auto 25px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: linear-gradient(
        135deg,
        #00ffff,
        #7b61ff,
        #ff4ecd
    );

    font-size: 40px;
    font-weight: 800;

    box-shadow: 0 0 45px rgba(0,255,255,.35);

    animation: float 4s ease-in-out infinite;
}

@keyframes float {
    50% {
        transform: translateY(-12px);
    }
}

.profile h2 {
    text-align: center;
}

.role {
    color: #00ffff;
    text-align: center;
}

.location {
    color: #8994b4;
    text-align: center;
}

.status {
    text-align: center;
    color: #aab4d4;
    margin: 25px 0;
}

.status-dot {
    display: inline-block;
    width: 9px;
    height: 9px;
    background: #00ff88;
    border-radius: 50%;
    box-shadow: 0 0 15px #00ff88;
}

.info {
    display: flex;
    justify-content: space-between;

    padding: 12px;
    margin: 9px 0;

    border-radius: 10px;
    background: rgba(255,255,255,.04);

    color: #9ca7c7;
    font-size: 13px;
}

.info span:last-child {
    color: #00ffff;
}

/* ================= SECTIONS ================= */

.section {
    width: 90%;
    max-width: 1200px;
    margin: 120px auto;
}

.section-title {
    text-align: center;
    margin-bottom: 50px;
}

.section-title h2 {
    font-size: clamp(32px,5vw,48px);
}

.section-title p {
    color: #7f8aaa;
}

/* ================= CARDS ================= */

.cards {
    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 25px;
}

.card {
    padding: 30px;

    border-radius: 22px;

    background: rgba(255,255,255,.04);

    border: 1px solid rgba(255,255,255,.08);

    transition: .4s;
}

.card:hover {
    transform: translateY(-8px);
    border-color: rgba(0,255,255,.35);
    box-shadow: 0 25px 60px rgba(0,0,0,.25);
}

.card h3 {
    color: #00ffff;
}

.card p {
    color: #9ca7c7;
    line-height: 1.8;
}

/* ================= SKILLS ================= */

.skills {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 18px;
}

.skill {
    padding: 25px;

    border-radius: 20px;

    background: rgba(255,255,255,.04);

    border: 1px solid rgba(255,255,255,.08);

    transition: .35s;
}

.skill:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,255,255,.4);
}

.skill-icon {
    font-size: 35px;
}

.skill h3 {
    margin: 12px 0 8px;
}

.skill p {
    color: #8792b2;
    font-size: 14px;
}

/* ================= PROJECTS ================= */

.projects {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 25px;
}

.project {
    min-height: 530px;

    display: flex;
    flex-direction: column;

    padding: 28px;

    border-radius: 24px;

    background: linear-gradient(
        145deg,
        rgba(255,255,255,.07),
        rgba(255,255,255,.025)
    );

    border: 1px solid rgba(255,255,255,.10);

    transition: .45s;
}

.project:hover {
    transform: translateY(-12px);
    border-color: rgba(0,255,255,.4);
    box-shadow: 0 30px 70px rgba(0,0,0,.4);
}

.number {
    color: #00ffff;
    font-size: 12px;
    letter-spacing: 2px;
}

.project-icon {
    width: 60px;
    height: 60px;

    margin: 20px 0;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 15px;

    background: rgba(0,255,255,.08);

    border: 1px solid rgba(0,255,255,.2);

    font-size: 28px;
}

.project h3 {
    font-size: 21px;
}

.project > p {
    color: #909abb;
    line-height: 1.7;
    font-size: 14px;
}

.feature {
    color: #00ffff;
    font-size: 12px;
    margin-top: 10px;
}

.project ul {
    padding-left: 0;
    list-style: none;
}

.project li {
    color: #9ca7c7;
    font-size: 13px;
    margin: 8px 0;
}

.project li::before {
    content: "✓ ";
    color: #00ff88;
}

.project-link {
    margin-top: auto;

    text-align: center;

    padding: 12px;

    border-radius: 10px;

    color: #00ffff;

    text-decoration: none;

    border: 1px solid rgba(0,255,255,.25);

    background: rgba(0,255,255,.05);

    transition: .3s;
}

.project-link:hover {
    background: #00ffff;
    color: #001014;
}

/* ================= TIMELINE ================= */

.timeline {
    max-width: 850px;
    margin: auto;
}

.timeline-item {
    position: relative;
    padding: 0 0 30px 45px;
    border-left: 2px solid #00ffff;
}

.timeline-dot {
    position: absolute;

    left: -9px;
    top: 0;

    width: 16px;
    height: 16px;

    border-radius: 50%;

    background: #00ffff;

    box-shadow: 0 0 20px #00ffff;
}

.timeline-card {
    padding: 25px;

    border-radius: 18px;

    background: rgba(255,255,255,.04);

    border: 1px solid rgba(255,255,255,.08);
}

.timeline-date {
    color: #00ffff;
    font-size: 13px;
}

.timeline-card p {
    color: #8994b4;
}

/* ================= CONTACT ================= */

.contact {
    max-width: 900px;
    margin: auto;

    padding: 50px;

    text-align: center;

    border-radius: 25px;

    background: linear-gradient(
        145deg,
        rgba(0,255,255,.07),
        rgba(123,97,255,.07)
    );

    border: 1px solid rgba(255,255,255,.10);
}

.contact h2 {
    font-size: 40px;
}

.contact p {
    color: #8994b4;
}

.contact-info {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin: 30px 0;
}

.contact-item {
    padding: 12px 18px;

    border-radius: 10px;

    background: rgba(255,255,255,.05);

    color: #c2cbe5;

    font-size: 13px;
}

.contact-item strong {
    color: #00ffff;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;

    padding: 45px 20px;

    margin-top: 100px;

    border-top: 1px solid rgba(255,255,255,.08);

    color: #69738f;
}

.footer span {
    color: #00ffff;
}

/* ================= RESPONSIVE ================= */

@media(max-width:1000px) {

    .hero {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .hero-text {
        margin: auto;
    }

    .buttons {
        justify-content: center;
    }

    .skills {
        grid-template-columns: repeat(2,1fr);
    }

    .projects {
        grid-template-columns: 1fr;
    }
}

@media(max-width:700px) {

    .navbar {
        width: 95%;
    }

    .nav-links {
        display: none;
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .skills {
        grid-template-columns: 1fr;
    }

    .profile {
        width: 100%;
    }

    .contact {
        padding: 30px 20px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVBAR
# =========================================================

st.markdown("""
<div class="navbar">

    <div class="logo">
        &lt;ABDULLAH/&gt;
    </div>

    <div class="nav-links">

        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero" id="home">

    <div>

        <div class="badge">
            ● IT STUDENT • AI TOOLS DEVELOPER
        </div>

        <h1>
            Hi, I'm<br>
            <span class="gradient">
                ABDULLAH MEHMOOD
            </span>
        </h1>

        <p class="hero-text">

            I'm an IT student who loves building
            useful applications for the web.

            My current focus is
            <span class="typing">
                AI, Web Development & Python
            </span>.

            I enjoy turning ideas into working
            digital products.

        </p>

        <div class="buttons">

            <a href="#projects" class="btn primary">
                View My Projects →
            </a>

            <a href="#contact" class="btn secondary">
                Contact Me
            </a>

        </div>

    </div>


    <div class="profile">

        <div class="avatar">
            AM
        </div>

        <h2>
            Abdullah Mehmood
        </h2>

        <p class="role">
            IT Student | AI Tools Developer
        </p>

        <p class="location">
            📍 Multan Cantt, Pakistan
        </p>

        <div class="status">
            <span class="status-dot"></span>
            Currently Learning & Building
        </div>

        <div class="info">
            <span>🎓 Degree</span>
            <span>BS IT</span>
        </div>

        <div class="info">
            <span>🏫 University</span>
            <span>UE Lahore</span>
        </div>

        <div class="info">
            <span>🤖 Focus</span>
            <span>AI & Web</span>
        </div>

        <div class="info">
            <span>📅 Session</span>
            <span>2024–2028</span>
        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# ABOUT
# =========================================================

st.markdown("""
<div class="section" id="about">

    <div class="section-title">

        <h2>
            About <span class="gradient">Me</span>
        </h2>

        <p>
            A little more about my journey
        </p>

    </div>

    <div class="cards">

        <div class="card">

            <h3>👨‍💻 Who I Am</h3>

            <p>

                Hi, I'm Abdullah Mehmood, an IT student
                at the University of Education Lahore,
                Multan Campus.

                I love building web applications,
                experimenting with AI and learning
                modern technologies.

            </p>

        </div>

        <div class="card">

            <h3>🚀 My Approach</h3>

            <p>

                I'm always learning and turning ideas
                into working projects.

                My interests include web development,
                AI-powered applications, e-commerce,
                digital marketing and emerging
                technologies.

            </p>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SKILLS
# =========================================================

st.markdown("""
<div class="section" id="skills">

    <div class="section-title">

        <h2>
            Technical <span class="gradient">Skills</span>
        </h2>

        <p>
            Technologies and skills I work with
        </p>

    </div>

    <div class="skills">

        <div class="skill">
            <div class="skill-icon">🌐</div>
            <h3>HTML5</h3>
            <p>Modern semantic web structure.</p>
        </div>

        <div class="skill">
            <div class="skill-icon">🎨</div>
            <h3>CSS3</h3>
            <p>Responsive design and animations.</p>
        </div>

        <div class="skill">
            <div class="skill-icon">⚡</div>
            <h3>JavaScript</h3>
            <p>Interactive frontend experiences.</p>
        </div>

        <div class="skill">
            <div class="skill-icon">🐍</div>
            <h3>Python</h3>
            <p>AI, automation and applications.</p>
        </div>

        <div class="skill">
            <div class="skill-icon">⚛️</div>
            <h3>React</h3>
            <p>Modern component-based UI.</p>
        </div>

        <div class="skill">
            <div class="skill-icon">🗄️</div>
            <h3>SQL</h3>
            <p>Database queries and management.</p>
        </div>

        <div class="skill">
            <div class="skill-icon">🔧</div>
            <h3>Git & GitHub</h3>
            <p>Version control and collaboration.</p>
        </div>

        <div class="skill">
            <div class="skill-icon">🤖</div>
            <h3>Prompt Engineering</h3>
            <p>Effective AI-powered workflows.</p>
        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# PROJECTS
# =========================================================

st.markdown("""
<div class="section" id="projects">

    <div class="section-title">

        <h2>
            Featured <span class="gradient">Projects</span>
        </h2>

        <p>
            AI-powered applications I've built
        </p>

    </div>

    <div class="projects">


        <!-- PROJECT 1 -->

        <div class="project">

            <div class="number">
                PROJECT 01
            </div>

            <div class="project-icon">
                📚
            </div>

            <h3>
                AI Research Paper Summarizer
            </h3>

            <p>

                An AI-powered research assistant
                that summarizes research papers
                and helps analyze potentially
                plagiarized content.

            </p>

            <div class="feature">
                CORE FEATURES
            </div>

            <ul>

                <li>PDF/DOCX paper input</li>
                <li>Automatic summary</li>
                <li>Plagiarism analysis</li>
                <li>Highlighted matched content</li>
                <li>Rephrasing suggestions</li>
                <li>Citation checking</li>

            </ul>

            <a
                class="project-link"
                href="https://ai-driven-research-paper-summarizer-plagiarism-corrector-9pdyf.streamlit.app/"
                target="_blank">

                Launch Project ↗

            </a>

        </div>


        <!-- PROJECT 2 -->

        <div class="project">

            <div class="number">
                PROJECT 02
            </div>

            <div class="project-icon">
                🧠
            </div>

            <h3>
                AI Mentor for Learning
            </h3>

            <p>

                A personalized AI learning assistant
                designed to help students create
                study plans and improve their
                learning process.

            </p>

            <div class="feature">
                CORE FEATURES
            </div>

            <ul>

                <li>User learning profile</li>
                <li>Personalized study roadmap</li>
                <li>AI Q&A assistant</li>
                <li>Progress tracking</li>
                <li>Quiz-based learning</li>
                <li>Adaptive difficulty</li>

            </ul>

            <a
                class="project-link"
                href="https://ai-mentor-for-learning-personalized-learning-assistant-odcr4p9.streamlit.app/"
                target="_blank">

                Launch Project ↗

            </a>

        </div>


        <!-- PROJECT 3 -->

        <div class="project">

            <div class="number">
                PROJECT 03
            </div>

            <div class="project-icon">
                💻
            </div>

            <h3>
                AI Code Reviewer
            </h3>

            <p>

                An intelligent code-review assistant
                that detects bugs, explains problems
                and suggests improvements.

            </p>

            <div class="feature">
                CORE FEATURES
            </div>

            <ul>

                <li>Code paste/upload</li>
                <li>Bug detection</li>
                <li>Line-by-line explanations</li>
                <li>Code quality suggestions</li>
                <li>Before/after comparison</li>
                <li>Multiple languages</li>

            </ul>

            <a
                class="project-link"
                href="https://ai-powered-code-reviewer-bug-explainer-uus4oprxmhrasquzwbqwzb.streamlit.app/"
                target="_blank">

                Launch Project ↗

            </a>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# EDUCATION
# =========================================================

st.markdown("""
<div class="section" id="education">

    <div class="section-title">

        <h2>
            Education <span class="gradient">& Journey</span>
        </h2>

        <p>
            My academic background
        </p>

    </div>

    <div class="timeline">

        <div class="timeline-item">

            <div class="timeline-dot"></div>

            <div class="timeline-card">

                <h3>
                    BS Information Technology
                </h3>

                <div class="timeline-date">
                    2024 – 2028
                </div>

                <p>
                    University of Education Lahore,
                    Multan Campus
                </p>

                <p>
                    CGPA: 3.09
                </p>

            </div>

        </div>

        <div class="timeline-item">

            <div class="timeline-dot"></div>

            <div class="timeline-card">

                <h3>
                    Local E-Commerce Course
                </h3>

                <div class="timeline-date">
                    Completed
                </div>

                <p>
                    Hands-on experience with
                    online stores and e-commerce
                    operations.
                </p>

            </div>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# CONTACT
# =========================================================

st.markdown("""
<div class="section" id="contact">

    <div class="contact">

        <h2>
            Let's Build Something
            <span class="gradient">Great</span>
        </h2>

        <p>
            Have a project, internship opportunity,
            or collaboration idea?
        </p>

        <div class="contact-info">

            <div class="contact-item">
                📧 <strong>Email</strong><br>
                abdullahmehmood2n4l@gmail.com
            </div>

            <div class="contact-item">
                📱 <strong>Phone</strong><br>
                03267636648
            </div>

            <div class="contact-item">
                📍 <strong>Location</strong><br>
                Multan Cantt
            </div>

        </div>

        <div class="buttons" style="justify-content:center;">

            <a
                href="mailto:abdullahmehmood2n4l@gmail.com"
                class="btn primary">

                Send Me an Email ✉

            </a>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    Designed & Built by
    <span>Abdullah Mehmood</span>

    <br><br>

    HTML • CSS • JavaScript • Python • AI

    <br><br>

    © 2026 Abdullah Mehmood

</div>
""", unsafe_allow_html=True)
