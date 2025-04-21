import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Life Domain Reflection", layout="wide")
st.title(" Life Domain Reflection")

st.markdown("Answer each question using the slider scale below. Your responses will generate a pie chart representing your current focus across five key life domains.")

# Custom CSS for pastel slider theme
st.markdown("""
<style>
.question-card {
    background-color: #f9f9f9;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
[data-testid="stSlider"] .st-c1 {
    background: linear-gradient(to right, #fde2e4, #e0bbf4, #caffbf);
    border-radius: 10px;
    height: 6px;
}
[data-testid="stSlider"] .st-c3 {
    background-color: #a0c4ff;
    border: 2px solid white;
}
[data-testid="stSlider"] .st-c4 {
    color: #555;
    font-size: 0.85rem;
    margin-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# Updated domain questions
domain_questions = {
    "Family": [
        "I feel deeply connected and supported by my family members in my daily life.",
        "I feel more at peace when I’ve checked in with my family recently.",
        "My family provides a strong support system during difficult times."
    ],
    "Health": [
        "Mental health is just as important as physical health.",
        "I function best when I’ve had enough rest, movement, and nourishment.",
        "I care about what I put into my body.",
        "I prioritize physical activity in my daily life."
    ],
    "Community": [
        "I enjoy engaging with my community.",
        "I feel supported by the people in my life.",
        "Pouring into others gives me a sense of purpose.",
        "I feel a genuine sense of belonging in the community I live in."
    ],
    "Spirituality": [
        "Believing in a higher power gives life more meaning.",
        "I often feel a sense of connection to something greater than myself.",
        "I seek purpose or deeper meaning in the experiences I go through.",
        "I feel deeply connected to my spiritual journey and/or practices."
    ],
    "Work": [
        "My sense of identity is strongly tied to my work or what I created.",
        "I actively seek opportunities to learn and develop new skills in my career.",
        "I balance my workload in a way that helps to prevent me from burning out."
    ]
}

# Collect answers and calculate average per domain
domain_scores = {}

for domain, questions in domain_questions.items():
    st.markdown(f"<div class='question-card'><h4>{domain}</h4>", unsafe_allow_html=True)
    scores = []
    for i, q in enumerate(questions):
        st.markdown(f"**{q}**")
        score = st.slider(
            label="",
            min_value=0,
            max_value=10,
            value=5,
            step=1,
            key=f"{domain}_{i}"
        )
        scores.append(score)
    domain_scores[domain] = sum(scores) / len(scores)
    st.markdown("</div>", unsafe_allow_html=True)

# Prepare data for pie chart
domains = list(domain_scores.keys())
values = list(domain_scores.values())
if sum(values) == 0:
    values = [1 for _ in values]  # prevent division by zero

# Pie chart
fig = go.Figure(data=[
    go.Pie(labels=domains, values=values, hole=0.3)
])
fig.update_traces(textinfo='label+percent')
fig.update_layout(margin=dict(t=10, b=10, l=10, r=10))

st.plotly_chart(fig, use_container_width=True)
# Highlight top scoring domain
top_domain = domains[values.index(max(values))]
st.markdown(f"**Highest scoring domain:** {top_domain}")