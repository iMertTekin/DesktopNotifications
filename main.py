import winsound

import winsound
from plyer import notification

# Bildirim sesini çal
winsound.PlaySound("Rickroll.wav", winsound.SND_FILENAME)

# Bildirim gönderme
notification.notify(
    title = 'Rickroll',
    message = 'HAHAHAHHA RİCROLLANDINNN.',
    app_name = 'Rick Astley',
    app_icon = 'img.ico',
    timeout = 8)
