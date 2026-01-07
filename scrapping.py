import asyncio
from TikTokApi import TikTokApi
import pandas as pd

video_url = "https://vt.tiktok.com/ZS59WxY7C/"

async def main():
    comments_data = []

    api = TikTokApi()

    # WAJIB await (INI KUNCI UTAMA)
    await api.create_sessions(
        num_sessions=1,
        sleep_after=3,
        headless=False
    )

    video = api.video(url=video_url)

    async for comment in video.comments(count=1000):
        comments_data.append({
            "text": comment.text
        })

    df = pd.DataFrame(comments_data)
    df.to_csv("tiktok_comments.csv", index=False, encoding="utf-8")

    print("Scraping komentar TikTok selesai!")
    print(df.head())

# Jalankan async
asyncio.run(main())
