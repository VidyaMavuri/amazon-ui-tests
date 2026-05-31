# Amazon UI Automation (Python + Selenium)

This project automates:
- Searching for a product on Amazon
- Adding a product to the cart

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager

## 📦 Setup

### 1. Clone the repo
git clone https://github.com/yourname/amazon-ui-tests.git (github.com in Bing)
cd amazon-ui-tests

### 2. Install dependencies
pip install -r requirements.txt


### 3. Run tests
pytest -v


## 📁 Project Structure
- `pages/` – Page Object Model classes
- `tests/` – Test cases
- `utils/` – Driver factory

## ⚠️ Notes
- Amazon UI changes frequently; selectors may need updates.
- Avoid running too many tests to prevent rate limiting.
