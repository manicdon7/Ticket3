from boa3.builtin import public
from boa3.builtin.interop.storage import put, get

@public
def host() -> dict:
    # Input data from the user
    Event_Name = input("Enter Event Name: ")
    Event_Location = input("Enter Event Location: ")
    Event_date = input("Enter Event Date: ")
    Token_Price = input("Enter Token Price: ")
    Total_Seats = input("Enter Total Seats: ")
    
    # Create a dictionary to store the input data
    group = {
        "Event_Name": Event_Name,
        "Event_Location": Event_Location,
        "Event_date": Event_date,
        "Token_Price": Token_Price,
        "Total_Seats": Total_Seats
    }

    # Store the group dictionary on the blockchain
    put("group_key", group)

    # Return the stored group dictionary
    return group

@public
def get_group() -> dict:
    # Retrieve the stored group dictionary from the blockchain
    group = get("group_key")
    return group
