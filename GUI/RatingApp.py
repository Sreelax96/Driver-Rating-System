import tkinter as tk
from tkinter import messagebox
import pickle

# Load the Random Forest Classifier model
with open('rf_clf.pkl', 'rb') as file:
    rf_clf = pickle.load(file)
def predict_driver_rating():
    # Retrieve input values from the entry fields
    throttle_position = float(entry_throttle_position.get())
    rpm = float(entry_rpm.get())
    speed = float(entry_speed.get())
    load = float(entry_load.get())

    # Make prediction using the model
    input_data = [[throttle_position, rpm, speed, load]]
    predicted_rating = rf_clf.predict(input_data)

    # Show the predicted driver rating in a message box
    messagebox.showinfo("Predicted Driver Rating", f"The predicted driver rating is: {predicted_rating[0]}")

# Create the main window
root = tk.Tk()
root.title("Driver Rating Prediction")

# Create and place entry fields for input
label_throttle_position = tk.Label(root, text="Throttle Position:")
label_throttle_position.grid(row=0, column=0, padx=5, pady=5)
entry_throttle_position = tk.Entry(root)
entry_throttle_position.grid(row=0, column=1, padx=5, pady=5)

label_rpm = tk.Label(root, text="RPM:")
label_rpm.grid(row=1, column=0, padx=5, pady=5)
entry_rpm = tk.Entry(root)
entry_rpm.grid(row=1, column=1, padx=5, pady=5)

label_speed = tk.Label(root, text="Speed:")
label_speed.grid(row=2, column=0, padx=5, pady=5)
entry_speed = tk.Entry(root)
entry_speed.grid(row=2, column=1, padx=5, pady=5)

label_load = tk.Label(root, text="Load:")
label_load.grid(row=3, column=0, padx=5, pady=5)
entry_load = tk.Entry(root)
entry_load.grid(row=3, column=1, padx=5, pady=5)

# Create and place the predict button
predict_button = tk.Button(root, text="Predict Driver Rating", command=predict_driver_rating)
predict_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()