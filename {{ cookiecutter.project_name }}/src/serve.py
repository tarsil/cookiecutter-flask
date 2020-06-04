#!/usr/bin/env python
import os


if __name__ == "__main__":
    os.environ.setdefault("FLASK_SETTINGS_FILENAME", "configs/settings.py")

    from src.app import create_app

    app = create_app()
    app.run(debug=app.config.get('DEBUG'), use_reloader=app.config.get('AUTO_RELOADER'), 
            port=app.config.get('PORT', 5001))
