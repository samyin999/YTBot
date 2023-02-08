from twitchtube.video import make_video


make_video(
    data=["c xQc", "c Mizkif", "c Trainwreckstv", "c forsen", "game Just Chatting"],
    client_id="1hq8ektpki36w5kn37mluioungyqjo",  # example client id (fake)
    oauth_token="9f5einm9qtp0bj4m9l1ykevpwdn98o",  # example token (fake)
    video_length=10.5,
    resolution=(1920, 1080),
    frames=60,
)
