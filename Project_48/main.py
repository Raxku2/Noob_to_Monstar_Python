from textual.app import App, ComposeResult
from textual.containers import Vertical, ScrollableContainer, Center
from textual.widgets import Static, Header, Footer, Input, Label
from textual.screen import ModalScreen
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from os import getenv
from datetime import datetime, timedelta

load_dotenv()
MONGO_URI = getenv("MONGO_URI")


class LoginForm(ModalScreen):
    def compose(self) -> ComposeResult:
        with Center():
            with Vertical(id="login-panel"):
                yield Label("Enter your username to join the chat:")
                yield Input(placeholder="Username...", id="username-input")

    def on_mount(self) -> None:
        self.query_one("#username-input").focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.value.strip():
            self.dismiss(event.value)


class HelloApp(App):
    CSS = """
    #login-panel {
        width: 40;
        height: auto;
        background: $surface;
        border: thick $primary;
        padding: 1;
    }
    #chat-log {
        height: 1fr;
        border: solid $accent;
        background: $surface;
        padding: 1;
    }
    Input {
        dock: bottom;
        width: 100%;
        margin: 1;
    }
    .message {
        margin-bottom: 1;
        padding: 0 1;
        background: $primary-muted;
        border-left: tall $accent;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            with ScrollableContainer(id="chat-log"):
                yield Static("Welcome! Please log in...", id="status-msg")
            yield Input(placeholder="Type message...", id="user-input")
        yield Footer()

    async def on_mount(self) -> None:
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client.chat_database
        self.collection = self.db.messages

        # FIX: Look back 1 minute to catch recent history or use min for full history
        self.last_timestamp = datetime.utcnow() - timedelta(minutes=1)
        self.username = "Anonymous"

        def set_username(name: str):
            if name:
                self.username = name
                self.notify(f"Logged in as {name}")
                self.query_one("#user-input").focus()

        self.push_screen(LoginForm(), set_username)
        self.set_interval(1.0, self.fetch_new_messages)

    async def fetch_new_messages(self) -> None:
        chat_log = self.query_one("#chat-log")
        cursor = self.collection.find({"timestamp": {"$gt": self.last_timestamp}}).sort(
            "timestamp", 1
        )

        async for message in cursor:
            # 1. Get the author, providing a fallback if it's missing or None
            author = message.get("author") or "Unknown User"
            text = message.get("text", "")

            # 2. Update the timestamp tracker
            msg_time = message.get("timestamp")
            if msg_time and msg_time > self.last_timestamp:
                self.last_timestamp = msg_time

            # 3. Format with bold tags for the name
            msg_text = f"[b][yellow]{author}[/yellow][/b]: {text}"

            new_msg = Static(msg_text, classes="message")
            chat_log.mount(new_msg)
            new_msg.scroll_visible()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        val = event.value.strip()
        if val:
            # Clear input immediately for better UX
            event.input.value = ""
            await self.collection.insert_one(
                {"text": val, "author": self.username, "timestamp": datetime.utcnow()}
            )


if __name__ == "__main__":
    HelloApp().run()
