# ☕ Coffee Machine Project

## 📖 Overview
This project simulates a **Coffee Machine** in Python.  
It allows users to order different types of coffee, insert coins for payment, and manages machine resources like water, milk, coffee, and sugar.  
The machine also tracks profit, provides reports, and includes a **refill system** with user confirmation.  
To make it fun, the program displays an ASCII art **coffee logo** when serving drinks.

---

## ✨ Features
- **Menu System**: Choose from available coffee drinks.
- **Coin Payment**: Insert quarters, dimes, nickels, and pennies.
- **Transaction Handling**: Calculates total money, checks against drink price, returns change.
- **Resource Management**:
  - Deducts water, milk, coffee, and sugar per drink.
  - Warns when any resource drops below 70 units.
  - Offers refill option (500 units) with cost deducted from profit.
  - If profit is insufficient, asks user to insert coins to cover refill cost.
  - Rewards user with **extra coffee capacity** when they help refill.
- **Reports**: Displays current resources and profit.
- **ASCII Art Coffee Logo**: Prints a coffee cup when a drink is served or machine shuts down.

---

## 🛠️ How It Works
1. **Start Program** → Machine prompts for input.
2. **Order Coffee** → Type the coffee name (e.g., `Latte`).
3. **Insert Coins** → Enter number of quarters, dimes, nickels, and pennies.
4. **Transaction**:
   - If enough money → Coffee is served, change returned.
   - If not enough → Payment refunded.
5. **Resource Check**:
   - If any resource < 70 → Machine asks if you want to refill.
   - If refill confirmed → Deducts cost from profit or asks for extra coins.
   - Shows updated report after refill.
6. **Reports** → Type `Report` to see resources and profit.
7. **Menu** → Type `Menu` to see available drinks.
8. **Shutdown** → Type `Off` to turn off the machine (shows ASCII coffee logo).

---

## 📂 File Structure
- `15_COFFEE_MACHINE.py` → Main program file.
- `Menu` → Contains coffee recipes (name, price, resource requirements).
- `README.md` → Project summary and instructions.

---

## 🎨 ASCII Coffee Logo
Displayed when serving drinks or shutting down:

