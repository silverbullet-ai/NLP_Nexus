from flask import Flask, render_template, request
from summarizer import text_summarize, sentiment_analysis, word_cloud
from pdf_extractor import extract_text_from_pdf

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    text = request.form.get("text", "")
    action = request.form.get("action")
    pdf_file = request.files.get("pdf_file")

    # Extract text from PDF if uploaded
    if pdf_file and pdf_file.filename != "":
        pdf_text = extract_text_from_pdf(pdf_file)
        text += "\n" + pdf_text

    if not text.strip():
        return render_template(
            "result.html",
            display="No Result",
            result="No text provided."
        )

    if action == "summarize":
        result = text_summarize(text)
        display = "Summarized Text"
        return render_template("result.html", display=display, result=result)

    elif action == "sentiment":
        result = sentiment_analysis(text)
        display = "Sentiment Analysis"
        return render_template("result.html", display=display, result=result)

    elif action == "wordcloud":
        filename = "wordcloud.png"
        word_cloud(text, filename)
        display = "Word Cloud"
        return render_template("result1.html", display=display)

    return render_template(
        "result.html",
        display="No Result",
        result="Invalid request."
    )


if __name__ == "__main__":
    app.run(debug=True)