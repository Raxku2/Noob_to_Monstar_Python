# Practice Task – Chapter 21 (Web Scraping + API)

## 📝 Task: MAKAUT Notice Notifier

**Goal:**  
Build a **Notice Notifier Program** that checks for new notices from MAKAUT University every few seconds.  
If a new notice is released, show a **desktop notification** and update a local file to store the last notice title.

---

### ✅ Requirements:
1. Fetch the latest notices from the MAKAUT Notice API.
2. Compare the newest notice with the last saved notice in a file (`lastNotice.txt`).
3. If there is a new notice:
   - Display a desktop notification with the notice title.
   - Print the list of latest notices in the console.
   - Save the latest notice title to `lastNotice.txt`.
4. Run the check in an infinite loop with a delay of a few seconds.

---

### 📦 Hints:
- Use **requests** to fetch the data.
- Use **notifypy** for desktop notifications.
- Use **dotenv** for API URL.
- Use `time.sleep()` for periodic checking.
- Handle cases where no new notice is released.
