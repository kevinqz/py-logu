# ⚠️ For testing purposes only
import os
import random
# ⚠️ Not necessary for production nor to use with Logu SDK

# API Key for Logu
LOGU_API_KEY = os.environ['LOGU_API_KEY']

# Project and User Information
LOGU_PROJECT = "Projeto 1"
LOGU_CHANNEL = "Canal " + str(random.randint(1, 2))


LOGU_ICON = "⚠️"
LOGU_ICON = random.choice(["⚠️", "\uD83D\uDCA1", "\uD83D\uDCCC", "\uD83D\uDCE2", "\uD83D\uDCAF"])

LOGU_EVENT = "Example Event #" + str(random.randint(0, 9999))

LOGU_USER_ID = "user_" + str(random.randint(0, 9999))
LOGU_USER_PROPERTIES = {
    "email": "user@example.com",
    "name": "John Doe"
}
LOGU_INSIGHT = "User Engagement"
LOGU_INSIGHT_VALUE = str(random.randint(0, 9999))