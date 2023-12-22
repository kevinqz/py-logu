from example_config import * # This file have some example configs that you can adjust according to your needs or set the variables directly in the code


# Simple Usage
## 1️⃣ Import Logu Client
from pylogu.client import Logu

## 2️⃣ Initialize the Logu client
logu = Logu(LOGU_API_KEY, LOGU_PROJECT, LOGU_CHANNEL)

## 3️⃣ Using the 'log' function
logu.log(LOGU_EVENT, LOGU_ICON)
# logu.log(LOGU_PROJECT, LOGU_CHANNEL, LOGU_EVENT, LOGU_ICON)

## 🙋 Using the 'identify' function
logu.identify(LOGU_USER_ID, LOGU_USER_PROPERTIES)
# logu.identify(LOGU_PROJECT, LOGU_USER_ID, LOGU_USER_PROPERTIES)

## 💡 Using the 'insight' function
logu.insight(LOGU_INSIGHT, LOGU_ICON, LOGU_INSIGHT_VALUE)
# logu.insight(LOGU_PROJECT, LOGU_INSIGHT, LOGU_ICON, LOGU_INSIGHT_VALUE)




# Usage Example
## 1️⃣ Import Logu Client
from logu.client import Logu

## 2️⃣ Initialize the Logu client
logu = Logu(
    key=LOGU_API_KEY,
    project=LOGU_PROJECT,
    channel=LOGU_CHANNEL # channel is optional
)

## 3️⃣ Using the 'log' function
log_response = logu.log(
    project=LOGU_PROJECT | None,
    # project is required, but optional if you initiated the client with a project
    channel=LOGU_CHANNEL | None,
    # channel is required, but optional, even if you didn't initiate the client with a channel
    event=LOGU_EVENT,
    icon=LOGU_ICON
)
print("Log Response:", log_response)

## 🙋 Using the 'identify' function
identify_response = logu.identify(
    project=LOGU_PROJECT | None,
    # project is required, but optional if you initiated the client with a project
    user_id=LOGU_USER_ID,
    properties=LOGU_USER_PROPERTIES
)
print("Identify Response:", identify_response)

## 💡 Using the 'insight' function
insight_response = logu.insight(
    # project=LOGU_PROJECT,
    # project is required, but optional if you initiated the client with a project
    insight=LOGU_INSIGHT, 
    icon=LOGU_ICON, 
    value=LOGU_INSIGHT_VALUE
)
print("Insight Response:", insight_response)




# ⚠️ For Test Purposes Only ⚠️
## 1️⃣ Import Logu Client
from logu.client import Logu

## 2️⃣ Initialize the Logu client
logu = Logu(
    key=LOGU_API_KEY,
    project=LOGU_PROJECT,
    channel=LOGU_CHANNEL # channel is optional
)

## 3️⃣ Using the 'log' function
log_response = logu.log(
    project=random.choice([LOGU_PROJECT, None]),
    # project is required, but optional if you initiated the client with a project
    channel=random.choice([LOGU_CHANNEL, None]),
    # channel is required, but optional, even if you didn't initiate the client with a channel
    event=LOGU_EVENT,
    icon=LOGU_ICON
)
print("Log Response:", log_response)

## 🙋 Using the 'identify' function
identify_response = logu.identify(
    # project=LOGU_PROJECT,
    # project is required, but optional if you initiated the client with a project
    user_id=LOGU_USER_ID + random.choice(["1", "2"]),
    properties=LOGU_USER_PROPERTIES
)
print("Identify Response:", identify_response)

## 💡 Using the 'insight' function
insight_response = logu.insight(
    # project=LOGU_PROJECT,
    # project is required, but optional if you initiated the client with a project
    insight=LOGU_INSIGHT, 
    icon=LOGU_ICON, 
    value=LOGU_INSIGHT_VALUE
)
print("Insight Response:", insight_response)