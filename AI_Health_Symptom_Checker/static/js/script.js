// Dark mode toggle
const toggle = document.getElementById("themeToggle");
const html = document.documentElement;

const saved = localStorage.getItem("theme") || "light";
html.setAttribute("data-theme", saved);
if (toggle) toggle.textContent = saved === "dark" ? "☀" : "🌙";

if (toggle) {
    toggle.addEventListener("click", () => {
        const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
        html.setAttribute("data-theme", next);
        localStorage.setItem("theme", next);
        toggle.textContent = next === "dark" ? "☀" : "🌙";
    });
}

// Voice input using Web Speech API
const voiceBtn = document.getElementById("voiceBtn");
const voiceStatus = document.getElementById("voiceStatus");

if (voiceBtn) {
    voiceBtn.addEventListener("click", () => {
        const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SR) {
            voiceStatus.textContent = "Voice input not supported in this browser.";
            return;
        }
        const recog = new SR();
        recog.lang = "en-US";
        recog.start();
        voiceStatus.textContent = "🎙 Listening...";

        recog.onresult = (e) => {
            const text = e.results[0][0].transcript.toLowerCase();
            voiceStatus.textContent = "Heard: " + text;
            document.querySelectorAll(".symptom-check").forEach(cb => {
                const label = cb.value.toLowerCase().replace(/_/g, " ");
                if (text.includes(label)) cb.checked = true;
            });
        };
        recog.onerror = () => voiceStatus.textContent = "Voice input error. Try again.";
    });
}
