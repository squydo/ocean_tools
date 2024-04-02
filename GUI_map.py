# import xarray as xr
# import matplotlib.pyplot as plt
# import xrscipy
# import numpy as np
# import cartopy.crs as ccrs
# import xesmf as xe
# from matplotlib import colorbar, colors
# from matplotlib.cm import get_cmap
# from roms_regrid import *
# from matplotlib.patches import Rectangle
# import seawater

# ds=xr.open_dataset(r"C:\Users\sydjw\Documents\[C]Worthy\z_Iceland3_BGC_select.20120701130000.nc")

# top = ds.sel(depth=0).sel(time=0)
# top = top.where(top['Alk'] != 0)
# alk_surface = top['Alk']

# # Create the plot
# plt.figure(figsize=(10, 10))
# alk_surface.plot.pcolormesh(x='xi_rho', y='eta_rho')
# plt.title('Surface Alkalinity (Alk) Distribution')
# plt.xlabel('xi_rho')
# plt.ylabel('eta_rho')
# plt.show()


import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import xarray as xr

# Load the dataset
ds = xr.open_dataset(r"C:\Users\sydjw\Documents\[C]Worthy\z_Iceland3_BGC_select.20120701130000.nc")
top = ds.sel(depth=0, method='nearest').isel(time=0)
alk_surface = top['Alk'].where(top['Alk'] != 0)

# Setup the Tkinter window
root = tk.Tk()
root.wm_title("Interactive Rectangle Drawing")

fig, ax = plt.subplots()
alk_surface.plot(ax=ax)

canvas = FigureCanvasTkAgg(fig, master=root)
widget = canvas.get_tk_widget()
widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Initialize global variables
rect = None
start_point = None
drawing = False

def on_click(event):
    global rect, start_point, drawing
    if event.inaxes != ax: return  # Ignore clicks outside the axes

    if not drawing:
        start_point = (event.xdata, event.ydata)
        rect = plt.Rectangle(start_point, 0, 0, fill=False, color='red', linewidth=2)
        ax.add_patch(rect)
        drawing = True
    else:
        finalize_rectangle()

def on_motion(event):
    global rect, start_point
    if drawing and event.inaxes == ax:
        width, height = event.xdata - start_point[0], event.ydata - start_point[1]
        rect.set_width(width)
        rect.set_height(height)
        canvas.draw_idle()

def finalize_rectangle():
    global drawing, rect, start_point
    if drawing:
        drawing = False
        # Calculate bottom-left vertex and deltas
        end_point = (rect.get_x() + rect.get_width(), rect.get_y() + rect.get_height())
        bottom_left_vertex = (min(start_point[0], end_point[0]), min(start_point[1], end_point[1]))
        delta_xi_rho = abs(rect.get_width())
        delta_eta_rho = abs(rect.get_height())
        # Display rectangle information
        display_rectangle_info(bottom_left_vertex, delta_xi_rho, delta_eta_rho)
        # Optionally clear the rectangle after showing info
        rect.remove()
        rect = None
        canvas.draw_idle()

def display_rectangle_info(bottom_left_vertex, delta_xi_rho, delta_eta_rho):
    # Round each component of the bottom_left_vertex individually
    bottom_left_x, bottom_left_y = bottom_left_vertex
    messagebox.showinfo("Rectangle Info",
                        f"Bottom-left vertex: ({round(bottom_left_x, 1)}, {round(bottom_left_y, 1)})\n"
                        f"Delta xi_rho: {round(delta_xi_rho, 1)}, Delta eta_rho: {round(delta_eta_rho, 1)}")
hocke
# Create the button for initiating rectangle drawing after all relevant functions are defined
btn_draw_rectangle = tk.Button(master=root, text="Draw Rectangle", command=lambda: fig.canvas.mpl_connect('button_press_event', on_click))
btn_draw_rectangle.pack(side=tk.BOTTOM)

# Connect motion event to update rectangle while drawing
fig.canvas.mpl_connect('motion_notify_event', on_motion)

tk.mainloop()
