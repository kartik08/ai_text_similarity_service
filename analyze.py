from flask import request, jsonify, current_app
from text_sanitization import sanitize_input, sanitize_output
from text_similarity import cosine_sim, jaccard_sim
from llm_handler import query_llm


def analyze_route(app):
    """
    Registers the /analyze route on the Flask app
    :param app: Flask instance
    """
    @app.route("/analyze", methods=["POST"])
    def analyze():
        """
        Endpoint that accepts two prompts, calculates similarity,
        and sends one prompt to an LLM if similar enough for this i have selected similarity as 80 Percent.
        :return: JSON response with similarity score and LLM response if applicable
        """
        try:
            data = request.get_json(force=True)
            current_app.logger.info(f"Incoming request: {data}")

            # Validate inputs
            prompt1_raw = data.get("prompt1")
            prompt2_raw = data.get("prompt2")

            if not prompt1_raw or not prompt2_raw:
                return jsonify({'error': 'Both prompt1 and prompt2 are required.'}), 400

            # Sanitize inputs
            prompt1 = sanitize_input(prompt1_raw)
            prompt2 = sanitize_input(prompt2_raw)

            # Choose similarity method
            method = data.get("method", "cosine").lower()
            if method not in {"cosine", "jaccard"}:
                current_app.logger.warning(f"Unknown method '{method}', defaulting to 'cosine'")
                method = "cosine"

            # Compute similarity
            similarity_func = jaccard_sim if method == "jaccard" else cosine_sim
            score = similarity_func(prompt1, prompt2)
            response_text = ""

            # Query LLM if similar enough
            if score > 0.5:
                response_text = sanitize_output(query_llm(prompt1))

            return jsonify({
                "similarity_score": round(score, 3),
                "response": response_text
            })

        except Exception as e:
            current_app.logger.exception("Unexpected error during /analyze request")
            return jsonify({'error': 'Internal server error'}), 500
