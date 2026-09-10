
"""
class MessagingApp:
	def send_message(self, message):
		print(f"Sending message: {message}")


class WhatsApp(MessagingApp):
	def send_photo(self, photo):
		print(f"Sending photo: {photo}")


whatsapp = WhatsApp()
whatsapp.send_message("Hello!")
whatsapp.send_photo("photo.jpg")

"""


class MessagingApp:
	def send_message(self, message):
		print(f"Sending message: {message}")


class PhotoSharingApp:
	def send_photo(self, photo):
		print(f"Sending photo: {photo}")


class VideoSharingApp:
	def send_video(self, video):
		print(f"Sending video: {video}")


class CallingApp:
	def voice_call(self, contact):
		print(f"Calling {contact}")

	def video_call(self, contact):
		print(f"Starting video call with {contact}")


class StatusApp:
	def post_status(self, status):
		print(f"Posting status: {status}")


class WhatsApp(MessagingApp, PhotoSharingApp, VideoSharingApp, CallingApp, StatusApp):
	pass


whatsapp = WhatsApp()
whatsapp.send_message("Hello!")
whatsapp.send_photo("photo.jpg")
whatsapp.send_video("video.mp4")
whatsapp.voice_call("tej")
whatsapp.video_call("sai")
whatsapp.post_status("Available")


