import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  
from PIL import Image, ImageTk

# Store PhotoImage objects in a list to prevent them from being garbage collected
image_references = []

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username.endswith("@klu.ac.in"):
        open_main_menu()
    else:
        messagebox.showerror("Login Error", "Invalid college email address")

def open_main_menu():
    login_frame.destroy()
    
    main_menu_frame = tk.Frame(app)
    main_menu_frame.pack(fill='both', expand=True)
    
    app.style = ttk.Style()
    app.style.configure("Rounded.TButton", padding=10, relief="raised", borderwidth=5)
    app.style.configure("Rounded.TLabel", font=("Helvetica", 18), padding=5, relief="raised")
    
    main_menu_image = Image.open("klu.jpg")
    main_menu_image = main_menu_image.resize((screen_width, screen_height), Image.LANCZOS)
    main_menu_photo = ImageTk.PhotoImage(main_menu_image)
    image_references.append(main_menu_photo)
    bg_label = tk.Label(main_menu_frame, image=main_menu_photo)
    bg_label.image = main_menu_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    tk.Label(main_menu_frame, text="Welcome to KLU Campus Services", foreground="white", background="green", font=("Helvetica", 24)).pack()
    
    transportation_image = Image.open("Transportation.jpg")
    transportation_image = transportation_image.resize((200, 200), Image.LANCZOS)
    transportation_photo = ImageTk.PhotoImage(transportation_image)
    image_references.append(transportation_photo)
    transportation_button = ttk.Button(main_menu_frame, image=transportation_photo, command=open_vehicle_selection, style="Rounded.TButton")
    transportation_button.image = transportation_photo
    transportation_button.pack(pady=20)
    tk.Label(main_menu_frame, text="TRANSPORTATION", font=("Helvetica", 18), bg="skyblue", foreground="blue").pack(pady=10)
    
    food_ordering_image = Image.open("FoodOrdering.jpg")
    food_ordering_image = food_ordering_image.resize((200, 200), Image.LANCZOS)
    food_ordering_photo = ImageTk.PhotoImage(food_ordering_image)
    image_references.append(food_ordering_photo)
    food_ordering_button = ttk.Button(main_menu_frame, image=food_ordering_photo, command=open_food_ordering, style="Rounded.TButton")
    food_ordering_button.image = food_ordering_photo
    food_ordering_button.pack(pady=20)
    tk.Label(main_menu_frame, text="FOOD ORDERING", font=("Helvetica", 18), bg="skyblue", foreground="blue").pack(pady=10)

def open_vehicle_selection():
    vehicle_selection_window = tk.Toplevel(app)
    
    vehicle_selection_image = Image.open("Road.jpg")
    vehicle_selection_image = vehicle_selection_image.resize((screen_width, screen_height), Image.LANCZOS)
    vehicle_selection_photo = ImageTk.PhotoImage(vehicle_selection_image)
    image_references.append(vehicle_selection_photo)
    bg_label = tk.Label(vehicle_selection_window, image=vehicle_selection_photo)
    bg_label.image = vehicle_selection_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    ambulance_image = Image.open("Ambulance.jpg")
    ambulance_image = ambulance_image.resize((100, 100), Image.LANCZOS)
    ambulance_photo = ImageTk.PhotoImage(ambulance_image)
    image_references.append(ambulance_photo)
    tk.Label(vehicle_selection_window, text="AMBULANCE", font=("Helvetica", 18), bg="skyblue", foreground="blue").pack(pady=10)
    
    ev_image = Image.open("Electronicvehicle.jpg")
    ev_image = ev_image.resize((100, 100), Image.LANCZOS)
    ev_photo = ImageTk.PhotoImage(ev_image)
    image_references.append(ev_photo)
    
    vehicle_type_var = tk.StringVar()
    ambulance_radio = tk.Radiobutton(vehicle_selection_window, image=ambulance_photo, variable=vehicle_type_var, value="Ambulance", font=("Helvetica", 16))
    ev_radio = tk.Radiobutton(vehicle_selection_window, image=ev_photo, variable=vehicle_type_var, value="Electric Vehicle", font=("Helvetica", 16))
    
    ambulance_radio.pack(pady=10)
    ev_radio.pack(pady=10)
    
    tk.Label(vehicle_selection_window, text="ELECTRONIC VEHICLE", font=("Helvetica", 18), bg="skyblue", foreground="blue").pack(pady=10)
    tk.Label(vehicle_selection_window, text="Source:", bg="purple", foreground="white", font=("Helvetica", 18)).pack(pady=(20, 0))
    source_entry = tk.Entry(vehicle_selection_window, font=("Helvetica", 16))
    source_entry.pack(pady=10)
    
    tk.Label(vehicle_selection_window, text="Destination:", bg="purple", foreground="white", font=("Helvetica", 18)).pack(pady=10)
    destination_entry = tk.Entry(vehicle_selection_window, font=("Helvetica", 16))
    destination_entry.pack(pady=10)
    
    tk.Button(vehicle_selection_window, text="Book Vehicle", command=lambda: book_vehicle(vehicle_type_var.get(), source_entry.get(), destination_entry.get()), font=("Helvetica", 16), foreground="white", background="blue", width=10, height=1).pack(pady=10)

def book_vehicle(vehicle_type, source, destination):
    messagebox.showinfo("Booking Confirmation", f"Vehicle Type: {vehicle_type}\nSource: {source}\nDestination: {destination}\nBooking Successful!")

def open_food_ordering():
    food_ordering_window = tk.Toplevel(app)
    food_ordering_window.title("Food Ordering")
    
    food_ordering_image = Image.open("FoodOrderingSystem.jpg")
    food_ordering_image = food_ordering_image.resize((screen_width, screen_height), Image.LANCZOS)
    food_ordering_photo = ImageTk.PhotoImage(food_ordering_image)
    image_references.append(food_ordering_photo)
    bg_label = tk.Label(food_ordering_window, image=food_ordering_photo)
    bg_label.image = food_ordering_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    vendors = [
        {"name": "Nalabagam", "image_file": "Nalabakam.jpg", "categories": ["Breakfast", "Rice Items", "Curries", "Snacks"]},
        {"name": "Sudexo", "image_file": "Sudexo.jpg", "categories": ["Breakfast", "Rice Items", "Curries", "Snacks", "Desserts"]},
        {"name": "Northern Canteen", "image_file": "Northendcanteen.jpg", "categories": ["Breakfast", "Rice Items", "Curries", "Desserts", "Sweets"]}
    ]
    
    vendor_frame = tk.Frame(food_ordering_window)
    vendor_frame.pack(expand=True)
    
    vendor_buttons = []
    
    for vendor in vendors:
        vendor_image = Image.open(vendor["image_file"])
        vendor_image = vendor_image.resize((150, 150), Image.LANCZOS)
        vendor_photo = ImageTk.PhotoImage(vendor_image)
        image_references.append(vendor_photo)
        vendor_button = tk.Button(
            vendor_frame,
            image=vendor_photo,
            command=lambda vendor=vendor: open_vendor_menu(vendor),
        )
        vendor_button.image = vendor_photo
        vendor_buttons.append(vendor_button)
    
    for button in vendor_buttons:
        button.pack(side="left", padx=20)

def open_vendor_menu(vendor):
    vendor_window = tk.Toplevel(app)
    vendor_window.title(vendor["name"])
    
    vendor_image = Image.open("Vendors.jpg")
    vendor_image = vendor_image.resize((screen_width, screen_height), Image.LANCZOS)
    vendor_photo = ImageTk.PhotoImage(vendor_image)
    image_references.append(vendor_photo)
    bg_label = tk.Label(vendor_window, image=vendor_photo)
    bg_label.image = vendor_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    categories = vendor["categories"]
    
    for category in categories:
        category_image = Image.open(f"{category}.jpg")
        category_image = category_image.resize((125, 125), Image.LANCZOS)
        category_photo = ImageTk.PhotoImage(category_image)
        image_references.append(category_photo)
        
        category_button = tk.Button(
            vendor_window,
            image=category_photo,
            command=lambda cat=category, vend=vendor: open_food_category(vend["name"], cat),
        )
        category_button.image = category_photo
        category_button.pack(side="left", padx=10, pady=10)
        tk.Label(vendor_window, text=category, font=("Helvetica", 18), bg="skyblue", foreground="blue").pack(side="left", padx=10)

def open_food_category(vendor_name, category):
    food_category_window = tk.Toplevel(app)
    food_category_window.title(f"{vendor_name} - {category}")
    
    food_category_image = Image.open("food.jpg")
    food_category_image = food_category_image.resize((screen_width, screen_height), Image.LANCZOS)
    food_category_photo = ImageTk.PhotoImage(food_category_image)
    image_references.append(food_category_photo)
    bg_label = tk.Label(food_category_window, image=food_category_photo)
    bg_label.image = food_category_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    food_items = {
        "Breakfast": ["Idli", "Dosa", "Upma", "Puri", "Pesarattu"],
        "Rice Items": ["Veg Biryani", "Chicken Biryani", "Pulao", "Fried Rice", "Curd Rice"],
        "Curries": ["Paneer Butter Masala", "Chole", "Dal Makhani", "Mixed Veg Curry"],
        "Snacks": ["Samosa", "Pakora", "Spring Rolls", "Sandwich"],
        "Desserts": ["Gulab Jamun", "Rasgulla", "Ice Cream", "Halwa"],
        "Sweets": ["Laddu", "Jalebi", "Barfi"]
    }
    
    items = food_items.get(category, [])
    
    for item in items:
        tk.Label(food_category_window, text=item, font=("Helvetica", 18), bg="skyblue", foreground="blue").pack(pady=10)
        # Ensure lambda captures current item correctly
        tk.Button(food_category_window, text=f"Order {item}", command=lambda i=item: order_food_item(vendor_name, i), font=("Helvetica", 16), foreground="white", background="blue").pack(pady=5)

def order_food_item(vendor_name, item):
    print(f"Ordering {item} from {vendor_name}")
    messagebox.showinfo("Order Confirmation", f"{item} from {vendor_name} ordered successfully!")

app = tk.Tk()
app.title("KLU Campus Services")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}")

login_frame = tk.Frame(app)
login_frame.pack(fill='both', expand=True)

bg_image = Image.open("klu.jpg")
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
image_references.append(bg_photo)
bg_label = tk.Label(login_frame, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(login_frame, text="Login", font=("Helvetica", 24), bg="skyblue").pack(pady=20)
username_entry = tk.Entry(login_frame, font=("Helvetica", 16))
username_entry.pack(pady=10)
password_entry = tk.Entry(login_frame, show='*', font=("Helvetica", 16))
password_entry.pack(pady=10)

tk.Button(login_frame, text="Login", command=login, font=("Helvetica", 16), foreground="white", background="blue").pack(pady=20)

app.mainloop()
