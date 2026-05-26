\# Simple File Organizer



A lightweight Python automation script that instantly cleans up cluttered directories by sorting loose files into dedicated folders based on their file extensions.



\## 📁 How It Works



The script scans the directory path you provide and dynamically groups files:

\* `document.pdf` ➔ `pdf\_files/document.pdf`

\* `image.png`    ➔ `png\_files/image.png`

\* `notes`        ➔ `no\_extension\_files/notes`



> \*\*Note:\*\* The script safely processes only individual files and automatically skips existing directories to prevent nested loop issues.



\## 🌟 Features



\* \*\*Dynamic Folder Creation:\*\* Automatically detects file formats and builds sorting folders (e.g., `txt\_files`, `pdf\_files`) on the fly.

\* \*\*Fallback Handling:\*\* Groups files without any file extensions safely into a unified `no\_extension\_files` folder.

\* \*\*Real-Time Logging:\*\* Displays a live console log of every file movement as it happens.

\* \*\*Zero External Dependencies:\*\* Built entirely using Python's native standard libraries (`os` and `shutil`).



\## 🛠️ Installation \& Requirements



\* \*\*Requirement:\*\* Python 3.x installed on your system.

\* No additional packages or installations are required.



\## 🚀 Usage



1\. Clone or download `file\_organizer.py` into your working directory.

2\. Open your terminal or command prompt and execute:

```bash

&#x20;  python file\_organizer.py

3\. Input the absolute or relative path of the directory you want to clean:

```bash

&#x20;  Enter the directory path to organize (e.g., ./test\_folder): ./Downloads



⚠️ Safe Practices

While shutil.move is completely stable, it is always recommended to test the utility on a dummy test folder or back up critical data before running automated file operations on your primary system directories.



📝 License

This project is open-source and available under the MIT License.

