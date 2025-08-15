import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .model import SEIDR

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SEIDR Model Simulator")

        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the controls
        control_frame = ttk.LabelFrame(self, text="Parameters")
        control_frame.pack(padx=10, pady=10, fill="x")

        # Create sliders for the parameters
        self.beta_slider = self._create_slider(control_frame, "Beta", 0, 1, 0.02)
        self.gamma_slider = self._create_slider(control_frame, "Gamma", 0, 1, 0.1)
        self.delta_slider = self._create_slider(control_frame, "Delta", 0, 1, 0.2)
        self.mu_slider = self._create_slider(control_frame, "Mu", 0, 1, 0.01)
        self.n_slider = self._create_slider(control_frame, "N", 100, 10000, 1000)

        # Create a button to run the simulation
        run_button = ttk.Button(self, text="Run Simulation", command=self.run_simulation)
        run_button.pack(pady=10)

        # Create a frame for the plot
        # Create stats frame
        self.stats_frame = ttk.LabelFrame(self, text="Simulation Statistics")
        self.stats_frame.pack(padx=10, pady=5, fill="x")

        # Create stats labels
        self.peak_day_label = ttk.Label(self.stats_frame, text="Peak Infection Day: ")
        self.peak_day_label.pack(side="left", padx=5)
        
        self.peak_infected_label = ttk.Label(self.stats_frame, text="Peak Infected: ")
        self.peak_infected_label.pack(side="left", padx=5)

        self.total_deaths_label = ttk.Label(self.stats_frame, text="Total Deaths: ")
        self.total_deaths_label.pack(side="left", padx=5)

        # Create plot frame
        plot_frame = ttk.Frame(self)
        plot_frame.pack(padx=10, pady=10)

        # Create a figure and a canvas for the plot
        self.fig = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack()

    def _create_slider(self, parent, text, from_, to, initial_value):
        frame = ttk.Frame(parent)
        frame.pack(fill="x", padx=5, pady=5)

        label = ttk.Label(frame, text=text)
        label.pack(side="left")

        slider = ttk.Scale(frame, from_=from_, to=to, orient="horizontal")
        slider.set(initial_value)
        slider.pack(side="right", fill="x", expand=True)

        return slider

    # Added statistics calculation methods
    def calculate_stats(self, S, E, I, D, R):
        peak_day = np.argmax(I)
        return {
            'peak_day': peak_day,
            'peak_infected': I[peak_day],
            'total_deaths': D[-1]
        }
    
    def update_stats_labels(self, stats):
        self.peak_day_label.config(text=f"Peak Infection Day: {stats['peak_day']}")
        self.peak_infected_label.config(text=f"Peak Infected: {stats['peak_infected']:.0f}")
        self.total_deaths_label.config(text=f"Total Deaths: {stats['total_deaths']:.0f}")

    def run_simulation(self):
        # Get the parameters from the sliders
        beta = self.beta_slider.get()
        gamma = self.gamma_slider.get()
        delta = self.delta_slider.get()
        mu = self.mu_slider.get()
        N = int(self.n_slider.get())

        # Create a SEIDR model and run the simulation
        model = SEIDR(beta, gamma, delta, mu, N)
        t, (S, E, I, D, R) = model.run()

        # Clear the previous plot
        self.fig.clear()

        # Plot the results
        ax = self.fig.add_subplot(111)
        ax.plot(t, S, label="Susceptible")
        ax.plot(t, E, label="Exposed")
        ax.plot(t, I, label="Infected")
        ax.plot(t, D, label="Deceased")
        ax.plot(t, R, label="Recovered")
        ax.set_xlabel("Days")
        ax.set_ylabel("Population")
        ax.legend()
        ax.grid(True)

        # Calculate statistics
        stats = self.calculate_stats(S, E, I, D, R)
        self.update_stats_labels(stats)

        # Redraw the canvas
        self.canvas.draw()

if __name__ == "__main__":
    app = App()
    app.mainloop()