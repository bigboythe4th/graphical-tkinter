import tkinter as tk

def predict_stock_price():
  try:
      # Convert input values to float
      current_price = float(txtCurrentPrice.get())
      trade_volume = float(txtTradeVolume.get())
      market_sentiment = float(txtMarketSentiment.get())
      market_cap = float(txtMarketCap.get())
      # Calculate risk factor
      risk_factor = 1 / market_cap  # Higher risk for smaller market cap
      if risk_factor > 0.2:
          risk_factor = 0.2  # Limiting the risk factor to a maximum of 20%
      # Calculate predicted price range
      predicted_price_low = current_price * (1 + ((trade_volume / 100) * market_sentiment - 0.05) * risk_factor)
      predicted_price_high = current_price * (1 + ((trade_volume / 100) * market_sentiment + 0.05) * risk_factor)
      # Display the predicted price range
      output_label.config(text="Predicted Price Range: " + format(predicted_price_low, ".2f") + " - " + format(predicted_price_high, ".2f")) #2f used for rounding 
  except ValueError:
      # Handle error if input is not a number
      output_label.config(text="Invalid input, please enter numbers")

# Create the main window
window = tk.Tk()
window.title("Stock Prediction Calculator")
window.geometry("600x400")
window.configure(background='light blue')

# Define a custom font
custom_font = ('Arial', 12)

# Create and place labels
lblCurrentPrice = tk.Label(window, text="Current Price:", font=custom_font, bg='light blue')
lblTradeVolume = tk.Label(window, text="Trade Volume:", font=custom_font, bg='light blue')
lblMarketSentiment = tk.Label(window, text="Market Sentiment:", font=custom_font, bg='light blue')
lblMarketCap = tk.Label(window, text="Market Cap (in billions):", font=custom_font, bg='light blue')

# Create and place entry widgets for user input
txtCurrentPrice = tk.Entry(window, font=custom_font)
txtTradeVolume = tk.Entry(window, font=custom_font)
txtMarketSentiment = tk.Entry(window, font=custom_font)
txtMarketCap = tk.Entry(window, font=custom_font)

# Create and place the "Predict" button
btnPredict = tk.Button(window, text="Predict", command=predict_stock_price)

# Create and place the output label
output_label = tk.Label(window, text="Predicted Price:", bg='light blue')

# Organize widgets using grid layout
lblCurrentPrice.grid(row=0, column=0, padx=10, pady=10)
txtCurrentPrice.grid(row=0, column=1, padx=10, pady=10)
lblTradeVolume.grid(row=1, column=0, padx=10, pady=10)
txtTradeVolume.grid(row=1, column=1, padx=10, pady=10)
lblMarketSentiment.grid(row=2, column=0, padx=10, pady=10)
txtMarketSentiment.grid(row=2, column=1, padx=10, pady=10)
lblMarketCap.grid(row=3, column=0, padx=10, pady=10)
txtMarketCap.grid(row=3, column=1, padx=10, pady=10)
btnPredict.grid(row=4, column=0, columnspan=2, pady=10)
output_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop
window.mainloop()





















