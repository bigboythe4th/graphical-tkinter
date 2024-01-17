import tkinter as tk
def predict_stock_price():
    try:
        current_price = float(txtCurrentPrice.get())
        trade_volume = float(txtTradeVolume.get())
        market_sentiment = float(txtMarketSentiment.get())
        market_cap = float(txtMarketCap.get())
        risk_factor = 1 / market_cap  # Smaller market cap results in higher risk
        predicted_price_low = current_price * (1 + ((trade_volume / 100) * market_sentiment - 0.05) * risk_factor)
        predicted_price_high = current_price * (1 + ((trade_volume / 100) * market_sentiment + 0.05) * risk_factor)
        output_label.config(text=f"Predicted Price Range: {predicted_price_low} - {predicted_price_high}")
    except ValueError:
        output_label.config(text="Invalid input, please enter numbers")
window = tk.Tk()
window.title("Stock Prediction Calculator")
window.geometry("600x400")


# Add custom color to background
window.configure(background='light blue')



# Create labels with custom font
custom_font = ('Arial', 12)  # Example of a custom font
lblCurrentPrice = tk.Label(window, text="Current Price:", font=custom_font)
lblTradeVolume = tk.Label(window, text="Trade Volume:", font=custom_font)
lblMarketSentiment = tk.Label(window, text="Market Sentiment:", font=custom_font)
lblMarketCap = tk.Label(window, text="Market Cap (in billions):", font=custom_font)


# Create textboxes with custom font
txtCurrentPrice = tk.Entry(window, font=custom_font)
txtTradeVolume = tk.Entry(window, font=custom_font)
txtMarketSentiment = tk.Entry(window, font=custom_font)
txtMarketCap = tk.Entry(window, font=custom_font)



# Create button
btnPredict = tk.Button(window, text="Predict", command=predict_stock_price)



# Create output label
output_label = tk.Label(window, text="Predicted Price:")


# Add GUI items to a grid
lblCurrentPrice.grid(row=0, column=0, padx=10, pady=10)
lblTradeVolume.grid(row=1, column=0, padx=10, pady=10)
lblMarketSentiment.grid(row=2, column=0, padx=10, pady=10)
lblMarketCap.grid(row=3, column=0, padx=10, pady=10)
txtCurrentPrice.grid(row=0, column=1, padx=10, pady=10)
txtTradeVolume.grid(row=1, column=1, padx=10, pady=10)
txtMarketSentiment.grid(row=2, column=1, padx=10, pady=10)
txtMarketCap.grid(row=3, column=1, padx=10, pady=10)
btnPredict.grid(row=4, column=0, padx=10, pady=10)
output_label.grid(row=4, column=1, padx=10, pady=10)



# Build window
window.mainloop()















