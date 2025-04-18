# Entry point to run the Flask application

from app import create_app  # Import the application creation 

# Create the Flask app using the Configs
app = create_app()

if __name__ == "__main__":
    # Run the app in debug mode for development purposes
    # Note: In production, use a WSGI server like gunicorn or uWSGI
    app.run(host="0.0.0.0", port=5000, debug=True)