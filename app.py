
import streamlit as st
import spacy

# Download spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.warning("Downloading spaCy model. This may take some time.")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Rest of your Streamlit app code

# Streamlit app
def main():
    st.title("Named Entity Recognition (NER) Demo")

    # User input
    text_input = st.text_area("Enter text:", "John Doe is the CEO of ABC Corp, and it is located in New York.")

    # NER processing
    if st.button("Extract Entities"):
        doc = nlp(text_input)

        # Display entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        st.write("Named Entities:")
        for entity, label in entities:
            st.write(f"- {entity} ({label})")

if __name__ == "__main__":
    main()
