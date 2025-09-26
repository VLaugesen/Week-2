# %%
import re
import os

def process_line(line, line_nr):
    """
    Validates a CSV line with format: customer_id,name,email,purchase_amount
    Raises ValueError with a clear message if the line is invalid.
    Returns the line if valid.
    """
    fields = line.strip().split(',')
    if len(fields) != 4:
        raise ValueError(f"Invalid number of fields on line: {line_nr}")

    customer_id, name, email, purchase_amount = fields

    # Validate customer_id: must be positive integer
    if not customer_id:
        raise ValueError(f"Missing customer_id on line: {line_nr}")
    
    # Strip the value to just an integer
    if not customer_id.strip().lstrip('-').isdigit():
        raise ValueError(f"customer_id is not an integer: '{customer_id}' on line: {line_nr}")
    if int(customer_id) <= 0:
        raise ValueError(f"customer_id must be positive: '{customer_id}' on line: {line_nr}")

    # Validate name: must not be empty
    if not name or not name.strip():
        raise ValueError(f"Name is missing in line: {line_nr}")

    # Validate email through regex for email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    if not email:
        raise ValueError(f"Missing email on line: {line_nr}")
    if not re.match(email_pattern, email.strip()):
        raise ValueError(f"Invalid email: '{email}' on line: {line_nr}")
    
    # Validate purchase_amount: must be positive float
    try:
        amount = float(purchase_amount)
    except ValueError:
        raise ValueError(f"purchase_amount is not a float: '{purchase_amount}' on line: {line_nr}")
    if amount <= 0:
        raise ValueError(f"purchase_amount must be positive: '{purchase_amount}' on line: {line_nr}")

    # Strip any trailing whitespace from name and email before returning the correct line
    return ",".join([customer_id, name.strip(), email.strip(), purchase_amount]) + "\n"

def parse_file(source_path, dest_path):
    """
    Parses a specified input file and copies its data to a specified output file. 
    If an exception occurs during the reading or writing, the program exits with an appropriate message.
    Each line in the input is parsed, and if anything is wrong an exception is raised with a message detailing
    what was wrong and on what line. Otherwise the correct line is added to the data, so only valid lines 
    are written to the destination file.
    """
    data = ["customer_id,name,email,purchase_amount\n"]
    try:
        with open(source_path, 'r') as file:
            lines = file.readlines()
            for i in range(1, len(lines)):
                try:
                    processed_line = process_line(lines[i], i)
                    data.append(processed_line)
                except ValueError as e:
                    print(e)
                except Exception as e:
                    print(f"Unexpected error while parsing line {i}: {e}")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' does not exist.")
    except PermissionError:
        print(f"Error: No read permission for source file '{source_path}'.")
    except Exception as e:
        print(f"Unexpected error while reading source file: {e}")

    try:
        with open(dest_path, 'w') as dest_file:
            dest_file.writelines(data)
        print(f"Data successfully copied from to '{dest_path}'.")
    except PermissionError:
        print(f"Error: No write permission for destination file '{dest_path}'.")
    except Exception as e:
        print(f"Unexpected error while writing to destination file: {e}")



# %%
# Example usage of the script
parse_file(os.path.join("..", "Data", "source_data.csv"), "dest_data.csv")


