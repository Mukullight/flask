
from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        :root {
            --background: #ffffff;
            --text: #000000;
            --sidebar-bg: #ffffff;
            --sidebar-text: #000000;
            --accent: #000000;
            --sidebar-width: 250px;
            --sidebar-collapsed-width: 60px;
        }

        [data-theme="dark"] {
            --background: #000000;
            --text: #ffffff;
            --sidebar-bg: #000000;
            --sidebar-text: #ffffff;
            --accent: #ffffff;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: var(--background);
            color: var(--text);
            transition: all 0.3s ease;
            display: flex;
        }

        .hamburger {
            display: none; 
            cursor: pointer;
            padding: 1rem;
            z-index: 1001;
            position: fixed;
            top: 1rem;
            left: 1rem;
        }

        .hamburger span {
            display: block;
            width: 25px;
            height: 3px;
            margin-bottom: 5px;
            background: var(--sidebar-text);
            transition: all 0.3s ease;
        }

        .hamburger span:last-child {
            margin-bottom: 0;
        }

        .sidebar {
            width: var(--sidebar-width);
            height: 100vh;
            background-color: var(--sidebar-bg);
            position: fixed;
            left: 0;
            top: 0;
            padding: 2rem 0;
            padding-top:3em;
            display: flex;
            flex-direction: column;
            transition: all 0.3s ease;
            z-index: 1000;
        }

        .nav-brand {
            color: var(--sidebar-text);
            font-size: 1.5rem;
            font-weight: bold;
            text-decoration: none;
            padding: 0 2rem 2rem;
            border-bottom: 1px solid var(--sidebar-text);
        }

        .nav-links {
    display: flex;
    flex-direction: column;
    padding: 2rem 0;
}

.nav-link {
    color: var(--sidebar-text);
    text-decoration: none;
    padding: 1rem 2rem;
    transition: all 0.3s ease;
    position: relative;
    opacity: 0.7;
}

.nav-link:hover,
.nav-link.active {
    opacity: 1;
    background-color: var(--accent);
    color: var(--contrast-text, #ffffff);  /* Default to white if var not set */
}

.nav-link.active {
    border-left: 4px solid var(--sidebar-text);
}

/* Theme-specific contrast text colors */
[data-theme="dark"] .nav-link:where(:hover, .active) {
    --contrast-text: #000000;
}

[data-theme="light"] .nav-link:where(:hover, .active) {
    --contrast-text: #ffffff;
}
      .theme-switch-wrapper {
    position: fixed;
    top: 1rem;
    right: 1rem;
    z-index: 1001; /* Ensure it's above other elements */
    padding: 0rem;
    background: var(--background);
    display: flex;
    align-items: center;
}
        .theme-switch {
            display: inline-block;
            height: 24px;
            position:relative;
            width: 48px;
            border: 1px solid var(--sidebar-text);
            border-color: white;
            border-radius: 34px;
            margin: 0 0.5rem;
        }

        .theme-switch input {
            display: none;
        }

        .slider {
            background-color: var(--background);
            bottom: 0;
            cursor: pointer;
            left: 0;
            position: absolute;
            right: 0;
            top: 0;
            transition: .4s;
            border-radius: 34px;
        }

        .slider:before {
            background-color: var(--text);
            bottom: 4px;
            content: "";
            height: 16px;
            left: 4px;
            position: absolute;
            transition: .4s;
            width: 16px;
            border-radius: 50%;
        }

        input:checked + .slider {
            background-color: var(--background);
        }

        input:checked + .slider:before {
            transform: translateX(24px);
        }

        .main-content {
            margin-left: var(--sidebar-width);
            width: calc(100% - var(--sidebar-width)+10%);
            padding-top: 0em;
            max-width: 1000px;
            margin: 0 auto;
            margin-left: calc(var(--sidebar-width) + 2rem);
        }

        .section {
            padding-left: 2em;
            padding-top: 0;
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            scroll-margin-top: 2rem;
        }

        h1, h2 {
            color: var(--text);
        }

        h1 {
            margin-bottom: 1rem;
            font-size: 2.5rem;
            padding-left: 0.5em;
        }

        h2 {
            margin-bottom: 1rem;
            font-size: 2rem;
            padding-top: 0em;
            padding: 0em;
        }

        .metadata {
            color: var(--text);
            font-size: 0.9rem;
            margin-bottom: 2rem;
        }

        p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
            padding: 0em;
        }

        .footer {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid var(--text);
            font-size: 0.9rem;
            color: var(--text);
            text-align: center;
        }
.main-content > .section {
    margin-top: 0;
    padding-top: 0;
    margin-bottom: 0;
    padding-bottom: 0;
}
#Introduction{
padding: 0em;
padding-left: 2.5em;
}
#Keydifferences{
padding: 0em;
padding-left: 2.5em;
}
#thesolution{
padding: 0em;
padding-left: 2.5em;
}
#Action{
padding: 0em;
padding-left: 2.5em;
}



@media (max-width: 768px) {
    .hamburger {
        display: block;
    }

    .sidebar {
        /* Remove transform to show sidebar by default */
        /* transform: translateX(-100%); */
        position: fixed; /* Ensure sidebar stays in place */
        left: -250px; /* Position sidebar off-screen initially */
        transition: left 0.3s ease;
    }

    .sidebar.active {
        left: 0; /* Slide sidebar into view when active */
        width: var(--sidebar-width);
    }

    .main-content {
        margin-left: 0; /* Start with no left margin */
        padding-left: 2rem; /* Add padding for content readability */
        padding-right: 0em;
    }


    
}
        }
    </style>
</head>
<body>
    <div class="hamburger" id="hamburger">
        <span></span>
        <span></span>
        <span></span>
    </div>
    <div class="theme-switch-wrapper">
            <span style="color: #000000">⚫</span>
            <label class="theme-switch">
                <input type="checkbox" id="theme-toggle">
                <span class="slider"></span>
            </label>
            <span style="color: #ffffff">⚪</span>
        </div>
    <aside class="sidebar">
        <a href="#top" class="nav-brand">Agents: The age of action </a>
        <nav class="nav-links">
            <a href="#Introduction" class="nav-link">Introduction</a>
            <a href="#Keydifferences" class="nav-link">What is so Special?</a>
            <a href="#thesolution" class="nav-link">An Important Answer</a>
            <a href="#Action" class="nav-link">Krea - To do</a>
        </nav>
            <div class="theme-switch-wrapper">
        <span style="color: #000000">⚫</span>
        <label class="theme-switch">
            <input type="checkbox" id="theme-toggle">
            <span class="slider"></span>
        </label>
        <span style="color: #ffffff">⚪</span>
    </div>

    </aside>

    <main class="main-content">
        <div id="Introduction" class="section">
            <h1>{{ title }}</h1>
            <div class="metadata">
                <span>Published on: {{ date }}</span>
                <span> | </span>
                <span>By: {{ author }}</span>
            </div>
            <p>I have always believed in the power of introspection, funny how in most social situations or in conversations. I have always been slow to respond, although I do agree that there is charm in quick-witted responses. I have always stuck with the former. I always think twice or even thrice before I say something or judge someone, as I was told growing up that for every finger you point at someone or something, there are three directly pointing right back at you. I often tend not to change or re-evaluate my opinion or respond unless I have been presented with concrete evidence; it sometimes worked in my favor, other times it did not, but to this day, I never regretted doing something after careful introspection. So what does introspection have to do with agents, you might ask? It was often the case that most AI projects that have been undertaken are not limited by the underlying architecture of the model or inefficiencies in the project design; it has always been the unavailability of large-scale compute resources. Hence, most large-scale successful projects have always been locked inside the research labs of technology giants, often releasing benchmark after another with better and better models every few months. Quite often, these monolithic models are quite performant in most tasks, ranging from code generation to multimodal understanding to solving complex problems at scale. I have a strong belief that these models, over time, with better training data, evaluation frameworks, and better compute, will inadvertently get better over time. As for the rest of the industry, most emerging startups, particularly in the AI space, are concerned with adapting these large-scale monolithic models to a specific use case and trying to be the best at their own use case. Most often, these efforts become obsolete as newer versions of the capable model roll out, but there is still hope and opportunity to capitalize on these niche markets. Most often, these large-scale model providers cannot provide or do not wish to take on the challenge of serving or deploying the models in end-user use cases, as there are too many and they require expertise from professionals in the specific fields. So you might ask the question: Where do agents come in? Is it just another buzzword that will go away after a few years? Will there be another AI winter? In my personal experience with few-shot models—where an AI is asked to generate a response in one go—it's quite common for the model to be rushed into providing an answer which is pretty mediocre and incomplete. Alternatively, when I have assigned several smaller models to solve the subtasks of the problem and merged them into the solution, it showed a slight improvement in the responses they produced, even without the models collaborating. Although these models perform well in certain use cases like aspect extraction and categorization, they fall short when it comes to more complex tasks requiring multi-step reasoning. Just as humans don't often need introspection for simple day-to-day tasks, when faced with solving a complex math problem, such introspection becomes necessary. Reevaluating the response and explaining the reasoning to reach a conclusion can be quite important in solving any form of complex problem; the same goes for these AI models. It is often the case that the limited context window that these models have restricts them to generate a response at its maximum potential. So let's take a step back and analyze how these so-called agents work.</p></div>
<div id="Keydifferences" class="section">
            <h2>What is so Special?</h2>
            <p>So if a non-agentic model is asked to solve a particular task, it analyzes the whole task at one go and tries to come up with a response at the best of its capability. But agents, on the other hand, act as independent actors that break down the task into multiple subtasks, with different agents working on different aspects with the collective goal of achieving the greater good. They often interact, collaborate, and evaluate the responses they generate. Some of the design patterns these agentic workflows utilize include reflection with feedback, using tools, planning, and distributing tasks among them. These models quite often have a huge degree of autonomy in the way they operate; they have a good ability to adapt to situations and initiate independent actions. Instead of being reactive, they are planned strategists.

As Microsoft CEO Satya Nadella puts it, the traditional CRUD (Create, Read, Update, Delete) databases with UI on top, aka SaaS (Software as a Service), are essentially going to be a thing of the past. The underlying traditional CRUD databases are going to be replaced by agents interacting to produce a result. The new year, 2025, is going to be the Year of Swarm Intelligence, with networks of agents working together. This shift towards agentic systems signifies a move from static data processing to dynamic, collaborative problem-solving, potentially expanding the capabilities of AI beyond what traditional models can offer in terms of flexibility and efficiency. 
</p></div>
         <div id="thesolution" class="section">
            <h2>An Important Solution</h2>
            <p>
So one might ask the question: are agents going to be the end-all-be-all solution to drastically increasing these models' performance? There is always a slight pessimism even in the AI community regarding how capable these models can get. The argument goes like this: since most of the data generated on the internet is pretty mediocre, as is most code written or content in general, before these models become truly capable, we might run out of good data to train these AI models. Or worse yet, synthetically generated data might not be good enough or could degrade the performance of the model due to data drift. But time and time again, this argument has been proven wrong by newer, more capable models, and positively reinforced by the argument that much of these models haven't even seen other modalities. 

"Just like the circle from Flatland, who could only grasp the two dimensions it lives in, most of these AI models have only been trained on a large corpus of text. The fact that learning almost all skills requires practical training and hands-on experience tells you that a huge chunk of high-level human knowledge cannot be acquired by merely reading text. And then, there is the mass of non-verbal knowledge that babies and animals acquire..." This perspective from Yann LeCun underscores the limitation of current AI models, suggesting that to achieve a more human-like understanding, they should be exposed to and trained across multiple modalities beyond just text. There is quite a strong argument that this agentic approach should be utilized in training the models across multiple modalities.
The idea is that by using agents to handle different aspects of training and data processing, we can leverage the strengths of multimodal learning. Agents could, for instance, focus on different sensory inputs like visual, auditory, or even haptic data, mirroring the way humans learn from their environment through various senses. This could potentially lead to AI systems that are not only more versatile but also more adept at understanding and interacting with the real world, much like how human cognition benefits from the integration of diverse sensory information.</p></div>
<div id="Action" class="section">
            <h2>Action</h2>
            <p>Human computer interaction has fundamentally changed over the years from batch processing to time sharing to modern day guis with the advent of mobile, pc technology and cloud computing these small scale devices have become more intertwined into our life. With agents the way we use this devices is going to change drastically instead of moving the mouse, editing the code and typing all we have to do to accomplish a task to give it a command and wait and watch from moving cursor to opening and writing files everything is going to be automated this is likely in very near future possibly in coming 3 to 4 years is going to be a reality. For those who are from the computer science background know how hard it is to programme a cursor to move on the screen yes! Yeah we all made the moving turtle animation. Now with AI agents the entire lines of code could be automated. All we have to do is give it a task and watch it finish it. This might seem not too impressive but is quite huge in its impact on jobs like basic HR work, editing a video to using tools, making powerpoints, working with spreadsheets; to designing animations these entire tasks could be accomplished with just a command. If the generated output is not impressive we can just prompt it to integrate more corrections. All that a human employee has to do is high level functional specification of a task to be achieved. This begs the question where does Vast majority of humans fit in ? Why should these companies hire more humans? How would the wealth transfer occur? So in the far future will the commerce stop? Unlike human employees, AI agents do not require breaks, vacations, or benefits. They are the epitome of the ideal worker - one who never errs, who never gets sick, never cheats.  Their only necessity for these agents is electricity to operate, making them incredibly efficient. This vision of a workforce where mistakes are nonexistent and downtime is eliminated showcases how AI agents can revolutionize the concept of labor, providing a scalable, error-free, and always-available team of professionals Night and Day available upon one command. So what happens to the rest of us who are not the brilliant ones who could not have the chance to join in or capitalize on this opportunity. So what are we to do this </p>
            <div class="footer">
                <p>© {{ current_year }} {{ author }}. All rights reserved.</p>
            </div>
        </div>
    </main>

    <script>
        const toggleSwitch = document.getElementById('theme-toggle');
        const sidebar = document.querySelector('.sidebar');
        const hamburger = document.getElementById('hamburger');
        const currentTheme = localStorage.getItem('theme');

        if (currentTheme) {
            document.documentElement.setAttribute('data-theme', currentTheme);
            if (currentTheme === 'dark') {
                toggleSwitch.checked = true;
            }
        }

        function switchTheme(e) {
            if (e.target.checked) {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
            } else {
                document.documentElement.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
            }
        }
        function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }
}

        toggleSwitch.addEventListener('change', switchTheme);

        hamburger.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });

        const sections = document.querySelectorAll('.section');
        const navLinks = document.querySelectorAll('.nav-link');

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.5
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === '#' + id) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }, observerOptions);

        sections.forEach(section => {
            observer.observe(section);
        });

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                document.querySelector(targetId).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>
'''

@app.route('/')
def blog_post():
    title = "Agents: The age of action "
    author = "Mukul Namagiri"
    date = "January 17, 2025"
    
    return render_template_string(
        TEMPLATE,
        title=title,
        author=author,
        date=date,
        current_year=datetime.now().year
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
