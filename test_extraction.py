from resumes.utils import extract_resume_text

file_path = "C:/Users/dell/OneDrive/Desktop/luminar/my project/Ai Resume Analyzer/muhammad_yaseen_khan_cv.pdf"

text = extract_resume_text(file_path)

print("EXTRACTED RESUME TEXT:")

print(text)