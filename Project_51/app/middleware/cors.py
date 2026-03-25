from fastapi.middleware.cors import CORSMiddleware


def cors_middleware(app):
    """Add CORD Origin Middilware"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allow all headers
    )
