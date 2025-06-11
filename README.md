**Automtion Assessment Task - Sign Up Flow On Magento Website **
**Objective:**
Automate the **sign-up and login flow** on the following e-commerce site:
🔗 [Magento Test Site](https://magento.softwaretestingboard.com/)

**Task Overview:**
1. Automate the **Sign Up** and **Sign In** functionality using Selenium and Python.
2. Follow **BDD (Behavior-Driven Development)** using the **Behave** framework.
3. Use **Page Object Model (POM)** to structure automation code.
4. Document test cases in Excel format.
5. Provide proof of execution (screenshots or screen recording).
6. Push to GitHub with multiple commits and clean folder structure.

---

## 🛠️ Tech Stack

| Category               | Tool / Framework                          |
|------------------------|-------------------------------------------|
| **Language**           | Python                                    |
| **Automation Tool**    | Selenium WebDriver                        |
| **BDD Framework**      | Behave (Gherkin syntax)                   |
| **Design Pattern**     | Page Object Model (POM)                   |
| **Test Runner**        | Behave CLI                                |
| **Reporting**          | (Optional) Allure / Behave JSON Reporter  |
| **Version Control**    | Git & GitHub                              |
| **Documentation**      | Excel for test cases, Markdown for README |

---

## 📁 Project Structure

bash
automation-assessment/
│
├── features/
│   ├── steps/                      # Step Definitions
│   ├── pages/                      # Page Object classes
│   ├── environment.py              # Hooks (setup & teardown)
│   ├── signup_login.feature        # Gherkin feature file
│
├── test-cases/
│   └── test-cases.xlsx             # Excel test plan
│
├── execution-proof/
│   └── screenshots/                # Screenshots or screen recording
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project overview (this file)
`

---

## ✍️ Sample Gherkin Scenario

gherkin
Feature: User Registration and Login

  Scenario: Successful account registration and login
    Given the user is on the Magento registration page
    When the user fills in valid account details
    And submits the form
    Then the account should be successfully created

    When the user logs out and logs back in
    Then the user should be successfully logged in


---

## ▶️ How to Run the Tests

### 1. 📦 Install Dependencies

Make sure Python 3.7+ is installed. Then run:

bash
pip install -r requirements.txt


### 2. 🚀 Run Tests

bash
behave


### 3. 📊 (Optional) Generate Report

If you're using a reporter plugin like Allure:

bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
allure serve reports/


---

## 📸 Proof of Execution

Proof of execution is stored in the `execution-proof/` folder.
Includes:

* Screenshots of successful registration and login
* Screen recording of full test flow

---

## 🧾 Test Case Documentation

You can find test scenarios and steps in:

📄 `test-cases/test-cases.xlsx`

Includes:

* Positive sign-up and login tests
* Negative tests for invalid input
* Edge case handling

---

## 🔗 GitHub Repository

👉 [View Repository on GitHub](https://github.com/Megha-Dg/magento-automation.git)

---

## Author

**\Meghana DoddappaGari**
📧 meghadg2002@gmail.com

---
