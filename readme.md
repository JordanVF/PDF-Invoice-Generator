# Invoice Generator


## Description
A Python application that generates a PDF invoice using `Tkinter` for the GUI and `FPDF` for PDF creation. The app allows users to select medicines, input quantities, and calculate the total amount. Once all items are added to the cart, the user can generate a PDF invoice with the customer name and purchased items.

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PDF-Invoice-Generator.git
2. Navigate to the project directory: 
```bash
cd PDF-Invoice-Generator
```
3. Install the required dependencies:
```bash
pip install fpdf tkinter
```
 
## Usage
1. Run the application
2. In the GUI:
    -Select a medicine from the list.
    -Enter the quantity of the selected medicine.
    -Click Add Medicine to add it to the cart.
    -The total amount will update automatically.
    -Enter the customer's name.
    -Click Generate Invoice to create a PDF file of the invoice in the specified directory.
3. The generated PDF invoice will include the customer's name, a list of purchased medicines with quantities and totals, and the overall total amount.

## How it works
- Tkinter GUI: The app uses Tkinter for the graphical interface. The user selects medicines and quantities, which are added to a cart (invoice items).
- Cart Management: The items in the cart are displayed in a text box with their details (name, quantity, total cost). The total amount is automatically calculated.
- PDF Invoice: Once the user inputs the customer’s name and clicks Generate Invoice, the FPDF library creates a PDF containing the customer’s name, a list of items, and the total amount.
- PDF Output: The PDF invoice is saved to the specified folder, which can be customized.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

