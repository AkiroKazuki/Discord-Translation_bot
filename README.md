# Discord Translation Bot

## Setup Instructions

### Google Cloud Setup

1. **Create a Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Click on the project drop-down menu at the top of the page.
   - Click on "New Project" and fill in the required details to create a new project.

2. **Enable the Cloud Translation API**:
   - In the Google Cloud Console, navigate to the "APIs & Services" > "Library".
   - Search for "Cloud Translation API" and click on it.
   - Click the "Enable" button to enable the API for your project.

3. **Create Service Account and Download Credentials**:
   - Go to "APIs & Services" > "Credentials".
   - Click on "Create Credentials" > "Service Account".
   - Fill in the required details and click "Create".
   - Assign appropriate roles (e.g., "Project Editor" or "Cloud Translation API User").
   - Click "Done" and then find the created service account in the list.
   - Click on the service account, go to the "Keys" tab, and click "Add Key" > "Create new key".
   - Choose JSON and click "Create". A JSON file will be downloaded.

### Bot Setup

4. **Install Google Cloud SDK**:
   - Follow the instructions to install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).

5. **Authenticate with Google Cloud**:
   ```sh
   gcloud auth login

6. **Set the Google Cloud project:**
   ```sh
   gcloud config set project YOUR_PROJECT_ID


7. **Place the JSON key file in a secure location on your server.**

8. **Set the environment variable:**

**For Unix-based systems (Linux/macOS):**

         ```sh
      export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-file.json

**For Windows:**

        ```cmd
      set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your-service-account-file.json

9. **Clone the repository:**
     ```sh
   git clone https://github.com/yourusername/yourrepository.git
cd yourrepository

10. **Install dependencies:**
     ```sh
      pip install -r requirements.txt

11. **Run the bot:**
     ```sh
      python bot.py
