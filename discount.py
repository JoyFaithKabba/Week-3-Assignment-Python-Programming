def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount if applicable, otherwise the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def get_float_input(prompt):
    """
    Prompts the user for a float input and handles invalid input.
    
    Parameters:
    prompt (str): The prompt message for user input.
    
    Returns:
    float: The valid float input from the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    price = get_float_input("Enter the original price of the item (in leones): ")
    discount_percent = get_float_input("Enter the discount percentage: ")
    
    final_price = calculate_discount(price, discount_percent)
    
    print(f"The final price is: Le {final_price:.2f}")

if __name__ == "__main__":
    main()
