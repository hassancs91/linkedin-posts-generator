import streamlit as st
from SimplerLLM.language.llm import LLM, LLMProvider
from templates import post_reviewer_prompt, templates_1, templates_2, templates_3, templates_4, prompt_short_to_post
import youtube_helpers

# Create instances
openai_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-4o")
anthropic_instance = LLM.create(provider=LLMProvider.ANTHROPIC, model_name="claude-3-5-sonnet-20240620")

# Streamlit Layout
st.title("YouTube Short to LinkedIn Post Converter")

# Video ID Input
video_id = st.text_input("Enter YouTube Video ID:", "CYTwGx43SzY")

if st.button("Generate Posts"):
    with st.spinner('Fetching YouTube content...'):
        content = youtube_helpers.get_youtube_transcript_with_searchapi(video_id)
            # Prepare prompts
        prompt_template_1 = prompt_short_to_post.format(video=content, post_templates=templates_1)
        prompt_template_2 = prompt_short_to_post.format(video=content, post_templates=templates_2)
        prompt_template_3 = prompt_short_to_post.format(video=content, post_templates=templates_3)
        prompt_template_4 = prompt_short_to_post.format(video=content, post_templates=templates_4)
        st.success('Content fetched successfully!')
    
    # Prepare prompts
    
    progress = st.progress(0)
    progress_value = 0  # Initialize the progress counter
    progress_text = st.empty()
    
    def generate_and_display(prompt_template, instance, description):
        progress_text.text(f'Generating {description}...')
        response = instance.generate_response(prompt=prompt_template)
        return response
    
    # Generate responses from OpenAI
    openai_responses = []
    for idx, template in enumerate([prompt_template_1, prompt_template_2, prompt_template_3, prompt_template_4]):
        response = generate_and_display(template, openai_instance, f"OpenAI Response {idx + 1}")
        checked_response = openai_instance.generate_response(prompt=post_reviewer_prompt.format(post=response))
        openai_responses.append(checked_response)
        progress_value += 0.125  # Increment progress value correctly as a fraction
        progress.progress(progress_value)
    
    # Generate responses from Anthropic
    anthropic_responses = []
    for idx, template in enumerate([prompt_template_1, prompt_template_2, prompt_template_3, prompt_template_4]):
        response = generate_and_display(template, anthropic_instance, f"Anthropic Response {idx + 1}")
        checked_response = anthropic_instance.generate_response(prompt=post_reviewer_prompt.format(post=response))
        anthropic_responses.append(checked_response)
        progress_value += 0.125  # Increment progress value correctly as a fraction
        progress.progress(progress_value)
    
    progress_text.text('All responses generated!')
    st.success('All responses generated successfully!')

    # Display results in a structured layout with boxes
    cols = st.columns(2)
    response_labels = ["Response 1", "Response 2", "Response 3", "Response 4"]
    for i, col in enumerate(cols):
        with col:
            st.subheader("OpenAI Responses" if i == 0 else "Anthropic Responses")
            for idx, response in enumerate(openai_responses if i == 0 else anthropic_responses):
                st.markdown(f"**{response_labels[idx]}:**")
                st.info(response)


