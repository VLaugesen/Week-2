# %%
import os

def filter_log(path):
    """
    Reads an input logfile and writes each category of log to seperate files.
    """
    with open(path) as log:
        full_log = log.readlines()

        
    # For each type of log event, write the log lines matching the current type
    with open("WARNING.txt", "w") as warning, open("ERROR.txt", "w") as error, open("SUCCESS.txt", "w") as success, open("INFO.txt", "w") as info:
        for line in full_log:
            if "WARNING" in line:
                warning.write(line)
            
            elif "ERROR" in line:
                error.write(line)

            elif "SUCCESS" in line:
                success.write(line)

            elif "INFO" in line:
                info.write(line)
                
        

# %%
filter_log(os.path.join("..", "Data", "app_log (logfil analyse) - random.txt"))


