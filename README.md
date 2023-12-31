# Logu - Python SDK

The `pylogu` library offers a powerful yet intuitive interface for integrating Logu's real-time monitoring and analytics capabilities into your Python applications. Designed with an emphasis on Developer Experience, it provides easy-to-use functionalities for logging events, identifying users, and gaining insights, all with real-time updates and custom notifications.

## Key Features
- **Developer-Friendly**: Straightforward setup and easy integration.
- **Customizable Logging**: Tailor log details to your project's needs.
- **User Identification**: Easily track and manage user data.
- **Insightful Analytics**: Gain valuable insights with minimal setup.
- **Real-Time Updates**: Stay up-to-date with the latest data.

## About Logu

Revolutionize your business with Logu – the epitome of simplicity and efficiency. Enjoy an unparalleled Developer Experience, an intuitive log interface, and customized notifications. Stay ahead with real-time insights. Logu isn't just a tool; it's your pathway to smarter, faster business decisions.

Start using at: www.logu.app
After creating your account, an API Key, a Project and a Channel, you can start using this: [Logu Example Usage Template](https://replit.com/@kevinqz/Logu-Template) hosted in a Replit Repl

---

# Setup
## 0️⃣Install pylogu

### Using pip
```python
pip install pylogu
```

### Using poetry
```python
poetry add pylogu
```

---

# Simple Usage
## 1️⃣ Import Logu Client
```python
from pylogu import Logu
```

## 2️⃣ Initialize the Logu client
```python
logu = Logu(LOGU_API_KEY, LOGU_PROJECT, LOGU_CHANNEL)
```

## 3️⃣ Using the 'log' function
```python
logu.log(LOGU_EVENT, LOGU_ICON)
# logu.log(LOGU_PROJECT, LOGU_CHANNEL, LOGU_EVENT, LOGU_ICON)
```

## 🙋 Using the 'identify' function
```python
logu.identify(LOGU_USER_ID, LOGU_USER_PROPERTIES)
# logu.identify(LOGU_PROJECT, LOGU_USER_ID, LOGU_USER_PROPERTIES)
```

## 💡 Using the 'insight' function
```python
logu.insight(LOGU_INSIGHT, LOGU_ICON, LOGU_INSIGHT_VALUE)
# logu.insight(LOGU_PROJECT, LOGU_INSIGHT, LOGU_ICON, LOGU_INSIGHT_VALUE)
```

---

# Usage Example
## 1️⃣ Import Logu Client
```python
from pylogu import Logu
```

## 2️⃣ Initialize the Logu client
```python
logu = Logu(
    key=LOGU_API_KEY,
    project=LOGU_PROJECT,
    channel=LOGU_CHANNEL # channel is optional
)
```

## 3️⃣ Using the 'log' function
```python
log_response = logu.log(
    # project=LOGU_PROJECT || None,
    # project is required, but optional if you initiated the client with a project
    # channel=LOGU_CHANNEL || None,
    # channel is required, but optional, even if you didn't initiate the client with a channel
    event=LOGU_EVENT,
    icon=LOGU_ICON
)
print("Log Response:", log_response)
```

## 🙋 Using the 'identify' function
```python
identify_response = logu.identify(
    # project=LOGU_PROJECT || None,
    # project is required, but optional if you initiated the client with a project
    user_id=LOGU_USER_ID,
    properties=LOGU_USER_PROPERTIES
)
print("Identify Response:", identify_response)
```

## 💡 Using the 'insight' function
```python
insight_response = logu.insight(
  # project=LOGU_PROJECT || None,
    # project is required, but optional if you initiated the client with a project
    insight=LOGU_INSIGHT, 
    icon=LOGU_ICON, 
    value=LOGU_INSIGHT_VALUE
)
print("Insight Response:", insight_response)
```

---

# ⚠️ For Test Purposes Only ⚠️

```python
from example_config import * # This file have some example configs that you can adjust according to your needs or set the variables directly in the code
```

## 1️⃣ Import Logu Client
```python
from pylogu import Logu
```

## 2️⃣ Initialize the Logu client
```python
logu = Logu(
    key=LOGU_API_KEY,
    project=LOGU_PROJECT,
    channel=LOGU_CHANNEL # channel is optional
)
```

## 3️⃣ Using the 'log' function
```python
log_response = logu.log(
    project=random.choice([LOGU_PROJECT, None]),
    # project is required, but optional if you initiated the client with a project
    channel=random.choice([LOGU_CHANNEL, None]),
    # channel is required, but optional, even if you didn't initiate the client with a channel
    event=LOGU_EVENT,
    icon=LOGU_ICON
)
print("Log Response:", log_response)
```

## 🙋 Using the 'identify' function
```python
identify_response = logu.identify(
    # project=LOGU_PROJECT,
    # project is required, but optional if you initiated the client with a project
    user_id=LOGU_USER_ID + random.choice(["1", "2"]),
    properties=LOGU_USER_PROPERTIES
)
print("Identify Response:", identify_response)
```

## 💡 Using the 'insight' function
```python
insight_response = logu.insight(
    # project=LOGU_PROJECT,
    # project is required, but optional if you initiated the client with a project
    insight=LOGU_INSIGHT, 
    icon=LOGU_ICON, 
    value=LOGU_INSIGHT_VALUE
)
print("Insight Response:", insight_response)
```
