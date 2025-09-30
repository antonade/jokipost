import os
import tweepy
import argparse
from datetime import datetime

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

newapi = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
)

auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)
api_v1 = tweepy.API(auth)

def post_tweet(content):
    try:
        newapi.create_tweet(text=content)
        print("Tweet berhasil diposting!")
    except Exception as e:
        print("Gagal memposting tweet:", e)

def post_tweet_with_image(content, image_path):
    try:
        media = api_v1.media_upload(image_path)
        newapi.create_tweet(text=content, media_ids=[media.media_id])
        print("Tweet dengan gambar berhasil diposting!")
    except Exception as e:
        print("Gagal memposting tweet dengan gambar:", e)

def post_first_tweet():
    content = (
        "LAGI BUTUH JASA OLAH DATA?\n"
        "Mulai dari uji klasik, chisquare, regresi, pearson, normalitas, homogenitas, dan uji lainnya, semua siap dikerjain!\n"
        "Data gak signifikan? Gak normal? Tenang, bisa dibikin cakep.\n"
        "Deadline mepet? Santai, pasti satset!\n"
        "#zonauang #jokispss"
    )
    post_tweet(content)

def post_second_tweet():
    content = (
        "OPEN JOKI SEMUA TUGASAN!\n"
        "- Makalah, essay, sampai artikel ilmiah? Gas!\n"
        "- Spesialis tugas FK/FKG? Ada disini!\n"
        "- Butuh desain? Mau liat porto bisa chat wa\n"
        "- Uji SPSS? Tenang, bisa juga!\n\n"
        "Semua jenis tugas WA: http://wa.me//6281216945469\n\n"
        "#jokitugas #jokidesain #zonauang"
    )
    image_path = "yes.jpeg"
    post_tweet_with_image(content, image_path)

def post_third_tweet():
    content = (
        "JOKI OLAH DATA SPSS MURAH BANGET!\n"
        "• Homogenitas? Beres!\n"
        "• Normalitas? Aman!\n"
        "• Korelasi? Gampang!\n"
        "• Anova (Oneway/Twoway), Regresi, dll? Bisa!\n"
        "Data acak-acakan? Data invalid? Dibikin valid!\n\n"
        "Langsung chat aja di http://wa.me/6281216945469\n\n"
        "#zonauang #jokispss #jokitugas"
    )
    post_tweet(content)

def post_fourth_tweet():
    content = (
        "❌ Data kamu gak normal?\n"
        "❌ Reliabilitas jeblok?\n"
        "❌ Validitas ngambang?\n\n"
        "Tenang, kami bantuin kamu beresin semua uji statistik mulai 20K aja! 💻📊\n\n"
        "📥 DM @jokispssnova\n"
        "📱 WA: 0812-1694-5469\n"
        "💸 Dana, Shopeepay, BCA ready\n\n"
        "#zonauang #jokiskripsi"
    )
    image_path = "baru.jpeg"
    post_tweet_with_image(content, image_path)

def post_tweet_by_choice(choice):
    if choice == 1:
        post_first_tweet()
    elif choice == 2:
        post_second_tweet()
    elif choice == 3:
        post_third_tweet()
    elif choice == 4:
        post_fourth_tweet()
    else:
        print("Pilihan tidak valid.")

def get_daily_choice(offset=0):
    doy = datetime.now().timetuple().tm_yday
    return ((doy - 1 + offset) % 4) + 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--choice", type=int, choices=[1, 2, 3, 4], help="Override choice 1-4")
    parser.add_argument("--offset", type=int, default=0, help="Day offset for cycling")
    args = parser.parse_args()

    choice = args.choice if args.choice else get_daily_choice(args.offset)
    print(f"Posting pilihan ke-{choice}")
    post_tweet_by_choice(choice)