
async def genStrSession() -> None:  # pylint: disable=missing-function-docstring

    async with Client(

            "KOT_BOTS",

            api_id=int(os.environ.get("APP_ID") or input("Enter Telegram APP ID: ")),

            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: "),

            device_model="CodeXBotz Ver 1.0.1"

    ) as codexbotz:

        print("\nprocessing...")

        await codexbotz.send_message(

            "me", f"<b>@KOT_BOTS User Session</b>\n\n<code>{await codexbotz.export_session_string()}</code>\n\n<i>Keep this Safe and Not share anyone</i>")

        print("Done!, Check your Saved Message for String Session!")

