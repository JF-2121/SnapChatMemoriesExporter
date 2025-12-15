# SnapChatMemoriesExporter

#### A simple tool to bulk download your Snapchat Memories (Photos & Videos), from your data export so you can save them locally and wipe your account.

## Part 1: Get Your DataSnapchat doesn't let you download everything at once easily. You need their official data export file first.

1. Log in to [accounts.snapchat.com](https://accounts.snapchat.com).
2. Click **My Data**.
3. Scroll to **Export your Memories** and toggle it **ON**.
4. **Uncheck** "Export Data by Date Range" (to get everything).
5. Click **Submit Request**.
6. Wait for the email (can take 24h).
7. Download the ZIP file, extract it, and find `memories_history.html`.

---

## Part 2: Download Your FilesThis script reads the hidden links in your HTML file and downloads them with the correct dates.

### 1. Setup* **Install Python:**
* **Windows:** [Download here](https://www.python.org/downloads/). (Check "Add Python to PATH" during install).
* **Mac/Linux:** You likely have it. Type `python3 --version` in terminal to check.


* **Prepare Folder:**
* Create a folder named `snapchat_backup`.
* Put your `memories_history.html` file inside it.
* Create a file named `download.py` inside it and paste the code below.


### 2. Copy The Script from the repo (`download_memories.py`)

### 3. Run It -> Open your terminal/command prompt, navigate to the folder, and run:

**Windows:**

```bash
cd Desktop\snapchat_backup
python download.py

```

**Mac / Linux:**

```bash
cd ~/Desktop/snapchat_backup
python3 download.py

```

---

## Part 3: Delete From SnapchatOnce you have verified your files are safe locally:

### Option A: Manual Delete (Keep Account)
1. Open Snapchat app -> **Memories**.
2. Hold one Snap to select.
3. Tap **Select All** (top right).
4. Tap **Delete**.
* *Note: For >5GB, the app can crash. You can do this in batches (e.g., month by month).*



### Option B: Nuke Everything (Delete Account)
1. Go to [accounts.snapchat.com](https://accounts.snapchat.com).
2. Select **Delete My Account**.
3. Wait 30 days without logging in. All data is wiped permanently.


Enjoy :) 
