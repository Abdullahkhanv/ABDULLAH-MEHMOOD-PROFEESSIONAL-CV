import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Abdullah Mehmood | IT Student & AI Tools Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


/* =========================================================
   GLOBAL
========================================================= */

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: 'Inter', sans-serif;
    background: #050816;
    color: white;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0,255,255,0.08),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 80%,
            rgba(123,97,255,0.10),
            transparent 30%
        ),
        #050816;
}


/* =========================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stDeployButton {
    display: none;
}


/* =========================================================
   NAVBAR
========================================================= */

.navbar {

    width: 92%;
    max-width: 1200px;

    margin: 20px auto 40px;

    padding: 15px 25px;

    display: flex;

    justify-content: space-between;

    align-items: center;

    border-radius: 18px;

    border: 1px solid
        rgba(255,255,255,0.10);

    background:
        rgba(8,13,35,0.75);

    backdrop-filter:
        blur(20px);

    box-shadow:
        0 15px 50px
        rgba(0,0,0,0.35);

    position: sticky;

    top: 15px;

    z-index: 999;
}


.logo {

    color: #00ffff;

    font-size: 21px;

    font-weight: 800;

    text-shadow:
        0 0 15px
        rgba(0,255,255,0.6);
}


.nav-links {

    display: flex;

    gap: 25px;
}


.nav-links a {

    color: #aab4d4;

    text-decoration: none;

    font-size: 14px;

    transition: 0.3s;
}


.nav-links a:hover {

    color: #00ffff;

    text-shadow:
        0 0 12px #00ffff;
}


/* =========================================================
   HERO
========================================================= */

.hero {

    width: 90%;

    max-width: 1200px;

    min-height: 650px;

    margin: auto;

    display: grid;

    grid-template-columns:
        1.1fr 0.9fr;

    gap: 70px;

    align-items: center;
}


.badge {

    display: inline-block;

    padding: 8px 15px;

    margin-bottom: 20px;

    border:
        1px solid
        rgba(0,255,255,0.35);

    border-radius: 30px;

    color: #00ffff;

    background:
        rgba(0,255,255,0.05);

    font-size: 12px;

    letter-spacing: 1px;

    animation:
        pulseBadge 2s infinite;
}


@keyframes pulseBadge {

    50% {
        box-shadow:
            0 0 25px
            rgba(0,255,255,0.20);
    }
}


.hero h1 {

    font-size:
        clamp(45px,6vw,76px);

    line-height: 1.05;

    margin-bottom: 20px;

    color: white;
}


.gradient {

    background:
        linear-gradient(
            90deg,
            #00ffff,
            #7b61ff,
            #ff4ecd
        );

    background-size:
        200% auto;

    -webkit-background-clip:
        text;

    background-clip:
        text;

    color: transparent;

    animation:
        gradientMove 4s linear infinite;
}


@keyframes gradientMove {

    to {
        background-position:
            200% center;
    }
}


.hero-text {

    color: #9ca7c7;

    font-size: 18px;

    line-height: 1.8;

    max-width: 680px;

    margin-bottom: 25px;
}


.typing {

    color: #00ffff;

    font-weight: 700;
}


/* =========================================================
   BUTTONS
========================================================= */

.button-row {

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

    transition:
        0.35s ease;
}


.primary-btn {

    color: #001014;

    background: #00ffff;

    box-shadow:
        0 0 25px
        rgba(0,255,255,0.30);
}


.secondary-btn {

    color: white;

    background:
        rgba(255,255,255,0.05);

    border:
        1px solid
        rgba(255,255,255,0.15);
}


.btn:hover {

    transform:
        translateY(-5px);
}


.primary-btn:hover {

    box-shadow:
        0 0 45px
        rgba(0,255,255,0.65);
}


.secondary-btn:hover {

    border-color:
        #00ffff;
}


/* =========================================================
   PROFILE CARD
========================================================= */

.profile-card {

    width: 390px;

    max-width: 100%;

    margin: auto;

    padding: 35px;

    border-radius: 30px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.08),
            rgba(255,255,255,0.02)
        );

    border:
        1px solid
        rgba(255,255,255,0.13);

    backdrop-filter:
        blur(20px);

    box-shadow:
        0 30px 80px
        rgba(0,0,0,0.5);

    transition:
        0.4s ease;
}


.profile-card:hover {

    transform:
        translateY(-10px);

    box-shadow:
        0 40px 100px
        rgba(0,0,0,0.6),
        0 0 40px
        rgba(0,255,255,0.12);
}


.avatar {

    width: 125px;

    height: 125px;

    margin:
        0 auto 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    font-size: 42px;

    font-weight: 800;

    background:
        linear-gradient(
            135deg,
            #00ffff,
            #7b61ff,
            #ff4ecd
        );

    box-shadow:
        0 0 45px
        rgba(0,255,255,0.3);

    animation:
        avatarFloat 4s
        ease-in-out infinite;
}


@keyframes avatarFloat {

    50% {
        transform:
            translateY(-12px);
    }
}


.profile-card h2 {

    text-align: center;

    font-size: 26px;

    margin-bottom: 5px;
}


.role {

    text-align: center;

    color: #00ffff;

    margin-bottom: 5px;
}


.location {

    text-align: center;

    color: #8994b4;

    margin-bottom: 25px;
}


.status {

    display: flex;

    justify-content: center;

    align-items: center;

    gap: 8px;

    color: #aab4d4;

    margin-bottom: 25px;

    font-size: 13px;
}


.status-dot {

    width: 9px;

    height: 9px;

    border-radius: 50%;

    background: #00ff88;

    box-shadow:
        0 0 15px #00ff88;

    animation:
        statusPulse 1.5s infinite;
}


@keyframes statusPulse {

    50% {
        transform:
            scale(1.5);

        opacity: 0.5;
    }
}


.info-item {

    display: flex;

    justify-content: space-between;

    padding: 11px 13px;

    margin-bottom: 10px;

    border-radius: 10px;

    background:
        rgba(255,255,255,0.04);

    color: #9ca7c7;

    font-size: 13px;

    transition: 0.3s;
}


.info-item:hover {

    transform:
        translateX(5px);

    background:
        rgba(0,255,255,0.06);
}


.info-item span:last-child {

    color: #00ffff;
}


/* =========================================================
   SECTION
========================================================= */

.section {

    width: 90%;

    max-width: 1200px;

    margin:
        120px auto;
}


.section-title {

    text-align: center;

    margin-bottom: 50px;
}


.section-title h2 {

    font-size:
        clamp(32px,5vw,48px);

    margin-bottom: 10px;
}


.section-title p {

    color: #7f8aaa;
}


/* =========================================================
   GLASS CARDS
========================================================= */

.glass-card {

    padding: 30px;

    border-radius: 22px;

    background:
        rgba(255,255,255,0.04);

    border:
        1px solid
        rgba(255,255,255,0.08);

    transition: 0.4s;
}


.glass-card:hover {

    transform:
        translateY(-8px);

    border-color:
        rgba(0,255,255,0.3);

    box-shadow:
        0 25px 60px
        rgba(0,0,0,0.25);
}


.glass-card h3 {

    color: #00ffff;

    margin-bottom: 15px;
}


.glass-card p {

    color: #9ca7c7;

    line-height: 1.8;
}


/* =========================================================
   SKILLS
========================================================= */

.skills-grid {

    display: grid;

    grid-template-columns:
        repeat(4,1fr);

    gap: 18px;
}


.skill-card {

    padding: 25px;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.04);

    border:
        1px solid
        rgba(255,255,255,0.08);

    transition: 0.4s;
}


.skill-card:hover {

    transform:
        translateY(-10px)
        scale(1.02);

    border-color:
        rgba(0,255,255,0.4);

    background:
        rgba(0,255,255,0.05);
}


.skill-icon {

    font-size: 35px;

    margin-bottom: 12px;
}


.skill-card h3 {

    margin-bottom: 7px;
}


.skill-card p {

    color: #8792b2;

    font-size: 14px;
}


/* =========================================================
   PROJECTS
========================================================= */

.projects-grid {

    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 25px;
}


.project-card {

    display: flex;

    flex-direction: column;

    min-height: 540px;

    padding: 28px;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.07),
            rgba(255,255,255,0.025)
        );

    border:
        1px solid
        rgba(255,255,255,0.10);

    transition:
        0.45s
        cubic-bezier(
            .22,1,.36,1
        );
}


.project-card:hover {

    transform:
        translateY(-12px);

    border-color:
        rgba(0,255,255,0.4);

    box-shadow:
        0 30px 70px
        rgba(0,0,0,0.4);
}


.project-number {

    color: #00ffff;

    font-size: 12px;

    letter-spacing: 2px;

    margin-bottom: 15px;
}


.project-icon {

    width: 60px;

    height: 60px;

    display: flex;

    justify-content: center;

    align-items: center;

    border-radius: 15px;

    font-size: 28px;

    margin-bottom: 20px;

    background:
        rgba(0,255,255,0.08);

    border:
        1px solid
        rgba(0,255,255,0.2);
}


.project-card h3 {

    font-size: 21px;

    margin-bottom: 12px;
}


.project-card > p {

    color: #909abb;

    font-size: 14px;

    line-height: 1.7;

    margin-bottom: 18px;
}


.feature-title {

    color: #00ffff;

    font-size: 12px;

    margin-bottom: 10px;
}


.features {

    list-style: none;

    padding: 0;

    margin-bottom: 25px;
}


.features li {

    color: #9ca7c7;

    font-size: 13px;

    margin-bottom: 7px;
}


.features li::before {

    content: "✓";

    color: #00ff88;

    margin-right: 8px;

    font-weight: bold;
}


.project-link {

    margin-top: auto;

    display: block;

    text-align: center;

    padding: 12px;

    border-radius: 10px;

    color: #00ffff;

    border:
        1px solid
        rgba(0,255,255,0.25);

    background:
        rgba(0,255,255,0.05);

    text-decoration: none;

    transition: 0.3s;
}


.project-link:hover {

    background: #00ffff;

    color: #001014;

    box-shadow:
        0 0 25px
        rgba(0,255,255,0.35);
}


/* =========================================================
   TIMELINE
========================================================= */

.timeline {

    max-width: 850px;

    margin: auto;

    position: relative;
}


.timeline::before {

    content: "";

    position: absolute;

    left: 20px;

    top: 0;

    bottom: 0;

    width: 2px;

    background:
        linear-gradient(
            #00ffff,
            #7b61ff,
            transparent
        );
}


.timeline-item {

    position: relative;

    padding:
        0 0 35px 60px;
}


.timeline-dot {

    position: absolute;

    left: 12px;

    top: 5px;

    width: 18px;

    height: 18px;

    border-radius: 50%;

    background: #00ffff;

    box-shadow:
        0 0 20px #00ffff;
}


.timeline-card {

    padding: 25px;

    border-radius: 18px;

    background:
        rgba(255,255,255,0.04);

    border:
        1px solid
        rgba(255,255,255,0.08);

    transition: 0.3s;
}


.timeline-card:hover {

    transform:
        translateX(8px);

    border-color:
        rgba(0,255,255,0.35);
}


.timeline-card h3 {

    margin-bottom: 5px;
}


.timeline-date {

    color: #00ffff;

    font-size: 13px;

    margin-bottom: 10px;
}


.timeline-card p {

    color: #8994b4;
}


/* =========================================================
   EXPERIENCE
========================================================= */

.experience-grid {

    display: grid;

    grid-template-columns:
        repeat(2,1fr);

    gap: 20px;
}


.experience-card {

    padding: 25px;

    border-radius: 18px;

    background:
        rgba(255,255,255,0.04);

    border:
        1px solid
        rgba(255,255,255,0.08);

    transition: 0.3s;
}


.experience-card:hover {

    transform:
        translateY(-7px);

    border-color:
        rgba(0,255,255,0.3);
}


.experience-card h3 {

    margin-bottom: 5px;
}


.company {

    color: #00ffff;

    font-size: 14px;

    margin-bottom: 8px;
}


.experience-card p {

    color: #8994b4;

    font-size: 14px;
}


/* =========================================================
   CONTACT
========================================================= */

.contact-card {

    max-width: 900px;

    margin: auto;

    padding: 45px;

    text-align: center;

    border-radius: 25px;

    background:
        linear-gradient(
            145deg,
            rgba(0,255,255,0.07),
            rgba(123,97,255,0.07)
        );

    border:
        1px solid
        rgba(255,255,255,0.10);
}


.contact-card h2 {

    font-size: 40px;

    margin-bottom: 12px;
}


.contact-card p {

    color: #8994b4;

    margin-bottom: 25px;
}


.contact-details {

    display: flex;

    justify-content: center;

    flex-wrap: wrap;

    gap: 12px;

    margin-bottom: 30px;
}


.contact-item {

    padding: 12px 18px;

    border-radius: 10px;

    background:
        rgba(255,255,255,0.05);

    color: #c2cbe5;

    font-size: 13px;
}


.contact-item span {

    color: #00ffff;
}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align: center;

    padding: 40px 20px;

    border-top:
        1px solid
        rgba(255,255,255,0.08);

    color: #69738f;
}


.footer span {

    color: #00ffff;
}


/* =========================================================
   RESPONSIVE
========================================================= */

@media(max-width:1000px) {

    .hero {

        grid-template-columns: 1fr;

        text-align: center;

        padding: 80px 0;
    }

    .hero-text {

        margin-left: auto;

        margin-right: auto;
    }

    .button-row {

        justify-content: center;
    }

    .skills-grid {

        grid-template-columns:
            repeat(2,1fr);
    }

    .projects-grid {

        grid-template-columns:
            1fr;
    }

}


@media(max-width:700px) {

    .navbar {

        width: 95%;
    }

    .nav-links {

        display: none;
    }

    .skills-grid {

        grid-template-columns:
            1fr;
    }

    .experience-grid {

        grid-template-columns:
            1fr;
    }

    .profile-card {

        width: 100%;
    }

    .contact-card {

        padding: 30px 20px;
    }

    .contact-card h2 {

        font-size: 30px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# JAVASCRIPT ANIMATIONS
# ============================================================

components.html("""
<script>

const words = [
    "AI Tools Developer",
    "Web Developer",
    "Python Developer",
    "Digital Marketer",
    "IT Student"
];

let wordIndex = 0;
let charIndex = 0;
let deleting = false;

function typeEffect() {

    const element =
        window.parent.document.getElementById("typing");

    if (!element) {
        setTimeout(typeEffect, 300);
        return;
    }

    const word = words[wordIndex];

    if (!deleting) {

        element.innerHTML =
            word.substring(0, charIndex + 1);

        charIndex++;

        if (charIndex === word.length) {

            deleting = true;

            setTimeout(typeEffect, 1200);

            return;
        }

    } else {

        element.innerHTML =
            word.substring(0, charIndex - 1);

        charIndex--;

        if (charIndex === 0) {

            deleting = false;

            wordIndex++;

            if (wordIndex >= words.length) {
                wordIndex = 0;
            }
        }
    }

    setTimeout(
        typeEffect,
        deleting ? 60 : 90
    );
}

typeEffect();

</script>
""", height=0)


# ============================================================
# NAVIGATION
# ============================================================

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


# ============================================================
# HERO
# ============================================================

st.markdown("""
<section class="hero" id="home">

    <div>

        <div class="badge">
            ● IT STUDENT • AI TOOLS DEVELOPER
        </div>

        <h1>

            Hi, I'm

            <br>

            <span class="gradient">
                ABDULLAH MEHMOOD
            </span>

        </h1>

        <p class="hero-text">

            I'm an IT student and aspiring

            <span
                class="typing"
                id="typing">
                AI Tools Developer
            </span>

            who loves building useful web
            applications, AI-powered tools
            and digital solutions.

        </p>

        <div class="button-row">

            <a
                href="#projects"
                class="btn primary-btn">

                View My Projects →

            </a>

            <a
                href="#contact"
                class="btn secondary-btn">

                Contact Me

            </a>

        </div>

    </div>


    <div class="profile-card">

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
            📍 Multan, Pakistan
        </p>

        <div class="status">

            <span class="status-dot"></span>

            Currently Learning & Building

        </div>


        <div class="info-item">

            <span>🎓 Degree</span>

            <span>BS IT</span>

        </div>


        <div class="info-item">

            <span>🏫 University</span>

            <span>UE Lahore</span>

        </div>


        <div class="info-item">

            <span>🤖 Focus</span>

            <span>AI & Web</span>

        </div>


        <div class="info-item">

            <span>📅 Session</span>

            <span>2024–2028</span>

        </div>

    </div>

</section>
""", unsafe_allow_html=True)


# ============================================================
# ABOUT
# ============================================================

st.markdown("""
<section class="section" id="about">

    <div class="section-title">

        <h2>
            About
            <span class="gradient">Me</span>
        </h2>

        <p>
            A little more about my journey
        </p>

    </div>


    <div style="
        display:grid;
        grid-template-columns:repeat(2,1fr);
        gap:25px;
    ">

        <div class="glass-card">

            <h3>
                👨‍💻 Who I Am
            </h3>

            <p>

                Hi, I'm Abdullah Mehmood,
                an IT student at the University
                of Education Lahore, Multan Campus.

                I enjoy building things for the web
                and experimenting with artificial
                intelligence and modern technologies.

            </p>

        </div>


        <div class="glass-card">

            <h3>
                🚀 My Approach
            </h3>

            <p>

                I'm always learning and turning
                ideas into working projects.

                My interests include web development,
                AI-powered applications, digital
                marketing, e-commerce and emerging
                technologies.

            </p>

        </div>

    </div>

</section>
""", unsafe_allow_html=True)


# ============================================================
# SKILLS
# ============================================================

st.markdown("""
<section class="section" id="skills">

    <div class="section-title">

        <h2>
            Technical
            <span class="gradient">Skills</span>
        </h2>

        <p>
            Technologies and professional skills
        </p>

    </div>


    <div class="skills-grid">


        <div class="skill-card">

            <div class="skill-icon">🌐</div>

            <h3>HTML5</h3>

            <p>
                Semantic and responsive
                web structures.
            </p>

        </div>


        <div class="skill-card">

            <div class="skill-icon">🎨</div>

            <h3>CSS3</h3>

            <p>
                Modern layouts, animations,
                transitions and responsive UI.
            </p>

        </div>


        <div class="skill-card">

            <div class="skill-icon">⚡</div>

            <h3>JavaScript</h3>

            <p>
                Interactive interfaces,
                DOM and frontend animations.
            </p>

        </div>


        <div class="skill-card">

            <div class="skill-icon">🐍</div>

            <h3>Python</h3>

            <p>
                AI applications, automation
                and application development.
            </p>

        </div>


        <div class="skill-card">

            <div class="skill-icon">⚛️</div>

            <h3>React</h3>

            <p>
                Component-based modern
                frontend development.
            </p>

        </div>


        <div class="skill-card">

            <div class="skill-icon">🗄️</div>

            <h3>SQL</h3>

            <p>
                Database management,
                queries and data handling.
            </p>

        </div>


        <div class="skill-card">

            <div class="skill-icon">🤖</div>

            <h3>Prompt Engineering</h3>

            <p>
                Designing effective prompts
                for AI-powered workflows.
            </p>

        </div>


        <div class="skill-card">

            <div class="skill-icon">📈</div>

            <h3>Digital Marketing</h3>

            <p>
                E-commerce operations,
                social media and online marketing.
            </p>

        </div>


    </div>

</section>
""", unsafe_allow_html=True)


# ============================================================
# PROJECTS
# ============================================================

st.markdown("""
<section class="section" id="projects">

    <div class="section-title">

        <h2>
            Featured
            <span class="gradient">Projects</span>
        </h2>

        <p>
            AI-powered applications I've built
        </p>

    </div>


    <div class="projects-grid">


        <!-- PROJECT 1 -->

        <div class="project-card">

            <div class="project-number">
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
                that summarizes papers and helps
                identify and improve potentially
                plagiarized content.

            </p>

            <div class="feature-title">
                CORE FEATURES
            </div>

            <ul class="features">

                <li>PDF/DOCX paper input</li>

                <li>Automatic summary</li>

                <li>Plagiarism similarity analysis</li>

                <li>Highlighted matched content</li>

                <li>Rephrasing suggestions</li>

                <li>Citation checking</li>

            </ul>

            <a
                href="https://ai-driven-research-paper-summarizer-plagiarism-corrector-9pdyf.streamlit.app/"
                target="_blank"
                class="project-link">

                Launch Project ↗

            </a>

        </div>


        <!-- PROJECT 2 -->

        <div class="project-card">

            <div class="project-number">
                PROJECT 02
            </div>

            <div class="project-icon">
                🧠
            </div>

            <h3>
                AI Mentor for Learning
            </h3>

            <p>

                A personalized learning assistant
                designed to adapt learning content,
                study plans and difficulty according
                to the learner.

            </p>

            <div class="feature-title">
                CORE FEATURES
            </div>

            <ul class="features">

                <li>User learning profile</li>

                <li>Personalized study roadmap</li>

                <li>AI Q&A assistant</li>

                <li>Progress tracking</li>

                <li>Quiz-based learning</li>

                <li>Adaptive difficulty</li>

            </ul>

            <a
                href="https://ai-mentor-for-learning-personalized-learning-assistant-odcr4p9.streamlit.app/"
                target="_blank"
                class="project-link">

                Launch Project ↗

            </a>

        </div>


        <!-- PROJECT 3 -->

        <div class="project-card">

            <div class="project-number">
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
                and suggests cleaner solutions.

            </p>

            <div class="feature-title">
                CORE FEATURES
            </div>

            <ul class="features">

                <li>Code paste/upload</li>

                <li>Bug detection</li>

                <li>Line-by-line explanations</li>

                <li>Code quality suggestions</li>

                <li>Before/after comparison</li>

                <li>Multiple languages</li>

            </ul>

            <a
                href="https://ai-powered-code-reviewer-bug-explainer-uus4oprxmhrasquzwbqwzb.streamlit.app/"
                target="_blank"
                class="project-link">

                Launch Project ↗

            </a>

        </div>


    </div>

</section>
""", unsafe_allow_html=True)


# ============================================================
# EDUCATION
# ============================================================

st.markdown("""
<section class="section" id="education">

    <div class="section-title">

        <h2>

            Education &

            <span class="gradient">
                Certifications
            </span>

        </h2>

        <p>
            Academic and professional journey
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
                    University of Education Lahore
                    — Multan Campus
                </p>

            </div>

        </div>


        <div class="timeline-item">

            <div class="timeline-dot"></div>

            <div class="timeline-card">

                <h3>
                    F.Sc Pre-Engineering
                </h3>

                <div class="timeline-date">
                    2021 – 2023
                </div>

                <p>
                    Govt. Graduate College of
                    Science, Multan
                </p>

            </div>

        </div>


        <div class="timeline-item">

            <div class="timeline-dot"></div>

            <div class="timeline-card">

                <h3>
                    E-Commerce Certificate
                </h3>

                <div class="timeline-date">
                    2024
                </div>

                <p>
                    ACE College / NAVTTC
                </p>

            </div>

        </div>


        <div class="timeline-item">

            <div class="timeline-dot"></div>

            <div class="timeline-card">

                <h3>
                    Youth Internship Certificate
                </h3>

                <div class="timeline-date">
                    2025
                </div>

                <p>
                    Friends of Police
                </p>

            </div>

        </div>


    </div>

</section>
""", unsafe_allow_html=True)


# ============================================================
# EXPERIENCE
# ============================================================

st.markdown("""
<section class="section">

    <div class="section-title">

        <h2>

            Work

            <span class="gradient">
                Experience
            </span>

        </h2>

        <p>
            Professional and practical experience
        </p>

    </div>


    <div class="experience-grid">


        <div class="experience-card">

            <h3>
                Store Backup Associate
            </h3>

            <div class="company">
                Sapphire • Jun 2025 – Jul 2025
            </div>

            <p>
                Fashion retail and store
                support experience.
            </p>

        </div>


        <div class="experience-card">

            <h3>
                Back Store Associate
            </h3>

            <div class="company">
                Outfitters • Jul 2025 – Aug 2025
            </div>

            <p>
                Back-store operations and
                inventory-related responsibilities.
            </p>

        </div>


        <div class="experience-card">

            <h3>
                Front of House Staff
            </h3>

            <div class="company">
                Al-Kaif Restaurant
            </div>

            <p>
                Customer-facing hospitality
                experience.
            </p>

        </div>


        <div class="experience-card">

            <h3>
                Self-Employed Online Marketer
            </h3>

            <div class="company">
                Freelance / E-Commerce • Ongoing
            </div>

            <p>
                Online marketing, e-commerce
                operations and digital activities.
            </p>

        </div>


    </div>

</section>
""", unsafe_allow_html=True)


# ============================================================
# CONTACT
# ============================================================

st.markdown("""
<section class="section" id="contact">

    <div class="contact-card">

        <h2>

            Let's Build Something

            <span class="gradient">
                Great
            </span>

        </h2>

        <p>

            Have a project, internship opportunity
            or collaboration idea?
            Feel free to contact me.

        </p>


        <div class="contact-details">

            <div class="contact-item">

                📧

                <span>Email</span>

                <br>

                abdullahmehmood2n4l@gmail.com

            </div>


            <div class="contact-item">

                📱

                <span>Phone</span>

                <br>

                03267636648

            </div>


            <div class="contact-item">

                📍

                <span>Location</span>

                <br>

                Multan Cantt

            </div>

        </div>


        <div class="button-row"
             style="justify-content:center;">

            <a
                href="mailto:abdullahmehmood2n4l@gmail.com"
                class="btn primary-btn">

                Send Me an Email ✉

            </a>


            <a
                href="#projects"
                class="btn secondary-btn">

                View Projects →

            </a>

        </div>

    </div>

</section>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <p>

        Designed & Built by

        <span>
            Abdullah Mehmood
        </span>

    </p>

    <p style="margin-top:8px;">

        HTML • CSS • JavaScript • Python • AI

    </p>

    <p style="margin-top:12px;">

        © 2026 Abdullah Mehmood.
        All Rights Reserved.

    </p>

</div>
""", unsafe_allow_html=True)
