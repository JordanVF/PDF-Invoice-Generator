from tkinter import *
from fpdf import FPDF

window =Tk()
window.title("Invoice Generator")

medicines = {
    "Medicine A":10,
    "Medicine B":20,
    "Medicine C":15,
    "Medicine D":25
}

# 'Shopping Cart'
invoice_items = []

# Add medicine to cart
def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quant_entry.get())
    price = medicines[selected_medicine]
    item_total = price * quantity
    invoice_items.append((selected_medicine,quantity,item_total))
    total_amount_entry.delete(0,END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()

# Update Invoice text box with cart items
def update_invoice_text():
    invoice_text.delete(1.0,END)
    for item in invoice_items:
        invoice_text.insert(END,f"Medicine: {item[0]}, Quantity: {item[1]}, Total: R{item[2]}\n")

# Calculate Total for cart
def calculate_total():
    total = 0.0
    for item in invoice_items:
        total = total + item[2]
    return total

# Generate Invoice PDF
def generate_invoice():
    customer_name = customer_entry.get()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica",size=15)
    # Heading
    pdf.cell(0,10,text="Invoice",new_x="LMARGIN",new_y="NEXT",align="C")
    # Customer Name
    pdf.cell(0,10,text="Customer: "+customer_name,new_x="LMARGIN",new_y="NEXT",align="L")
    # Blank Space
    pdf.cell(0,10,text="",new_x="LMARGIN",new_y="NEXT")

    # Print Invoice items
    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(0,10,text=f"Medicine: {medicine_name}, Quantity: {quantity}, Total: R{item_total}", new_x="LMARGIN",new_y="NEXT",align="L")
    # Print Total
    pdf.cell(0,10,text="Total Amount: R"+str(calculate_total()),new_x="LMARGIN",new_y="NEXT",align="L")
    # Generate PDF
    pdf.output("PDF Generator/PDF Invoice/invoice.pdf")




#region Medicine window
medicine_label = Label(window,text="Medicine: ")
medicine_label.pack()

# List box
medicine_listbox = Listbox(window,selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END,medicine)
medicine_listbox.pack()
#endregion

#region Quantity Entry
quant_label = Label(window,text="Quantity")
quant_label.pack()
quant_entry = Entry(window)
quant_entry.pack()

# Add Medicine button
add_button = Button(window,text="Add Medicine",command=add_medicine)
add_button.pack()
#endregion

#region Total Amount
total_amount_label = Label(window,text="Total Amount: ")
total_amount_label.pack()

total_amount_entry = Entry(window)
total_amount_entry.pack()
#endregion

#region Customer Name 
customer_label = Label(window,text="Customer Name:")
customer_label.pack()

customer_entry = Entry(window)
customer_entry.pack()
#endregion

#region Generate Invoice
generate_button = Button(window,text="Generate Invoice",command=generate_invoice)
generate_button.pack()

# Invoice Text Box
invoice_text = Text(window,height=10,width=50)
invoice_text.pack()
#endregion

window.mainloop()