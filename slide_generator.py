import streamlit as st
import json
import io
from PIL import Image, ImageDraw, ImageFont
import textwrap
from zipfile import ZipFile
import os
import tempfile
from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.language.llm_addons import generate_pydantic_json_model

# Initialize OpenAI client
openai_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-4o")


from typing import List
from pydantic import BaseModel

class Slide(BaseModel):
    title: str  # Slide title under 60 characters
    points: List[str] 

class CreateLinkedInCarousel(BaseModel):
    caption: str  # 2-3 engaging sentences with emojis and hashtags for LinkedIn post
    slides: List[Slide]  # Array of 5-7 slides


# Initialize session state for storing generated and editable content
if 'slides_data' not in st.session_state:
    st.session_state.slides_data = None
if 'slides_images' not in st.session_state:
    st.session_state.slides_images = None
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 1
if 'editing_mode' not in st.session_state:
    st.session_state.editing_mode = False
if 'edited_slides' not in st.session_state:
    st.session_state.edited_slides = None
if 'current_style' not in st.session_state:
    st.session_state.current_style = {
        "background_color": "#FFFFFF",
        "text_color": "#000000",
        "font_style": "Professional",
        "guidelines": "Use professional tone, include statistics when available, make content scannable"
    }

def create_download_zip(slides_images):
    """Create a ZIP file containing all slides"""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save all images to temp directory
        for i, img in enumerate(slides_images, 1):
            img_path = os.path.join(temp_dir, f'slide_{i}.png')
            img.save(img_path, 'PNG')
        
        # Create ZIP file in memory
        zip_buffer = io.BytesIO()
        with ZipFile(zip_buffer, 'w') as zip_file:
            # Add all images to ZIP
            for i in range(1, len(slides_images) + 1):
                img_path = os.path.join(temp_dir, f'slide_{i}.png')
                zip_file.write(img_path, f'slide_{i}.png')
        
        zip_buffer.seek(0)
        return zip_buffer.getvalue()

def update_slide():
    """Update current slide based on slider value"""
    st.session_state.current_slide = st.session_state.slide_navigator

def generate_slides_content(text, style):
    """Generate slides content using GPT-4 with function calling"""
    
    # functions = [
    #     {
    #         "name": "create_linkedin_carousel",
    #         "description": "Generate content for LinkedIn carousel post",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "caption": {
    #                     "type": "string",
    #                     "description": "2-3 engaging sentences with emojis and hashtags for LinkedIn post"
    #                 },
    #                 "slides": {
    #                     "type": "array",
    #                     "description": "Array of 5-7 slides",
    #                     "items": {
    #                         "type": "object",
    #                         "properties": {
    #                             "title": {
    #                                 "type": "string",
    #                                 "description": "Slide title under 60 characters"
    #                             },
    #                             "points": {
    #                                 "type": "array",
    #                                 "description": "2-3 bullet points per slide",
    #                                 "items": {
    #                                     "type": "string",
    #                                     "description": "Bullet point under 100 characters"
    #                                 }
    #                             }
    #                         },
    #                         "required": ["title", "points"]
    #                     }
    #                 }
    #             },
    #             "required": ["caption", "slides"]
    #         }
    #     }
    # ]

    prompt = f"""Transform the following text into an engaging LinkedIn carousel post.
    Make it informative and eye-catching, with relevant statistics when possible.
    Style guidelines: {style}
    
    Text to transform:
    {text}"""

    try:

        response = generate_pydantic_json_model(model_class=CreateLinkedInCarousel,
                                                 prompt=prompt,llm_instance=openai_instance,
                                                 max_tokens=4096)


        # response = client.chat.completions.create(
        #     model="gpt-4-turbo-preview",
        #     messages=[{"role": "user", "content": prompt}],
        #     functions=functions,
        #     function_call={"name": "create_linkedin_carousel"}
        # )
        
        # Extract the function call from the response
        #function_response = response.choices[0].message.function_call
        #if function_response and function_response.name == 'create_linkedin_carousel':
        #    return json.loads(function_response.arguments)
        return response
        st.error("Unexpected response format from GPT-4")
        return create_error_response("Invalid response format")
            
    except Exception as e:
        st.error(f"API call error: {str(e)}")
        return create_error_response("API call failed")
    
def create_error_response(error_message):
    """Create a fallback response for error cases"""
    return {
        "caption": f"Error: {error_message}",
        "slides": [
            {
                "title": "Error Occurred",
                "points": [
                    "Failed to generate slides",
                    "Please try again",
                    f"Error: {error_message}"
                ]
            }
        ]
    }


def create_slide_image(title, points, style):
    """Create an image for a single slide with proper text positioning"""
    width = 1080
    height = 1080
    img = Image.new('RGB', (width, height), style['background_color'])
    draw = ImageDraw.Draw(img)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        body_font = ImageFont.truetype("arial.ttf", 40)
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
    
    # Draw title with proper centering
    title_wrapped = textwrap.fill(title, width=30)
    title_bbox = draw.multiline_textbbox((0, 0), title_wrapped, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    
    title_x = (width - title_width) / 2
    title_y = 100
    
    draw.multiline_text(
        (title_x, title_y), 
        title_wrapped, 
        font=title_font, 
        fill=style['text_color'],
        align='center'
    )
    
    # Draw points with proper formatting
    y_position = 300
    for point in points:
        wrapped_point = textwrap.fill(point, width=40)
        
        # Calculate point text dimensions
        point_bbox = draw.multiline_textbbox((0, 0), wrapped_point, font=body_font)
        point_height = point_bbox[3] - point_bbox[1]
        
        # Draw bullet point
        draw.text((60, y_position), "•", font=body_font, fill=style['text_color'])
        
        # Draw point text
        draw.multiline_text(
            (120, y_position),
            wrapped_point,
            font=body_font,
            fill=style['text_color']
        )
        
        # Update y position based on actual text height
        y_position += point_height + 40  # Add some padding between points
    
    return img



def update_slide_content():
    """Update slides based on edited content"""
    if st.session_state.edited_slides:
        slides_images = []
        for slide in st.session_state.edited_slides:
            slide_img = create_slide_image(
                slide.title,
                slide.points,
                st.session_state.current_style
            )
            slides_images.append(slide_img)
        st.session_state.slides_images = slides_images

def edit_slide_content(index):
    """Edit interface for individual slide content"""
    slide = st.session_state.edited_slides[index]
    
    # Edit title
    new_title = st.text_input(
        "Edit Title",
        value=slide.title,
        key=f"title_{index}"
    )
    
    # Edit points
    new_points = []
    for i, point in enumerate(slide.points):
        new_point = st.text_input(
            f"Point {i+1}",
            value=point,
            key=f"point_{index}_{i}"
        )
        new_points.append(new_point)
    
    # Update the edited slide
    st.session_state.edited_slides[index] = {
        "title": new_title,
        "points": new_points
    }

def create_style_editor():
    """Create interface for editing slide style"""
    st.sidebar.subheader("Edit Style")
    
    # Style customization with unique keys
    background_color = st.sidebar.color_picker(
        "Background Color",
        st.session_state.current_style.get("background_color", "#FFFFFF"),
        key="style_editor_bg_color"
    )
    text_color = st.sidebar.color_picker(
        "Text Color",
        st.session_state.current_style.get("text_color", "#000000"),
        key="style_editor_text_color"
    )
    font_style = st.sidebar.selectbox(
        "Style",
        ["Professional", "Creative", "Minimalist", "Bold"],
        index=0,
        key="style_editor_font_style"
    )
    
    st.session_state.current_style = {
        "background_color": background_color,
        "text_color": text_color,
        "font_style": font_style,
        "guidelines": "Use professional tone, include statistics when available, make content scannable"
    }

def create_carousel(slides_images):
    """Create a carousel preview of slides with edit functionality"""
    if not slides_images:
        return
    
    # Create columns for navigation
    col1, col2, col3 = st.columns([1, 8, 1])
    
    # Previous slide button
    with col1:
        if st.button("◀") and st.session_state.current_slide > 1:
            st.session_state.current_slide -= 1
    
    # Display current slide
    with col2:
        st.image(
            slides_images[st.session_state.current_slide - 1],
            caption=f"Slide {st.session_state.current_slide}/{len(slides_images)}",
            use_column_width=True
        )
        
        # Add edit button for current slide
        if st.button("Edit Current Slide"):
            st.session_state.editing_mode = not st.session_state.editing_mode
    
    # Next slide button
    with col3:
        if st.button("▶") and st.session_state.current_slide < len(slides_images):
            st.session_state.current_slide += 1
    
    # Edit interface
    if st.session_state.editing_mode:
        edit_slide_content(st.session_state.current_slide - 1)
        if st.button("Apply Changes"):
            update_slide_content()
    
    # Navigation slider
    st.slider(
        "Navigate slides",
        min_value=1,
        max_value=len(slides_images),
        value=st.session_state.current_slide,
        key="slide_navigator",
        on_change=update_slide
    )

def main():
    st.title("LinkedIn Slides Generator")
    
    # Input section for initial generation
    if not st.session_state.slides_data:
        input_text = st.text_area(
            "Paste your content here (article, video script, etc.)",
            height=200,
            key="input_text_area"
        )
        
        # Initial style customization with unique keys
        st.subheader("Customize Your Slides")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            background_color = st.color_picker(
                "Background Color",
                "#FFFFFF",
                key="initial_bg_color"
            )
        with col2:
            text_color = st.color_picker(
                "Text Color",
                "#000000",
                key="initial_text_color"
            )
        with col3:
            font_style = st.selectbox(
                "Style",
                ["Professional", "Creative", "Minimalist", "Bold"],
                index=0,
                key="initial_font_style"
            )
        
        style = {
            "background_color": background_color,
            "text_color": text_color,
            "font_style": font_style,
            "guidelines": "Use professional tone, include statistics when available, make content scannable"
        }
        
        # Generate button
        if st.button("Generate Slides", key="generate_button"):
            if input_text:
                with st.spinner("Generating slides..."):
                    try:
                        slides_data = generate_slides_content(input_text, style)
                        if slides_data.caption and slides_data.slides:
                            st.session_state.slides_data = slides_data
                            st.session_state.edited_slides = slides_data.slides
                            st.session_state.current_style = style
                            update_slide_content()
                            st.success("Slides generated successfully!")
                        else:
                            st.error("Failed to generate slides")
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
            else:
                st.error("Please enter some content to generate slides.")
    
    # Display and edit generated content
    if st.session_state.slides_data and st.session_state.slides_images:
        # Create style editor in sidebar
        create_style_editor()
        
        # Display caption
        st.subheader("LinkedIn Caption")
        st.text_area(
            "Caption (copy this to your LinkedIn post)",
            st.session_state.slides_data.caption,
            height=100,
            key="caption_display"
        )
        
        # Display slides carousel with edit functionality
        st.subheader("Preview Slides")
        create_carousel(st.session_state.slides_images)
        
        # Apply style changes button
        if st.sidebar.button("Apply Style Changes", key="apply_style_button"):
            update_slide_content()
        

        
        # Download buttons
        col1, col2 = st.columns(2)
        with col1:
            # Download all slides
            zip_data = create_download_zip(st.session_state.slides_images)
            st.download_button(
                label="📥 Download All Slides",
                data=zip_data,
                file_name="linkedin_slides.zip",
                mime="application/zip",
                help="Download all slides as a ZIP file",
                key="download_all_button"
            )
        
        with col2:
            # Download individual slides
            if st.button("Show Individual Downloads", key="show_individual_downloads"):
                for i, img in enumerate(st.session_state.slides_images, 1):
                    buf = io.BytesIO()
                    img.save(buf, format='PNG')
                    st.download_button(
                        label=f"Download Slide {i}",
                        data=buf.getvalue(),
                        file_name=f"slide_{i}.png",
                        mime="image/png",
                        key=f"download_slide_{i}"
                    )

if __name__ == "__main__":
    main()