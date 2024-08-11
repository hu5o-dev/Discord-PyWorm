# Discord Message Spreader 📩💬

A Python script to send messages and optional files to all your Discord friends. The script uses the Discord API to communicate with your friends and offers configurable delays between messages.

## Features ✨

- **Send Messages:** Quickly send a message to all your Discord friends.
- **Send Files:** Optionally attach and send a file with your message.
- **Customizable Delay:** Set a delay between sending messages to avoid rate limits.
- **Graphical File Selection:** Use a file dialog to select files to send.

## Prerequisites 📦

- **Python 3.x:** Ensure Python is installed on your machine.
- **Requests Library:** Used for making HTTP requests. Install it via pip:

  ```bash
  pip install requests
  ```

## How to Use 🛠️

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hu5o-dev/Discord-PyWorm.git
   cd Discord-PyWorm
   ```

2. **Run the Script:**

   Execute the script from your terminal:

   ```bash
   python send_dms.py
   ```

3. **Provide Input:**

   - **Discord Token:** Enter your Discord token when prompted.
   - **Message:** Enter the message you want to send.
   - **Send File:** Specify if you want to send a file. If yes, select the file using the file dialog.
   - **Delay:** Enter the delay between messages in milliseconds.

4. **Automatic Execution:**

   The script will start sending messages and/or files to all your friends, with the specified delay between each message.

## Example Usage 📸

```
Enter your Discord token: [your_token_here]
Enter the message you want to send: Hello there!
Do you want to send a file as well? (yes/no): no
Enter the delay between messages in milliseconds: 1000
```

## Important Notes ⚠️

- **Token Security:** Be cautious with your Discord token. Sharing it can compromise your account. It's recommended to use a separate bot token for such scripts if possible.
- **Rate Limits:** Discord enforces rate limits. If you encounter errors, consider increasing the delay between messages.
- **API Version:** This script uses Discord API v6, which may become outdated. Check the Discord API documentation for updates or modifications.

## Troubleshooting 🛠️

- **Invalid Token:** Ensure your token is correct and has the necessary permissions.
- **File Upload Issues:** Verify that the file is correctly selected and that its size is within acceptable limits for Discord.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions 🤝

Contributions are welcome! Feel free to fork this repository, submit a pull request, or open an issue if you have any suggestions or improvements.

## Acknowledgments 🙌

- Thanks to the Discord API team for providing the tools to interact with Discord programmatically.
