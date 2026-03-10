import streamlit as st

def apply_custom_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* Dark gradient background */
        .stApp {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
        }

        /* Weather info card */
        .weather-card {
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            margin-bottom: 1.5rem;
            color: #fff;
        }

        /* Big temperature number */
        .temp-display {
            font-size: 5rem;
            font-weight: 700;
            line-height: 1;
            color: #ffffff;
            text-shadow: 0 0 30px rgba(100,200,255,0.6);
        }

        .metric-label {
            font-size: 0.75rem;
            color: rgba(255,255,255,0.5);
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }
        .metric-value { font-size: 1.4rem; font-weight: 600; color: #ffffff; }

        /* Alert banners */
        .alert-danger  { background: rgba(255,60,60,0.2);  border-left: 4px solid #ff3c3c; border-radius:12px; padding:1rem; color:#fff; }
        .alert-warning { background: rgba(255,165,0,0.2);  border-left: 4px solid #ffa500; border-radius:12px; padding:1rem; color:#fff; }
        .alert-info    { background: rgba(60,160,255,0.2); border-left: 4px solid #3ca0ff; border-radius:12px; padding:1rem; color:#fff; }
        .alert-success { background: rgba(50,205,100,0.2); border-left: 4px solid #32cd64; border-radius:12px; padding:1rem; color:#fff; }

        /* Gradient title */
        .hero-title {
            font-size: 2.4rem;
            font-weight: 700;
            background: linear-gradient(90deg, #a18dff, #64c8ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }

        hr { border-color: rgba(255,255,255,0.1); }
        h3 { color: rgba(255,255,255,0.9) !important; }

        /* ── BUTTONS ─────────────────────────── */
        div.stButton > button,
        div.stButton > button:focus,
        div.stButton > button:active {
            background: linear-gradient(90deg, #6c63ff, #3c9eff) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.6rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            width: 100% !important;
            box-shadow: 0 4px 20px rgba(108,99,255,0.35) !important;
            transition: opacity 0.2s, box-shadow 0.2s !important;
        }
        div.stButton > button:hover {
            opacity: 0.88 !important;
            box-shadow: 0 6px 28px rgba(60,158,255,0.5) !important;
        }

        /* ── LABELS ──────────────────────────── */
        .stTextInput label, .stNumberInput label,
        div[data-testid="stTextInput"] label,
        div[data-testid="stNumberInput"] label {
            color: rgba(255,255,255,0.7) !important;
        }
        .stSlider label, div[data-testid="stSlider"] label {
            color: rgba(255,255,255,0.7) !important;
        }

        /* ── INPUTS: broad universal override ── */
        /* Target every <input> and its wrappers */
        input[type="text"], input[type="number"], input {
            background: rgba(20, 17, 50, 0.9) !important;
            background-color: rgba(20, 17, 50, 0.9) !important;
            color: #ffffff !important;
            border: 1.5px solid rgba(160,140,255,0.5) !important;
            border-radius: 10px !important;
            caret-color: #a18dff !important;
            outline: none !important;
            transition: border-color 0.2s, box-shadow 0.2s !important;
        }
        input:focus {
            border-color: rgba(100,200,255,0.8) !important;
            box-shadow: 0 0 0 3px rgba(108,99,255,0.3) !important;
        }
        input::placeholder { color: rgba(200,190,255,0.4) !important; }

        /* Nuke all white backgrounds inside input containers */
        div[data-testid="stTextInput"] *,
        div[data-testid="stNumberInput"] * {
            background: transparent !important;
            background-color: transparent !important;
        }
        /* Re-apply dark to the actual input after the nuke */
        div[data-testid="stTextInput"] input,
        div[data-testid="stNumberInput"] input {
            background: rgba(20, 17, 50, 0.9) !important;
            background-color: rgba(20, 17, 50, 0.9) !important;
            color: #ffffff !important;
            border: 1.5px solid rgba(160,140,255,0.5) !important;
            border-radius: 10px !important;
        }

        /* Number stepper +/– buttons */
        div[data-testid="stNumberInput"] button {
            background: rgba(108,99,255,0.3) !important;
            background-color: rgba(108,99,255,0.3) !important;
            border: 1px solid rgba(160,140,255,0.35) !important;
            color: #fff !important;
            border-radius: 8px !important;
        }
        div[data-testid="stNumberInput"] button:hover {
            background: rgba(108,99,255,0.55) !important;
            background-color: rgba(108,99,255,0.55) !important;
        }
        div[data-testid="stNumberInput"] button svg {
            fill: #fff !important;
            stroke: #fff !important;
        }

        /* Spinner */
        .stSpinner > div { border-top-color: #a18dff !important; }
        </style>

        <script>
        /* Force dark styles on every Streamlit input via MutationObserver.
           This is needed because Streamlit's styled-components use inline styles
           that override even !important CSS rules. */
        (function() {
          var DARK_BG   = 'rgba(20, 17, 50, 0.9)';
          var BORDER    = '1.5px solid rgba(160,140,255,0.5)';
          var BORDER_F  = '1.5px solid rgba(100,200,255,0.8)';
          var SHADOW_F  = '0 0 0 3px rgba(108,99,255,0.3)';

          function styleInputs() {
            document.querySelectorAll('input').forEach(function(el) {
              el.style.setProperty('background',       DARK_BG, 'important');
              el.style.setProperty('background-color', DARK_BG, 'important');
              el.style.setProperty('color',            '#ffffff', 'important');
              el.style.setProperty('border',           BORDER,   'important');
              el.style.setProperty('border-radius',    '10px',   'important');
              el.style.setProperty('caret-color',      '#a18dff','important');
              el.style.setProperty('outline',          'none',   'important');

              // Focus / blur events
              if (!el._darkThemed) {
                el._darkThemed = true;
                el.addEventListener('focus', function() {
                  el.style.setProperty('border',     BORDER_F, 'important');
                  el.style.setProperty('box-shadow', SHADOW_F, 'important');
                });
                el.addEventListener('blur', function() {
                  el.style.setProperty('border',     BORDER,  'important');
                  el.style.setProperty('box-shadow', 'none',  'important');
                });
              }
            });

            // Nuke any white wrapper backgrounds
            document.querySelectorAll(
              '[data-testid="stTextInput"] > div, ' +
              '[data-testid="stNumberInput"] > div, ' +
              '[data-testid="stTextInput"] > div > div, ' +
              '[data-testid="stNumberInput"] > div > div'
            ).forEach(function(el) {
              el.style.setProperty('background',       'transparent', 'important');
              el.style.setProperty('background-color', 'transparent', 'important');
            });
          }

          // Run immediately & on every DOM mutation
          var obs = new MutationObserver(styleInputs);
          function init() {
            styleInputs();
            obs.observe(document.body, { childList: true, subtree: true });
          }

          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
          } else {
            init();
            setTimeout(styleInputs, 300);
            setTimeout(styleInputs, 800);
            setTimeout(styleInputs, 1800);
          }
        })();
        </script>
        """,
        unsafe_allow_html=True,
    )

def render_header():
    st.markdown('<div class="hero-title">🌤️ Weather Alert System</div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:rgba(255,255,255,0.55);margin-bottom:1.5rem;">'
        "Live weather data with intelligent alerts</p>",
        unsafe_allow_html=True,
    )

def render_footer():
    st.markdown(
        """
        <hr style="margin-top:3rem;">
        <p style="color:rgba(255,255,255,0.25);text-align:center;font-size:0.75rem;">
          Data sourced from <a href="https://wttr.in" style="color:#6c9eff;">wttr.in</a> ·
          Weather Alert System · AI Assignment 01
        </p>
        """,
        unsafe_allow_html=True,
    )

def render_weather_card(city_name, temp, desc, emoji, feels, humid, wind):
    st.markdown(
        f"""
        <div class="weather-card">
          <div style="display:flex; justify-content:space-between; align-items:flex-start;">
            <div>
              <div style="color:rgba(255,255,255,0.6);font-size:0.9rem;">📍 {city_name}</div>
              <div class="temp-display">{temp}°<span style="font-size:2rem;">C</span></div>
              <div style="color:rgba(255,255,255,0.6);margin-top:0.3rem;">{desc}</div>
            </div>
            <div style="font-size:4rem;">{emoji}</div>
          </div>
          <hr style="margin:1rem 0;">
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;text-align:center;">
            <div>
              <div class="metric-label">Feels Like</div>
              <div class="metric-value">{feels}°C</div>
            </div>
            <div>
              <div class="metric-label">Humidity</div>
              <div class="metric-value">{humid}%</div>
            </div>
            <div>
              <div class="metric-label">Wind</div>
              <div class="metric-value">{wind} km/h</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_alert_message(level, emoji, title, message):
    st.markdown(
        f"""
        <div class="alert-{level}">
          <strong>{emoji} {title}</strong><br>
          {message}
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_manual_gauge(temp, humid, wind, gauge_color, pct):
    st.markdown(
        f"""
        <div class="weather-card">
          <div style="text-align:center;">
            <div class="temp-display" style="color:{gauge_color};">{temp}°C</div>
            <div style="color:rgba(255,255,255,0.5);margin:0.5rem 0;">
              Humidity: {humid}% &nbsp;|&nbsp; Wind: {wind} km/h
            </div>
          </div>
          <div style="background:rgba(255,255,255,0.1);border-radius:9999px;height:12px;margin:1rem 0;">
            <div style="background:linear-gradient(90deg,#64c8ff,{gauge_color});
                         width:{pct}%;height:12px;border-radius:9999px;
                         transition:width 0.5s;"></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
