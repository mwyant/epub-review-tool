# EPUB Review Tool

A self-hosted web tool for proofreading and reviewing EPUB books.

## Features
- **TTS Narration**: Uses browser-native Web Speech API (Windows 11 voices).
- **Format Preservation**: Retains paragraphs, indents, and headers for accurate review.
- **Controller Support**: Use an Xbox controller (A or RT) to mark spots that need editing.
- **Contextual Marking**: Automatically captures the current sentence and the previous sentence for context.
- **Auto-save**: Progress and marks are saved to browser Local Storage.
- **Export**: Download your marks as JSON or CSV.
- **Self-Hosted**: Runs in a Docker container with self-signed SSL for secure API access.

## Quick Start

1. Ensure you have Docker and Docker Compose installed.
2. Clone this repository.
3. Start the tool:
   ```bash
   docker-compose up -d --build
   ```
4. Access the tool at `https://localhost:8002` (or your server's IP).
   - Note: Since it uses a self-signed certificate, you will need to bypass the browser warning.

## How to Use
1. Click **Open EPUB** and select your book.
2. Select a Voice and adjust Speed.
3. Click Play or use the **Jump to Start** field (e.g., "ch1").
4. When you hear something wrong, press **A** or **Right Trigger** on your Xbox controller.
5. Review your marks in the sidebar and export them when finished.

## Troubleshooting Timeouts

If you get a connection timeout (`ERR_TIMED_OUT`) in your browser:

1. **Verify the URL**: Ensure you are using `https://` and not `http://`.
   - Correct: `https://localhost:8002`
2. **Bypass SSL Warning**: You must click "Advanced" and "Proceed" when you see the self-signed certificate warning.
3. **Check Docker Desktop**: Ensure the container `epub-review-player` is listed as "Running" and shows port `8002:8002`.
4. **Try another browser**: If Chrome fails, try Edge or Firefox.
5. **No Proxy**: Ensure your browser or system doesn't have a proxy configured for `localhost` or `127.0.0.1`.
